"""Build the offline emergency page and plain guides from country content.

This code runs inside the Infrastructure/Infrastruktur source folder. The
release packager maps its links to the language-specific USB folder names.
"""
from html import escape
from pathlib import Path
from urllib.parse import quote
import json
import re

root = Path(__file__).resolve().parents[1]
site = json.loads((root / "content/site.json").read_text(encoding="utf-8"))
cards = []
for path in sorted((root / "content").glob("*.json")):
    if path.name in {"site.json", "package.json", "readme_pdf.json"}:
        continue
    card = json.loads(path.read_text(encoding="utf-8"))
    required = {"slug", "title", "summary", "steps", "source_ids", "reviewed", "volatility"}
    if not required <= card.keys() or not card["steps"] or not re.fullmatch(r"[a-z0-9-]+", card["slug"]):
        raise ValueError(f"Invalid situation card: {path}")
    cards.append(card)
if len(cards) < 9:
    raise SystemExit("At least nine reviewed situation cards are required")

def h(value):
    return escape(str(value), quote=True)

guides = root / "guides"
guides.mkdir(exist_ok=True)
for card in cards:
    lines = [f'# {card["title"]}', "", card["summary"], "", f'## {site["guide"]["heading"]}', ""]
    lines += [f"{i}. {step}" for i, step in enumerate(card["steps"], 1)]
    lines += ["", f'{site["guide"]["reviewed"]}: {card["reviewed"]}',
              f'{site["guide"]["sources"]}: {", ".join(card["source_ids"])}',
              site["guide"]["details"], ""]
    (guides / f'{card["slug"]}.md').write_text("\n".join(lines), encoding="utf-8", newline="\n")

def card_html(card):
    tag = site["card"]["time"] if card["volatility"] == "time-sensitive" else site["card"]["stable"]
    steps = "".join(f"<li>{h(step)}</li>" for step in card["steps"])
    return (
        f'<details class="card" data-card><summary><span class="card-heading">{h(card["title"])}</span>'
        f'<span class="card-summary">{h(card["summary"])}</span>'
        f'<span class="card-open"><span class="show">{h(site["card"]["show"])}</span>'
        f'<span class="hide">{h(site["card"]["hide"])}</span> <span aria-hidden="true">⌄</span></span>'
        f'</summary><div class="card-body"><p class="card-tag">{h(tag)} · {h(site["card"]["reviewed"])} {h(card["reviewed"])}</p>'
        f'<ol>{steps}</ol><p class="card-foot"><a href="guides/{quote(card["slug"])}.md">{h(site["card"]["file"])}</a>'
        f'<span>{h(site["card"]["sources"])}: {h(", ".join(card["source_ids"]))}</span></p></div></details>'
    )

folder_links = []
media_links = []
for folder in site["folders"]:
    source = folder["path"]
    if not re.fullmatch(r"[A-Za-z0-9-]+", source):
        raise ValueError(f"Invalid personal folder: {source}")
    folder_links.append(f'<a class="folder-link" href="personal/{quote(source)}/README.txt">{h(folder["label"])}</a>')
    for item in sorted((root / "personal" / source).rglob("*")):
        if item.is_file() and item.name != "README.txt":
            rel = item.relative_to(root).as_posix()
            media_links.append(f'<a href="{quote(rel, safe="/")}">{h(rel)}</a>')

media = "".join(media_links) if media_links else f'<p class="muted">{h(site["personal"]["empty"])}</p>'
css = (root / "assets/style.css").read_text(encoding="utf-8")
js = (root / "assets/app.js").read_text(encoding="utf-8")
s = site
page = f'''<!doctype html>
<html lang="{h(s["locale"])}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{h(s["title"])}</title><style>{css}</style></head><body>
<a class="skip" href="#main">{h(s["skip"])}</a>
<header class="top"><div class="wrap"><div class="brand">{h(s["brand"])}</div><div class="edition">{h(s["edition"])}</div></div></header>
<main id="main">
<section class="intro"><div class="wrap"><p class="eyebrow">{h(s["eyebrow"])}</p><h1>{h(s["headline"])}</h1>
<p class="lead">{h(s["lead"])}</p>
<div class="emergency"><strong>{h(s["emergency"]["title"])}</strong><p>{h(s["emergency"]["text"])}</p><small>{h(s["emergency"]["source"])}</small></div>
<p class="offline-note">{h(s["offline_note"])}</p>
<div class="search-block"><label for="search">{h(s["search"]["label"])}</label><div class="search-row"><input id="search" type="search" autocomplete="off" placeholder="{h(s["search"]["placeholder"])}"><button id="clear-search" type="button">{h(s["search"]["clear"])}</button></div><p id="count" role="status" aria-live="polite" data-available="{h(s["search"]["available"])}" data-found="{h(s["search"]["found"])}"></p></div>
<nav class="quick-links" aria-label="{h(s["links"]["label"])}"><a href="{h(s["pdf"])}">{h(s["links"]["pdf"])}</a><a href="{h(s["txt"])}">{h(s["links"]["txt"])}</a><a href="#personal">{h(s["links"]["personal"])}</a></nav>
</div></section>
<section class="topics" aria-labelledby="topics-title"><div class="wrap"><h2 id="topics-title">{h(s["topics_title"])}</h2><div class="grid">{''.join(card_html(card) for card in cards)}</div></div></section>
<section class="section" id="personal"><div class="wrap"><h2>{h(s["personal"]["title"])}</h2><p>{h(s["personal"]["lead"])}</p><div class="folder-links">{''.join(folder_links)}</div><p class="private-link"><a href="private/README.txt">{h(s["personal"]["private"])}</a></p><h3>{h(s["personal"]["indexed"])}</h3><div class="indexed"><!-- PERSONAL-INDEX-START -->{media}<!-- PERSONAL-INDEX-END --></div><p class="small">{h(s["personal"]["rebuild"])}</p></div></section>
<section class="section sources"><div class="wrap"><h2>{h(s["sources"]["title"])}</h2><p>{h(s["sources"]["lead"])}</p><a href="SOURCES.md">{h(s["sources"]["link"])}</a></div></section>
</main><footer><div class="wrap">{h(s["footer"])} · <a href="LICENSE">MIT</a></div></footer><script>{js}</script></body></html>'''
(root / "START.html").write_text(page, encoding="utf-8", newline="\n")
print(f"Built {len(cards)} guides and START.html; indexed {len(media_links)} personal files.")
