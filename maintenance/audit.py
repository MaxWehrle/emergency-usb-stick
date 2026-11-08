"""Read-only audit for a checked-out country branch. Python 3.12, no dependencies."""
from argparse import ArgumentParser
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
from urllib.request import Request, urlopen
import json
import re

parser = ArgumentParser()
parser.add_argument('--country', required=True, type=Path, help='Path to checked-out country branch')
parser.add_argument('--max-age-days', type=int, default=180)
parser.add_argument('--check-links', action='store_true', help='Perform best-effort HTTP checks')
args = parser.parse_args()
root = args.country.resolve()
errors, warnings = [], []
if not (root / 'START.html').is_file():
    errors.append('START.html missing')
if not (root / 'SOURCES.md').is_file():
    errors.append('SOURCES.md missing')
sources = (root / 'SOURCES.md').read_text(encoding='utf-8') if (root / 'SOURCES.md').is_file() else ''
source_ids = set(re.findall(r'^\| ([A-Z][A-Z0-9-]+) \|', sources, re.M))
urls = sorted(set(re.findall(r'https?://[^\s|)>]+', sources)))
today = date.today()
cards = list((root / 'content').glob('*.json'))
if len(cards) < 9:
    errors.append(f'Only {len(cards)} cards')
for path in cards:
    try:
        c = json.loads(path.read_text(encoding='utf-8'))
        checked = date.fromisoformat(c['reviewed'])
        if (today - checked).days > args.max_age_days:
            warnings.append(f'{path.name}: review date is {(today-checked).days} days old')
        for source_id in c['source_ids']:
            if source_id not in source_ids:
                errors.append(f'{path.name}: unknown source {source_id}')
        if not (root / 'guides' / f"{c['slug']}.md").is_file():
            errors.append(f'{path.name}: plain-text guide missing')
    except (ValueError, KeyError, json.JSONDecodeError) as exc:
        errors.append(f'{path.name}: {exc}')

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        self.hrefs.extend(value for key, value in attrs if key == 'href' and value)

if (root / 'START.html').is_file():
    links = Links()
    links.feed((root / 'START.html').read_text(encoding='utf-8'))
    for href in links.hrefs:
        if not href.startswith(('#', 'http:', 'https:', 'mailto:')) and not (root / unquote(href)).is_file():
            errors.append(f'Broken local link: {href}')

for path in root.rglob('*'):
    if not path.is_file() or any(part in {'.git', 'dist', '__pycache__'} for part in path.parts):
        continue
    rel = path.relative_to(root).as_posix()
    if rel.startswith('private/') and rel != 'private/README.txt':
        errors.append(f'Unexpected file in private/: {rel}')
    if rel.startswith('personal/') and not rel.endswith('/README.txt'):
        errors.append(f'Unexpected public media: {rel}')
    if path.suffix.lower() in {'.jpg', '.jpeg', '.png', '.pdf', '.docx', '.xlsx', '.mp4', '.key', '.pem'}:
        errors.append(f'Unexpected media/secret candidate: {rel}')

if args.check_links:
    for url in urls:
        try:
            req = Request(url, method='HEAD', headers={'User-Agent': 'EmergencyUSB-audit/1.0'})
            with urlopen(req, timeout=12) as response:
                if response.status >= 400:
                    warnings.append(f'HTTP {response.status}: {url}')
        except Exception as exc:
            warnings.append(f'Link needs manual check: {url} ({type(exc).__name__})')

report = {'country_path': str(root), 'cards': len(cards), 'source_ids': len(source_ids),
          'external_links': len(urls), 'errors': errors, 'warnings': warnings}
print(json.dumps(report, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)
