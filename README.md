# Notfall-USB-Stick · offene Vorlage

Ein einfacher Notfall-Ordner für einen USB-Stick. Die Startseite funktioniert ohne Internet und ohne Installation. Alle Themen liegen zusätzlich als normale Textdateien bereit.

## Deutschland: in fünf Schritten

1. [Deutsches Paket herunterladen](https://raw.githubusercontent.com/MaxWehrle/emergency-usb-stick/main/releases/DE-2026.11.09-r3.zip). Es ist eine **ZIP-Datei**: eine gepackte Sammlung von Dateien.
2. Öffnen Sie auf Windows **Downloads**. Klicken Sie mit der rechten Maustaste auf die ZIP-Datei und wählen Sie **Alle extrahieren**. So holen Sie die Dateien in einen normalen Ordner.
3. Stecken Sie einen USB-Stick ein. Kopieren Sie **alles aus dem entpackten Ordner** auf den Stick. Danach muss die Datei `START.html` direkt auf dem Stick zu sehen sein.
4. Klicken Sie zweimal schnell auf `START.html`. Auf Android öffnen Sie den Stick in der App **Dateien** und tippen auf `START.html`. Wenn das nicht klappt, lesen Sie die Dateien im Ordner `guides`.
5. Ergänzen Sie eigene Dateien im Ordner `personal`. Testen Sie den Stick ohne Internet und kopieren Sie eine Datei probeweise zurück. Legen Sie eine zweite Kopie an einem anderen Ort ab.

[Anleitung mit ganz kleinen Schritten](https://github.com/MaxWehrle/emergency-usb-stick/blob/country/DE/STARTERGUIDE.md) · [Deutschland (`de-DE`) ansehen](https://github.com/MaxWehrle/emergency-usb-stick/tree/country/DE) · [Quellen](https://github.com/MaxWehrle/emergency-usb-stick/blob/country/DE/SOURCES.md) · [Wartungs-Prompts](https://github.com/MaxWehrle/emergency-usb-stick/blob/maintenance/maintenance/PROMPTS.md)

> Ein digitaler Notfallordner ersetzt weder aktuelle behördliche Warnungen noch Originaldokumente. Bei akuter Gefahr gelten die Anweisungen der örtlichen Einsatzkräfte.

## Verfügbare Fassungen

| Land | Sprache | Stand | Download |
|---|---|---|---|
| Deutschland | de-DE | 09.11.2026, einfache Anleitung, Revision 3 | [Paket-ZIP direkt herunterladen](https://raw.githubusercontent.com/MaxWehrle/emergency-usb-stick/main/releases/DE-2026.11.09-r3.zip) · [Datei im Repository](releases/DE-2026.11.09-r3.zip) |

Weitere Länder erscheinen erst nach Übersetzung **und** eigener regionaler Quellenprüfung. Sprache und Land sind getrennte Angaben.

## Aufbau und Releases

- `main`: gemeinsame Technik, Projektstart, Beiträge und Lizenz.
- `country/DE`: vollständiges deutsches USB-Paket. Weitere Länder: `country/FR`, `country/GB` usw. Sprachvarianten tragen BCP-47-Tags wie `de-DE`.
- `maintenance`: Prüfabläufe, Vorlagen und Prompts ohne private Daten.

Gemeinsame technische Änderungen werden auf `main` geprüft und per selektivem `git cherry-pick` oder gezieltem Dateiabgleich in Länder-Branches übernommen. Dateien unter `content/`, `guides/`, `SOURCES.md` und `STARTERGUIDE.md` sind regional und werden dabei nicht automatisch überschrieben. Nach dem Abgleich `python tools/build.py` und `python tools/verify.py` ausführen und die erzeugte Oberfläche prüfen. Länder-Releases heißen `DE-YYYY.MM.DD-rN`; das Release-ZIP enthält den **Inhalt** des Länder-Branches und wird vor Veröffentlichung gegen dessen Commit-Prüfsummen geprüft. Das Paket `DE-2026.11.09-r3.zip` hat SHA-256 `3167bfe75dd144f91622f54616f4215a390b32c1d6aa8db4a4f5fd159df8a738`.

GitHub Actions mit `schedule` laufen nur vom Default-Branch. Deshalb liegt der technische Prüfauslöser auf `main`; fachliche und regionale Prüfabläufe stehen in `maintenance` und werden nicht durch einen automatischen grünen Haken ersetzt. `workflow_dispatch` wird ebenfalls auf `main` gehalten, damit es leicht auffindbar ist.

## Lizenz

Eigene Software und Texte: MIT, siehe [LICENSE](LICENSE). Verlinkte Inhalte Dritter bleiben bei deren Rechteinhabern und sind nicht Teil dieser Lizenz. Es werden keine fremden PDFs oder privaten Medien mitgeliefert.
