"""Build a country package from local JSON and CSS/JS, without dependencies or network."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json
import re

ROOT = Path(__file__).resolve().parents[1]
site = json.loads((ROOT / 'content/site.json').read_text(encoding='utf-8'))
cards = []
for path in sorted((ROOT / 'content').glob('*.json')):
    if path.name == 'site.json':
        continue
    card = json.loads(path.read_text(encoding='utf-8'))
    required = {'slug', 'title', 'summary', 'steps', 'source_ids', 'reviewed', 'volatility'}
    if not required <= card.keys() or not card['steps'] or not re.fullmatch(r'[a-z0-9-]+', card['slug']):
        raise ValueError(f'Invalid card: {path}')
    cards.append(card)
if len(cards) < 9:
    raise SystemExit('At least nine country cards are required')

def e(value):
    return escape(str(value), quote=True)

guides = ROOT / 'guides'
guides.mkdir(exist_ok=True)
for card in cards:
    lines = [f"# {card['title']}", '', card['summary'], '', f"## {site['guide']['steps']}", '']
    lines += [f'{i}. {step}' for i, step in enumerate(card['steps'], 1)]
    lines += ['', f"{site['guide']['reviewed']}: {card['reviewed']} · {card['volatility']}",
              f"{site['guide']['sources']}: {', '.join(card['source_ids'])}",
              site['guide']['details'], '']
    with (guides / f"{card['slug']}.md").open('w', encoding='utf-8', newline='\n') as out:
        out.write('\n'.join(lines))

def render_card(card):
    steps = ''.join(f'<li>{e(x)}</li>' for x in card['steps'])
    volatile = card['volatility'] == 'time-sensitive'
    label = site['card']['time'] if volatile else site['card']['stable']
    cls = 'time' if volatile else ''
    return (f'<article class="card" data-card><div class="meta"><span class="tag {cls}">{e(label)}</span> · {e(site["card"]["reviewed"])} {e(card["reviewed"])}</div>'
            f'<h3>{e(card["title"])}</h3><p>{e(card["summary"])}</p><ol>{steps}</ol>'
            f'<footer><a href="guides/{quote(card["slug"])}.md">{e(site["card"]["file"])}</a>'
            f'<span>{e(site["card"]["sources"])}: {e(", ".join(card["source_ids"]))}</span></footer></article>')

media_links = []
folder_links = []
for folder in site['folders']:
    name = folder['path']
    if not re.fullmatch(r'[A-Za-z0-9-]+', name):
        raise ValueError(f'Invalid folder name: {name}')
    base = ROOT / 'personal' / name
    folder_links.append(f'<a href="personal/{quote(name)}/README.txt">{e(folder["label"])}</a>')
    for path in sorted(base.rglob('*')):
        if path.is_file() and path.name != 'README.txt':
            rel = path.relative_to(ROOT).as_posix()
            media_links.append(f'<a href="{quote(rel, safe="/")}">{e(rel)}</a>')

css = (ROOT / 'assets/style.css').read_text(encoding='utf-8')
js = (ROOT / 'assets/app.js').read_text(encoding='utf-8')
intro_path = ROOT / 'content/quickstart.html'
intro = intro_path.read_text(encoding='utf-8') if intro_path.is_file() else ''
orient = ''.join(f'<div class="step"><b>{i}</b><h3>{e(item["title"])}</h3><p>{e(item["text"])}</p></div>'
                 for i, item in enumerate(site['orientation']['steps'], 1))
hero_title = e(site['hero']['title']).replace('\n', '<br>')
page = f'''<!doctype html><html lang="{e(site['locale'])}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(site['title'])}</title><style>{css}</style></head><body>
<a href="#inhalt" class="small" style="position:absolute;left:-9999px" onfocus="this.style.left='8px'" onblur="this.style.left='-9999px'">{e(site['skip'])}</a>
<header class="top"><div class="wrap"><div class="brand">✚ {e(site['brand'])} <span class="small" style="color:#c5ded8">{e(site['country_code'])} · {e(site['locale'])}</span></div><nav aria-label="{e(site['nav']['label'])}"><a href="#sofort">{e(site['nav']['quick'])}</a><a href="#lagen">{e(site['nav']['cards'])}</a><a href="#eigenes">{e(site['nav']['personal'])}</a><a href="#quellen">{e(site['nav']['sources'])}</a></nav></div></header>
<main id="inhalt"><section class="hero"><div class="wrap hero-grid"><div><div class="eyebrow">{e(site['hero']['eyebrow'])}</div><h1>{hero_title}</h1><p class="lead">{e(site['hero']['lead'])}</p><div class="actions"><a class="button" href="#sofort">{e(site['hero']['primary'])}</a><a class="button alt" href="#lagen">{e(site['hero']['secondary'])}</a></div></div><aside class="notice"><strong>{e(site['alert']['title'])}</strong><p>{e(site['alert']['text'])}</p><span class="small">{e(site['alert']['source'])}</span></aside></div></section>
{intro}
<section id="sofort" class="section"><div class="wrap"><div class="section-head"><div><div class="eyebrow">{e(site['orientation']['eyebrow'])}</div><h2>{e(site['orientation']['title'])}</h2></div><p class="small">{e(site['orientation']['note'])}</p></div><div class="steps">{orient}</div></div></section>
<section id="lagen" class="section alt"><div class="wrap"><div class="eyebrow">{e(site['cards']['eyebrow'])}</div><h2>{e(site['cards']['title'])}</h2><label for="search">{e(site['cards']['label'])}</label><input id="search" class="search" type="search" placeholder="{e(site['cards']['placeholder'])}" autocomplete="off"><p id="count" class="small" role="status" aria-live="polite" data-available="{e(site['cards']['available'])}" data-found="{e(site['cards']['found'])}"></p><div class="grid">{''.join(map(render_card,cards))}</div></div></section>
<section id="eigenes" class="section"><div class="wrap"><div class="eyebrow">{e(site['personal']['eyebrow'])}</div><h2>{e(site['personal']['title'])}</h2><div class="columns"><div class="panel"><h3>{e(site['personal']['media_title'])}</h3><p>{e(site['personal']['media_text'])}</p><div class="files">{''.join(folder_links)}</div><p class="small" style="margin-top:15px">{e(site['personal']['rebuild'])}</p></div><div class="panel"><h3>{e(site['personal']['private_title'])}</h3><p>{e(site['personal']['private_text'])}</p><a href="private/README.txt">{e(site['personal']['private_link'])}</a><p class="small" style="margin-top:15px">{e(site['personal']['private_note'])}</p></div></div><h3 style="margin-top:25px">{e(site['personal']['indexed_title'])}</h3><div class="files">{''.join(media_links) or '<p class="muted">'+e(site['personal']['empty'])+'</p>'}</div></div></section>
<section id="quellen" class="section alt"><div class="wrap"><div class="eyebrow">{e(site['sources']['eyebrow'])}</div><h2>{e(site['sources']['title'])}</h2><div class="columns"><div class="panel"><p>{e(site['sources']['description'])}</p><a href="SOURCES.md">{e(site['sources']['link'])}</a></div><div class="panel"><p>{e(site['sources']['current'])}</p><a href="STARTERGUIDE.md">{e(site['sources']['starter'])}</a></div></div></div></section></main>
<footer class="footer"><div class="wrap">{e(site['footer'])} · <a href="LICENSE">MIT</a></div></footer><script>{js}</script></body></html>'''
with (ROOT / 'START.html').open('w', encoding='utf-8', newline='\n') as out:
    out.write(page)
print(f'Built {len(cards)} guides and START.html; indexed {len(media_links)} personal files.')
