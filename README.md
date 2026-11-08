# Notfall-USB-Stick · offene Vorlage

Ein einfacher Offline-Ordner mit Lagekarten, Quellen und Platz für eigene Dateien. Er läuft ohne Installation und ohne Internet im Browser; alle Inhalte bleiben zusätzlich als normale Dateien zugänglich.

## Deutschland: in fünf Schritten

1. [Deutsches Paket als ZIP herunterladen](https://raw.githubusercontent.com/MaxWehrle/emergency-usb-stick/main/releases/DE-2026.11.09-r1.zip) und entpacken.
2. **Den Inhalt des entpackten Ordners** auf einen leeren USB-Stick kopieren, sodass `START.html` direkt auf dem Stick liegt.
3. `START.html` doppelklicken. Unter Android den Stick im Dateimanager öffnen und `START.html` mit einem Browser öffnen; Dateimanager und Browser können sich je nach Gerät unterscheiden.
4. Eigene Fotos, Karten und Dokumente in `personal/` ergänzen. Sensible Dateien nur nach der Anleitung in `private/README.txt` verschlüsseln. Die Ordner funktionieren auch ohne Katalog.
5. Stick auswerfen, offline erneut öffnen und mindestens eine Datei probeweise zurückkopieren. Eine zweite Kopie getrennt aufbewahren.

[Deutschland (`de-DE`) ansehen](https://github.com/MaxWehrle/emergency-usb-stick/tree/country/DE) · [Starterguide](https://github.com/MaxWehrle/emergency-usb-stick/blob/country/DE/STARTERGUIDE.md) · [Quellen](https://github.com/MaxWehrle/emergency-usb-stick/blob/country/DE/SOURCES.md) · [Wartungs-Prompts](https://github.com/MaxWehrle/emergency-usb-stick/blob/maintenance/maintenance/PROMPTS.md)

> Ein digitaler Notfallordner ersetzt weder aktuelle behördliche Warnungen noch Originaldokumente. Bei akuter Gefahr gelten die Anweisungen der örtlichen Einsatzkräfte.

## Verfügbare Fassungen

| Land | Sprache | Stand | Download |
|---|---|---|---|
| Deutschland | de-DE | 09.11.2026, erste recherchierte Fassung | [Paket-ZIP direkt herunterladen](https://raw.githubusercontent.com/MaxWehrle/emergency-usb-stick/main/releases/DE-2026.11.09-r1.zip) · [Datei im Repository](releases/DE-2026.11.09-r1.zip) |

Weitere Länder erscheinen erst nach Übersetzung **und** eigener regionaler Quellenprüfung. Sprache und Land sind getrennte Angaben.

## Aufbau und Releases

- `main`: gemeinsame Technik, Projektstart, Beiträge und Lizenz.
- `country/DE`: vollständiges deutsches USB-Paket. Weitere Länder: `country/FR`, `country/GB` usw. Sprachvarianten tragen BCP-47-Tags wie `de-DE`.
- `maintenance`: Prüfabläufe, Vorlagen und Prompts ohne private Daten.

Gemeinsame technische Änderungen werden auf `main` geprüft und per selektivem `git cherry-pick` oder gezieltem Dateiabgleich in Länder-Branches übernommen. Dateien unter `content/`, `guides/`, `SOURCES.md` und `STARTERGUIDE.md` sind regional und werden dabei nicht automatisch überschrieben. Nach dem Abgleich `python tools/build.py` und `python tools/verify.py` ausführen und die erzeugte Oberfläche prüfen. Länder-Releases heißen `DE-YYYY.MM.DD-rN`; das Release-ZIP enthält den **Inhalt** des Länder-Branches und wird vor Veröffentlichung gegen dessen Commit-Prüfsummen geprüft. Das lokale Paket `DE-2026.11.09-r1.zip` hat SHA-256 `7edd978b920b32f1df9d6ee0fc5bd23b3cb0abcb8b29771816455dfa8259ce4a`.

GitHub Actions mit `schedule` laufen nur vom Default-Branch. Deshalb liegt der technische Prüfauslöser auf `main`; fachliche und regionale Prüfabläufe stehen in `maintenance` und werden nicht durch einen automatischen grünen Haken ersetzt. `workflow_dispatch` wird ebenfalls auf `main` gehalten, damit es leicht auffindbar ist.

## Lizenz

Eigene Software und Texte: MIT, siehe [LICENSE](LICENSE). Verlinkte Inhalte Dritter bleiben bei deren Rechteinhabern und sind nicht Teil dieser Lizenz. Es werden keine fremden PDFs oder privaten Medien mitgeliefert.
