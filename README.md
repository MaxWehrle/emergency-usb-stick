# Wartung / Maintenance

Dieser Branch enthält die öffentlichen Prüfabläufe und kopierbaren Prompts für den [Emergency USB Stick](https://github.com/MaxWehrle/emergency-usb-stick). Hier liegen keine persönlichen Daten oder Zugangsdaten.

- [Wartungsabläufe](maintenance/WORKFLOWS.md): Quellen, Hardware, Regionalisierung, Sicherheit, technische Übernahme, Release und Nutzerkorrekturen.
- [Kopierbare Prompts](maintenance/PROMPTS.md) und [Prüfvorlagen](maintenance/CHECKLISTS.md).
- `python maintenance/audit.py --country <Pfad-zum-Länderbranch-oder-ZIP>` prüft Struktur, Sprache, PDF/TXT, Quellenverweise, lokale Links, Prüfsummen und offensichtliche Datenschutzfehler. `--check-links` ergänzt eine unverbindliche HTTP-Erreichbarkeitsprüfung.

Die Nutzerpakete liegen auf [`country/DE`](https://github.com/MaxWehrle/emergency-usb-stick/tree/country/DE) und [`country/US`](https://github.com/MaxWehrle/emergency-usb-stick/tree/country/US). Direkte ZIP-Downloads stehen auf [`main`](https://github.com/MaxWehrle/emergency-usb-stick#paket-auswählen--choose-a-package). Dort stehen auch die jeweils aktuellen Release-Hashes.

Die technische Prüfung ersetzt keine fachliche Freigabe für Medizin, Sicherheit oder regionales Recht. Nicht bestätigte Angaben bleiben außerhalb eines veröffentlichten Pakets.
