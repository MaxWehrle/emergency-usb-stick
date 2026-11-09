"""Create a deterministic, localized USB ZIP from a checked country branch.

Only explicitly mapped public files are included. Personal and private user
files are never copied into a release.
"""
from hashlib import sha256
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo
import json
import re

root = Path(__file__).resolve().parents[1]
user_root = root.parent if root.name in {"Infrastruktur", "Infrastructure"} else root
cfg = json.loads((root / "content/package.json").read_text(encoding="utf-8"))

required = ("release", "pdf", "txt", "readme", "starter", "sources", "license",
            "guides", "personal", "private", "illustrations", "tools",
            "catalog_script", "manifest", "connector_source", "connector_name",
            "folders", "folder_readme", "empty_message")
missing = [key for key in required if key not in cfg]
if missing:
    raise SystemExit(f"Missing package settings: {missing}")

def safe_rel(value):
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not value or "\\" in value:
        raise ValueError(f"Unsafe package path: {value}")
    return value

files = {}
replacements = {}

def add(src, dst, *, text=True):
    safe_rel(src)
    safe_rel(dst)
    path = root / src
    if not path.is_file():
        raise SystemExit(f"Missing release input: {src}")
    if dst in files:
        raise ValueError(f"Duplicate package path: {dst}")
    files[dst] = (path.read_bytes(), text)
    if src != dst:
        replacements[src] = dst

for src, key in (("README.md", "readme"), ("STARTERGUIDE.md", "starter"),
                 ("SOURCES.md", "sources"), ("LICENSE", "license")):
    add(src, cfg[key])
add("START.html", "START.html")
add(cfg["pdf"], cfg["pdf"], text=False)
add(cfg["txt"], cfg["txt"])
add(cfg["connector_source"], f'{cfg["illustrations"]}/{cfg["connector_name"]}')
add("private/README.txt", f'{cfg["private"]}/{cfg["folder_readme"]}')

for source_folder, target_folder in cfg["folders"].items():
    add(f"personal/{source_folder}/README.txt",
        f'{cfg["personal"]}/{target_folder}/{cfg["folder_readme"]}')

for extra in cfg.get("extra_files", []):
    add(extra["source"], extra["dest"])

for guide in sorted((root / "guides").glob("*.md")):
    add(guide.relative_to(root).as_posix(), f'{cfg["guides"]}/{guide.stem}.txt')
if len(list((root / "guides").glob("*.md"))) < 9:
    raise SystemExit("At least nine situation guides are required")

replacements.update({
    "guides/": cfg["guides"] + "/",
    "personal/": cfg["personal"] + "/",
    "private/": cfg["private"] + "/",
    "tools/build.py": f'{cfg["tools"]}/{cfg["catalog_script"]}',
    "`guides`": f'`{cfg["guides"]}`',
    "`personal`": f'`{cfg["personal"]}`',
    "`private`": f'`{cfg["private"]}`',
    ">guides<": f'>{cfg["guides"]}<',
    ">personal<": f'>{cfg["personal"]}<',
})

catalog = (root / "tools/catalog.py").read_text(encoding="utf-8")
catalog = catalog.replace("__PERSONAL_DIR__", cfg["personal"])
catalog = catalog.replace("FOLDERS = []", f'FOLDERS = {list(cfg["folders"].values())!r}')
catalog = catalog.replace("__EMPTY_MESSAGE__", cfg["empty_message"])
catalog_path = f'{cfg["tools"]}/{cfg["catalog_script"]}'
files[catalog_path] = (catalog.encode("utf-8"), True)

if cfg.get("source_code"):
    for subdir in ("assets", "content", "tools", "tests"):
        for path in sorted((root / subdir).rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                rel = path.relative_to(root).as_posix()
                dest = safe_rel(f'{cfg["source_code"]}/{rel}')
                files[dest] = (path.read_bytes().replace(b"\r\n", b"\n"), False)

def canonical(data):
    return data.replace(b"\r\n", b"\n")

output = {}
for dst, (data, is_text) in files.items():
    if is_text:
        content = canonical(data).decode("utf-8")
        for before, after in sorted(replacements.items(), key=lambda pair: len(pair[0]), reverse=True):
            content = content.replace(before, after)
        if dst.startswith(cfg["guides"] + "/") and dst.endswith(".txt"):
            content = re.sub(r"(?m)^#{1,3} ", "", content).replace("**", "")
        data = content.encode("utf-8")
    output[dst] = data

for dst in list(output):
    if dst == cfg["starter"]:
        text = output[dst].decode("utf-8")
        asset = f'{cfg["illustrations"]}/{cfg["connector_name"]}'
        text = text.replace(asset, f'Bilder/{cfg["connector_name"]}')
        output[dst] = text.encode("utf-8")

start_html = output["START.html"].decode("utf-8")
if start_html.count("<!-- PERSONAL-INDEX-START -->") != 1 or start_html.count("<!-- PERSONAL-INDEX-END -->") != 1:
    raise SystemExit("START.html is missing catalogue markers; rebuild first")

manifest = "\n".join(f"{sha256(output[name]).hexdigest()}  {name}"
                     for name in sorted(output)) + "\n"
output[cfg["manifest"]] = manifest.encode("utf-8")

release = root / "dist" / cfg["release"]
release.parent.mkdir(exist_ok=True)
with ZipFile(release, "w", ZIP_DEFLATED) as archive:
    for name in sorted(output):
        info = ZipInfo(name, date_time=(2026, 11, 9, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        archive.writestr(info, output[name])
for name, data in output.items():
    target = user_root / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
print(f"{release} SHA-256 {sha256(release.read_bytes()).hexdigest()}")
