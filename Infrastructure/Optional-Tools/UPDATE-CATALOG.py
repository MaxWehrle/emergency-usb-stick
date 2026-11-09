"""Optional: refresh links to personal files in a localized USB package.

The release packager fills in the three settings below. The folders themselves
remain usable without running this script or installing Python.
"""
from html import escape
from pathlib import Path
from urllib.parse import quote

PERSONAL_DIR = "My-Files"
FOLDERS = ['Photos', 'Maps', 'Documents', 'Local-Info']
EMPTY_MESSAGE = "No personal files linked yet. Open the folders directly."
START_MARKER = "<!-- PERSONAL-INDEX-START -->"
END_MARKER = "<!-- PERSONAL-INDEX-END -->"

if not FOLDERS:
    raise SystemExit("This script must be taken from a country release ZIP.")

root = Path(__file__).resolve().parents[2]
page = root / "START.html"
html = page.read_text(encoding="utf-8")
if html.count(START_MARKER) != 1 or html.count(END_MARKER) != 1:
    raise SystemExit("The media index markers are missing from START.html.")

links = []
for folder in FOLDERS:
    base = root / PERSONAL_DIR / folder
    for item in sorted(base.rglob("*")):
        if item.is_file() and item.name not in {"README.txt", "HINWEIS.txt", "VORLAGE.txt", "LOCAL-INFO-TEMPLATE.txt"}:
            rel = item.relative_to(root).as_posix()
            links.append(f'<a href="{quote(rel, safe="/")}">{escape(rel)}</a>')

middle = "".join(links) if links else f'<p class="muted">{escape(EMPTY_MESSAGE)}</p>'
start = html.index(START_MARKER) + len(START_MARKER)
end = html.index(END_MARKER)
page.write_text(html[:start] + middle + html[end:], encoding="utf-8", newline="\n")
print(f"Updated START.html with {len(links)} personal file links.")
