"""Check the distributable ZIP and optional media catalogue without a network."""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from html.parser import HTMLParser
from urllib.parse import unquote
import shutil
import subprocess

root = Path(__file__).resolve().parents[1]
zip_path = root / 'dist/US-2026.11.09-r2.zip'
assert zip_path.is_file(), 'Run python tools/package.py first'

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.remote_assets = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'href' in a:
            self.links.append(a['href'])
        if 'src' in a:
            self.links.append(a['src'])
        if tag in ('script', 'link', 'img') and a.get('src', a.get('href', '')).startswith(('http:', 'https:')):
            self.remote_assets.append(tag)

with TemporaryDirectory() as tmp:
    target = Path(tmp)
    with ZipFile(zip_path) as z:
        assert z.testzip() is None
        names = z.namelist()
        assert all(not n.startswith(('.git/', 'dist/', 'personal/', 'private/', 'tools/', 'content/')) for n in names)
        assert {'00-READ-ME-US.pdf', '00-READ-ME-US.txt', 'START.html', 'README.md'} <= set(names)
        assert all(n.split('/')[0] in {'00-READ-ME-US.pdf', '00-READ-ME-US.txt', 'START.html', 'README.md', 'Guides', 'My-Files', 'Private-Files', 'Infrastructure'} for n in names)
        z.extractall(target)
    start = target / 'START.html'
    assert start.is_file()
    parser = Links()
    parser.feed(start.read_text(encoding='utf-8'))
    assert not parser.remote_assets, 'Offline page depends on network assets'
    for link in parser.links:
        if not link.startswith(('#', 'http:', 'https:', 'mailto:')):
            assert (target / unquote(link)).is_file(), link
    assert len(list((target / 'Guides').glob('*.txt'))) >= 9
    assert (target / '00-READ-ME-US.pdf').read_bytes().startswith(b'%PDF-')
    assert 'Copy the package to your drive' in (target / '00-READ-ME-US.txt').read_text(encoding='utf-8')
    manifest = (target / 'Infrastructure/CHECKSUMS.sha256').read_text(encoding='utf-8')
    from hashlib import sha256
    for line in manifest.splitlines():
        digest, rel = line.split('  ', 1)
        assert sha256((target / rel).read_bytes()).hexdigest() == digest, rel
    sample = target / 'My-Files/Photos/TESTPHOTO.txt'
    sample.write_text('harmless test', encoding='utf-8')
    subprocess.run(['python', 'Infrastructure/Optional-Tools/UPDATE-CATALOG.py'], cwd=target, check=True, capture_output=True)
    assert 'TESTPHOTO.txt' in start.read_text(encoding='utf-8')
    assert sample.read_text(encoding='utf-8') == 'harmless test'
print('ZIP extraction, offline links/assets, guides, and media indexing passed.')
