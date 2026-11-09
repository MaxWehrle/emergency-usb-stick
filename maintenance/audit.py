"""Read-only structural audit of a country branch directory or release ZIP.

Checks can flag missing evidence; they cannot approve medical or regional advice.
Python 3.12, standard library only.
"""
from argparse import ArgumentParser
from datetime import date
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import unquote
from urllib.request import Request, urlopen
from zipfile import ZipFile
import json
import re

parser = ArgumentParser()
parser.add_argument('--country', required=True, type=Path, help='Country branch directory or release ZIP')
parser.add_argument('--max-age-days', type=int, default=180)
parser.add_argument('--check-links', action='store_true', help='Best-effort HTTP checks; review content manually')
args = parser.parse_args()
errors, warnings = [], []

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        self.hrefs.extend(value for key, value in attrs if key == 'href' and value)

def audit(root):
    root = root.resolve()
    infra = root / 'Infrastruktur' if (root / 'Infrastruktur').is_dir() else root / 'Infrastructure'
    if not infra.is_dir():
        errors.append('Localized infrastructure folder missing')
        return {}
    is_de = infra.name == 'Infrastruktur'
    guides_name = 'Anleitungen' if is_de else 'Guides'
    files_name = 'Eigene-Dateien' if is_de else 'My-Files'
    private_name = 'Vertrauliche-Dateien' if is_de else 'Private-Files'
    pdf_name = '00-LIESMICH-DE.pdf' if is_de else '00-READ-ME-US.pdf'
    txt_name = '00-LIESMICH-DE.txt' if is_de else '00-READ-ME-US.txt'
    sources_name = 'QUELLEN.md' if is_de else 'SOURCES.md'
    manifest_name = 'PRUEFSUMMEN.sha256' if is_de else 'CHECKSUMS.sha256'
    source = infra if (infra / 'content').is_dir() else infra / ('Quellcode' if is_de else 'Source-Code')
    content = source / 'content'
    expected_locale = 'de-DE' if is_de else 'en-US'
    for name in ('START.html', pdf_name, txt_name):
        if not (root / name).is_file():
            errors.append(f'Missing top-level file: {name}')
    if (root / pdf_name).is_file() and not (root / pdf_name).read_bytes().startswith(b'%PDF-'):
        errors.append(f'Invalid PDF header: {pdf_name}')
    for name in (guides_name, files_name, private_name):
        if not (root / name).is_dir():
            errors.append(f'Missing localized folder: {name}')
    sources_path = infra / sources_name
    if not sources_path.is_file():
        errors.append(f'Missing source register: {sources_path.relative_to(root)}')
    sources = sources_path.read_text(encoding='utf-8') if sources_path.is_file() else ''
    source_ids = set(re.findall(r'^\| ([A-Z][A-Z0-9-]+) \|', sources, re.M))
    urls = sorted(set(re.findall(r'https?://[^\s|)>]+', sources)))
    cards = [p for p in content.glob('*.json') if p.name not in {'site.json', 'package.json', 'readme_pdf.json'}]
    if len(cards) < 9:
        errors.append(f'Only {len(cards)} situation cards')
    site_path = content / 'site.json'
    if not site_path.is_file():
        errors.append('Missing content/site.json')
    else:
        try:
            site = json.loads(site_path.read_text(encoding='utf-8'))
            if site['locale'] != expected_locale:
                errors.append('site.json: locale does not match package')
            if (root / 'START.html').is_file() and f'<html lang="{expected_locale}"' not in (root / 'START.html').read_text(encoding='utf-8'):
                errors.append('START.html: language tag differs from package')
        except (KeyError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f'site.json: {exc}')
    for path in cards:
        try:
            card = json.loads(path.read_text(encoding='utf-8'))
            checked = date.fromisoformat(card['reviewed'])
            if (date.today() - checked).days > args.max_age_days:
                warnings.append(f'{path.name}: review date is {(date.today()-checked).days} days old')
            for source_id in card['source_ids']:
                if source_id not in source_ids:
                    errors.append(f'{path.name}: unknown source {source_id}')
            guide = root / guides_name / f"{card['slug']}.txt"
            if not guide.is_file():
                errors.append(f'{path.name}: user-visible text guide missing')
        except (KeyError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f'{path.name}: {exc}')
    if (root / 'START.html').is_file():
        links = Links()
        html = (root / 'START.html').read_text(encoding='utf-8')
        links.feed(html)
        for href in links.hrefs:
            if not href.startswith(('#', 'http:', 'https:', 'mailto:')) and not (root / unquote(href)).is_file():
                errors.append(f'Broken local link: {href}')
        if '.step b{' in html:
            errors.append('Broad .step b selector can corrupt text emphasis')
    for path in root.rglob('*'):
        if not path.is_file() or any(part in {'.git', 'dist', '__pycache__'} for part in path.parts):
            continue
        rel = path.relative_to(root).as_posix()
        if rel.startswith(private_name + '/') and rel != f'{private_name}/{"HINWEIS.txt" if is_de else "README.txt"}':
            errors.append(f'Unexpected public private file: {rel}')
        if rel.startswith(files_name + '/') and not rel.endswith(('/HINWEIS.txt', '/README.txt', '/VORLAGE.txt', '/TEMPLATE.txt', '-TEMPLATE.txt')):
            errors.append(f'Unexpected public personal file: {rel}')
        if path.suffix.lower() in {'.jpg', '.jpeg', '.png', '.webp', '.pdf', '.docx', '.xlsx', '.mp4', '.key', '.pem'} and rel != pdf_name:
            errors.append(f'Unexpected media/secret candidate: {rel}')
        if path.suffix.lower() in {'.txt', '.md', '.html', '.json', '.py', '.js', '.css', '.svg'}:
            if re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', path.read_text(encoding='utf-8')):
                errors.append(f'Possible private key: {rel}')
    manifest = infra / manifest_name
    if not manifest.is_file():
        errors.append(f'Missing checksum manifest: {manifest.relative_to(root)}')
    else:
        for line in manifest.read_text(encoding='utf-8').splitlines():
            try:
                digest, name = line.split('  ', 1)
                path = root / name
                if not path.is_file():
                    source_prefix = f'{infra.name}/{"Quellcode" if is_de else "Source-Code"}/'
                    if name.startswith(source_prefix):
                        path = infra / name[len(source_prefix):]
                if not path.is_file():
                    errors.append(f'Missing checksum target: {name}')
                    continue
                data = path.read_bytes()
                if path.suffix.lower() in {'.html', '.md', '.txt', '.json', '.py', '.js', '.css', '.svg'} or path.name == 'LICENSE':
                    data = data.replace(b'\r\n', b'\n')
                if sha256(data).hexdigest() != digest:
                    errors.append(f'Checksum mismatch: {name}')
            except ValueError:
                errors.append(f'Malformed checksum line: {line[:60]}')
    if args.check_links:
        for url in urls:
            try:
                with urlopen(Request(url, method='HEAD', headers={'User-Agent': 'EmergencyUSB-audit/1.0'}), timeout=12) as response:
                    if response.status >= 400:
                        warnings.append(f'HTTP {response.status}: {url}')
            except Exception as exc:
                warnings.append(f'Link needs manual check: {url} ({type(exc).__name__})')
    return {'country_path': str(root), 'locale': expected_locale, 'cards': len(cards),
            'source_ids': len(source_ids), 'external_links': len(urls)}

if args.country.suffix.lower() == '.zip':
    with TemporaryDirectory(prefix='emergency-usb-audit-') as temp:
        with ZipFile(args.country) as archive:
            names = archive.namelist()
            if any(name.startswith('/') or '..' in Path(name).parts or '\\' in name for name in names):
                errors.append('Unsafe ZIP path')
                result = {}
            else:
                archive.extractall(temp)
                result = audit(Path(temp))
else:
    result = audit(args.country)
result.update({'errors': errors, 'warnings': warnings})
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)
