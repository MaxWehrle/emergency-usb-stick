"""Build a self-contained offline landing page and plain-text guides from country JSON."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json

ROOT = Path(__file__).resolve().parents[1]
cards = []
for path in sorted((ROOT / 'content').glob('*.json')):
    obj = json.loads(path.read_text(encoding='utf-8'))
    required = {'slug', 'title', 'summary', 'steps', 'source_ids', 'reviewed', 'volatility'}
    if not required <= obj.keys() or not isinstance(obj['steps'], list) or not obj['steps']:
        raise ValueError(f'Incomplete card: {path}')
    cards.append(obj)
if not cards:
    raise SystemExit('No country cards in content/')

guides = ROOT / 'guides'
guides.mkdir(exist_ok=True)
for c in cards:
    lines = [f"# {c['title']}", '', c['summary'], '', '## Was jetzt hilft', '']
    lines += [f"{i}. {step}" for i, step in enumerate(c['steps'], 1)]
    lines += ['', f"Prüfstand: {c['reviewed']} · Art: {c['volatility']}",
              f"Quellenkennungen: {', '.join(c['source_ids'])}",
              'Details und Originalquellen: ../SOURCES.md', '']
    with (guides / f"{c['slug']}.md").open('w', encoding='utf-8', newline='\n') as out:
        out.write('\n'.join(lines))

def card(c):
    steps = ''.join(f'<li>{escape(x)}</li>' for x in c['steps'])
    kind = 'Häufig prüfen' if c['volatility'] == 'zeitkritisch' else 'Grundlage'
    klass = 'time' if c['volatility'] == 'zeitkritisch' else ''
    return (f'<article class="card" data-card><div class="meta"><span class="tag {klass}">{kind}</span> · geprüft {escape(c["reviewed"])}</div>'
            f'<h3>{escape(c["title"])}</h3><p>{escape(c["summary"])}</p><ol>{steps}</ol>'
            f'<footer><a href="guides/{quote(c["slug"])}.md">Als Textdatei</a>'
            f'<span>Quellen: {escape(", ".join(c["source_ids"]))}</span></footer></article>')

media = []
for folder in ('Fotos', 'Karten', 'Dokumente'):
    base = ROOT / 'personal' / folder
    for p in sorted(base.rglob('*')):
        if p.is_file() and p.name != 'README.txt':
            rel = p.relative_to(ROOT).as_posix()
            media.append(f'<a href="{quote(rel, safe="/")}">{escape(rel)}</a>')
media_html = ''.join(media) or '<p class="muted">Noch keine eigenen Dateien katalogisiert. Öffnen Sie die Ordner direkt im Dateimanager.</p>'
css = (ROOT / 'assets/style.css').read_text(encoding='utf-8')
js = (ROOT / 'assets/app.js').read_text(encoding='utf-8')
html = f'''<!doctype html><html lang="de-DE"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Notfall-USB · Deutschland</title><style>{css}</style></head><body>
<a href="#inhalt" class="small" style="position:absolute;left:-9999px" onfocus="this.style.left='8px'" onblur="this.style.left='-9999px'">Zum Inhalt springen</a>
<header class="top"><div class="wrap"><div class="brand">✚ NOTFALL-USB <span class="small" style="color:#c5ded8">DE · de-DE</span></div><nav aria-label="Hauptnavigation"><a href="#sofort">Schnelleinstieg</a><a href="#lagen">Lagekarten</a><a href="#eigenes">Eigene Dateien</a><a href="#quellen">Quellen</a></nav></div></header>
<main id="inhalt"><section class="hero"><div class="wrap hero-grid"><div><div class="eyebrow">Offline dabei · Deutschland</div><h1>Wichtige Schritte.<br>Auch ohne Netz.</h1><p class="lead">Kurze Orientierung für Krisen, mit normalen Dateien zum Weitergeben. Stand: 09.11.2026. Aktuelle Warnungen und Anweisungen vor Ort haben Vorrang.</p><div class="actions"><a class="button" href="#sofort">Jetzt beginnen</a><a class="button alt" href="#lagen">Lage finden</a></div></div><aside class="notice"><strong>Akute Gefahr?</strong><p>Eigene Sicherheit zuerst. In Deutschland: <b>112</b> für Feuerwehr und Rettungsdienst, <b>110</b> für Polizei. Wenn Netze ausfallen, örtliche Anlaufstellen beachten.</p><span class="small">Nummern und Hinweise: BBK · Prüfung 09.11.2026</span></aside></div></section>
<section id="sofort" class="section"><div class="wrap"><div class="section-head"><div><div class="eyebrow">Schnelleinstieg</div><h2>In drei Schritten orientieren</h2></div><p class="small">Dieses Paket enthält keine Live-Warnungen.</p></div><div class="steps"><div class="step"><b>1</b><h3>Gefahr erkennen</h3><p>Bringen Sie sich und andere ohne Eigengefährdung in Sicherheit. Hören Sie auf Einsatzkräfte.</p></div><div class="step"><b>2</b><h3>Hilfe und Warnungen</h3><p>Bei Notfällen 112 oder 110. Wenn möglich: amtliche Warnungen, Radio und lokale Hinweise prüfen.</p></div><div class="step"><b>3</b><h3>Lagekarte öffnen</h3><p>Suchen Sie unten nach dem Thema. Jede Karte liegt zusätzlich als Textdatei im Ordner <code>guides/</code>.</p></div></div></div></section>
<section id="lagen" class="section alt"><div class="wrap"><div class="eyebrow">Krisenguides</div><h2>Lagekarten</h2><label for="search">Thema oder Stichwort suchen</label><input id="search" class="search" type="search" placeholder="z. B. Wasser, Strom, Evakuierung" autocomplete="off"><p id="count" class="small" role="status" aria-live="polite"></p><div class="grid">{''.join(map(card,cards))}</div></div></section>
<section id="eigenes" class="section"><div class="wrap"><div class="eyebrow">Ihre Ergänzungen</div><h2>Eigene Dateien</h2><div class="columns"><div class="panel"><h3>Persönliche Medien</h3><p>Kopieren Sie eigene Dateien in diese Ordner. Die Dateien sind im Dateimanager immer direkt zugänglich.</p><div class="files"><a href="personal/Fotos/README.txt">Fotos</a><a href="personal/Karten/README.txt">Karten</a><a href="personal/Dokumente/README.txt">Dokumente</a></div><p class="small" style="margin-top:15px">Für aktualisierte Links in dieser Seite optional <code>python tools/build.py</code> ausführen. Dafür ist Python nötig; die Ordner selbst brauchen es nicht.</p></div><div class="panel"><h3>Vertrauliche Daten</h3><p>Für Ausweise, Gesundheitsdaten und andere sensible Dateien zuerst einen verschlüsselten Tresor einrichten. Passwort und Wiederherstellungsschlüssel getrennt verwahren.</p><a href="private/README.txt">Anleitung für Windows und Android</a><p class="small" style="margin-top:15px">Digitale Kopien ersetzen keine Originale. Testen Sie das Öffnen auf Ihren eigenen Geräten.</p></div></div><h3 style="margin-top:25px">Katalogisierte eigene Dateien</h3><div class="files">{media_html}</div></div></section>
<section id="quellen" class="section alt"><div class="wrap"><div class="eyebrow">Nachvollziehbar</div><h2>Quellen und Prüfstand</h2><div class="columns"><div class="panel"><p>Die Lagekarten sind eigene Kurztexte auf Basis der dokumentierten Primärquellen. Fremde PDFs sind nur verlinkt und nicht im Paket enthalten.</p><a href="SOURCES.md">Quellenverzeichnis öffnen</a></div><div class="panel"><p>Angaben zu Warnungen, Nummern, Recht, Gesundheit und Kaufbeispielen können sich ändern. Prüfen Sie bei Internetzugang den aktuellen Stand der verlinkten Stellen.</p><a href="STARTERGUIDE.md">Stick vorbereiten und testen</a></div></div></div></section></main>
<footer class="footer"><div class="wrap">Offene Vorlage · Deutschland / de-DE · <a href="LICENSE">MIT-Lizenz für eigene Texte und Software</a></div></footer><script>{js}</script></body></html>'''
with (ROOT / 'START.html').open('w', encoding='utf-8', newline='\n') as out:
    out.write(html)
print(f'Built {len(cards)} guides and START.html; indexed {len(media)} personal files.')
