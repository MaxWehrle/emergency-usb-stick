# Wartung · öffentlicher Branch `maintenance`

Dieser Branch enthält Arbeitsanleitungen und kopierbare Prompts. Er enthält keine persönlichen Daten, Zugangsdaten oder unveröffentlichten Hinweise von Betroffenen.

## Schnellstart

1. Aktuellen Länder-Branch in einem **separaten Arbeitsverzeichnis** auschecken, zum Beispiel `git worktree add ../emergency-de country/DE`.
2. `python maintenance/audit.py --country ../emergency-de` ausführen. Optional `--check-links` bei verfügbarem Internet. Das Skript prüft Struktur, Datumsangaben, interne Quellenkennungen, lokale Links und offensichtliche sensible Dateien. Es ersetzt keine fachliche Prüfung.
3. Den passenden Ablauf in [WORKFLOWS.md](WORKFLOWS.md) und den Prompt in [PROMPTS.md](PROMPTS.md) verwenden.
4. Ergebnisse mit Datum, Belegen, Prüfer und Entscheidung in einem öffentlichen Pull Request dokumentieren. Keine personenbezogenen Daten in Issues, Logs oder Prompts kopieren.

Alle URLs und Preise sind zeitkritisch. Ein fehlgeschlagener Linktest ist ein Prüfhinweis, keine automatische Inhaltskorrektur. Notrufnummern, Medizin, Sicherheit und regionales Recht benötigen vor Veröffentlichung eine nachvollziehbare menschliche Prüfung anhand zuständiger Primärquellen.
