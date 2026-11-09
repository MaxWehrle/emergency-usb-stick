"""Dependency-free structural and privacy checks; run from the repository root."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from urllib.parse import unquote
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
failures = []
for path in root.rglob('*'):
    if not path.is_file() or '.git' in path.parts or 'dist' in path.parts:
        continue
    rel = path.relative_to(root).as_posix()
    if rel.startswith('private/') and rel != 'private/README.txt':
        failures.append(f'Unexpected private file: {rel}')
    if rel.startswith('personal/') and not rel.endswith('/README.txt'):
        failures.append(f'Unexpected personal file: {rel}')
    if path.suffix.lower() in {'.jpg', '.jpeg', '.png', '.webp', '.pdf', '.docx', '.xlsx', '.mp4'} and rel != '00-READ-ME-US.pdf':
        failures.append(f'Unexpected media: {rel}')
    if path.suffix.lower() in {'.html', '.md', '.txt', '.json', '.py', '.js', '.css', '.yml'}:
        data = path.read_text(encoding='utf-8')
        if re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', data):
            failures.append(f'Possible private key: {rel}')
if (root / 'content').exists():
    for needed in ('START.html', 'SOURCES.md', 'STARTERGUIDE.md'):
        if not (root / needed).exists():
            failures.append(f'Missing country file: {needed}')
    cards = [p for p in (root / 'content').glob('*.json') if p.name not in {'site.json', 'package.json', 'readme_pdf.json'}]
    if len(cards) < 9:
        failures.append('Expected at least nine country cards')
    source_text = (root / 'SOURCES.md').read_text(encoding='utf-8') if (root / 'SOURCES.md').exists() else ''
    for card in cards:
        obj = json.loads(card.read_text(encoding='utf-8'))
        for source_id in obj.get('source_ids', []):
            if f'| {source_id} |' not in source_text:
                failures.append(f'Unknown source {source_id} in {card.name}')
    class Links(HTMLParser):
        def __init__(self):
            super().__init__()
            self.hrefs = []
        def handle_starttag(self, tag, attrs):
            self.hrefs.extend(v for k, v in attrs if k == 'href' and v)
    if (root / 'START.html').exists():
        parser = Links()
        parser.feed((root / 'START.html').read_text(encoding='utf-8'))
        for href in parser.hrefs:
            if not href.startswith(('#', 'http:', 'https:', 'mailto:')) and not (root / unquote(href)).is_file():
                failures.append(f'Broken local link: {href}')
    manifest = root / 'MANIFEST.sha256'
    if manifest.exists():
        for line in manifest.read_text(encoding='utf-8').splitlines():
            digest, rel = line.split('  ', 1)
            p = root / rel
            if not p.is_file():
                failures.append(f'Checksum mismatch: {rel}')
                continue
            data = p.read_bytes()
            if p.suffix.lower() in {'.html', '.md', '.txt', '.json', '.py', '.js', '.css', '.yml', '.svg'} or p.name in {'LICENSE', '.gitignore'}:
                data = data.replace(b'\r\n', b'\n')
            if sha256(data).hexdigest() != digest:
                failures.append(f'Checksum mismatch: {rel}')
if failures:
    print('\n'.join(failures), file=sys.stderr)
    sys.exit(1)
print('Structural and basic privacy checks passed.')
