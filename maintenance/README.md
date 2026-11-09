# Wartung · öffentlicher Branch `maintenance`

Dieser Branch enthält Arbeitsanleitungen und kopierbare Prompts. Er enthält keine persönlichen Daten, Zugangsdaten oder unveröffentlichten Hinweise von Betroffenen.

## Schnellstart

1. Aktuellen Länder-Branch in einem **separaten Arbeitsverzeichnis** auschecken, zum Beispiel `git worktree add ../emergency-de country/DE` oder entsprechend `country/US`.
2. `python maintenance/audit.py --country ../emergency-de` ausführen. Alternativ direkt das Release-ZIP als `--country` angeben. Optional `--check-links` bei verfügbarem Internet. Das Skript prüft Struktur, PDF/TXT, Datumsangaben, interne Quellenkennungen, lokale Links, Prüfsummen und offensichtliche sensible Dateien. Es ersetzt keine fachliche Prüfung.
3. Den passenden Ablauf in [WORKFLOWS.md](WORKFLOWS.md), die [Prüfvorlage](CHECKLISTS.md) und den Prompt in [PROMPTS.md](PROMPTS.md) verwenden.
4. Ergebnisse mit Datum, Belegen, Prüfer und Entscheidung in einem öffentlichen Pull Request dokumentieren. Keine personenbezogenen Daten in Issues, Logs oder Prompts kopieren.

Alle URLs und Preise sind zeitkritisch. Ein fehlgeschlagener Linktest ist ein Prüfhinweis, keine automatische Inhaltskorrektur. Notrufnummern, Medizin, Sicherheit und regionales Recht benötigen vor Veröffentlichung eine nachvollziehbare menschliche Prüfung anhand zuständiger Primärquellen.

Die Länderfassungen `country/DE` (`de-DE`) und `country/US` (`en-US`) enthalten eigene Quellen und Ordnernamen. `Infrastruktur/content/site.json` beziehungsweise `Infrastructure/content/site.json` beschreibt die Sprache der Oberfläche und ist **keine Lagekarte**. Der Audit berücksichtigt das. Eine nationale US-Fassung ersetzt keine Prüfung von Bundesstaat, Tribal Nation, Territorium, County oder Stadt; die lokale Vorlage bleibt unausgefüllt.
