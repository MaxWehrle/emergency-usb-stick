"""Make a clean German ZIP; never include user's files from personal/ or private/."""
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
allowed = ['START.html', 'STARTERGUIDE.md', 'SOURCES.md', 'LICENSE', 'README.md',
           'CONTRIBUTING.md', 'assets/app.js', 'assets/style.css', 'assets/stecker.svg', 'tools/build.py',
           'tools/verify.py', 'tools/package.py', 'MANIFEST.sha256',
           'private/README.txt']
allowed += [p.relative_to(root).as_posix() for folder in ('content', 'guides')
            for p in (root / folder).glob('*') if p.is_file()]
allowed += [f'personal/{folder}/README.txt' for folder in ('Fotos', 'Karten', 'Dokumente')]
allowed = sorted(set(allowed))
missing = [rel for rel in allowed if rel != 'MANIFEST.sha256' and not (root / rel).is_file()]
if missing:
    raise SystemExit(f'Missing files: {missing}')
def canonical_bytes(rel):
    # All allowlisted files are text. LF makes hashes and ZIP bytes independent
    # of Windows checkout settings; user media is never packaged here.
    return (root / rel).read_bytes().replace(b'\r\n', b'\n')

manifest = '\n'.join(f'{sha256(canonical_bytes(rel)).hexdigest()}  {rel}'
                     for rel in allowed if rel != 'MANIFEST.sha256') + '\n'
(root / 'MANIFEST.sha256').write_bytes(manifest.encode('utf-8'))
out = root / 'dist' / 'DE-2026.11.09-r4.zip'
out.parent.mkdir(exist_ok=True)
with ZipFile(out, 'w', ZIP_DEFLATED) as z:
    for rel in allowed:
        info = ZipInfo(rel, date_time=(2026, 11, 9, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        z.writestr(info, canonical_bytes(rel))
print(f'{out} SHA-256 {sha256(out.read_bytes()).hexdigest()}')
