"""Dependency-free structural and privacy checks; run from the repository root."""
from pathlib import Path
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
    if path.suffix.lower() in {'.jpg', '.jpeg', '.png', '.webp', '.pdf', '.docx', '.xlsx', '.mp4'}:
        failures.append(f'Unexpected media: {rel}')
    if path.suffix.lower() in {'.html', '.md', '.txt', '.json', '.py', '.js', '.css', '.yml'}:
        data = path.read_text(encoding='utf-8')
        if re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', data):
            failures.append(f'Possible private key: {rel}')
if (root / 'content').exists():
    for needed in ('START.html', 'SOURCES.md', 'STARTERGUIDE.md'):
        if not (root / needed).exists():
            failures.append(f'Missing country file: {needed}')
    cards = list((root / 'content').glob('*.json'))
    if len(cards) < 9:
        failures.append('Expected at least nine country cards')
if failures:
    print('\n'.join(failures), file=sys.stderr)
    sys.exit(1)
print('Structural and basic privacy checks passed.')
