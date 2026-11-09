# Emergency USB Stick · Notfall-Stick

Offline-Hinweise für den USB-Stick, ergänzt durch Platz für eigene Dateien. Die Pakete funktionieren ohne Installation und ohne Internet. Jede Länderfassung hat geprüfte regionale Inhalte; Sprache und Land sind getrennt ausgewiesen.

Offline emergency guides for a USB drive, with space for your own files. Each country package includes reviewed regional information and identifies its language separately.

## Pakete / Packages

| Land / Country | Sprache / Language | Stand / Release | Download | Quellen / Sources |
|---|---|---|---|---|
| Deutschland | de-DE | 09.11.2026 · Revision 4 | [Deutsches Paket herunterladen](https://raw.githubusercontent.com/MaxWehrle/emergency-usb-stick/main/releases/DE-2026.11.09-r4.zip) | [Deutschland](https://github.com/MaxWehrle/emergency-usb-stick/blob/country/DE/SOURCES.md) |
| United States | en-US | Nov 9, 2026 · revision 1 | [Download U.S. package](https://raw.githubusercontent.com/MaxWehrle/emergency-usb-stick/main/releases/US-2026.11.09-r1.zip) | [United States](https://github.com/MaxWehrle/emergency-usb-stick/blob/country/US/SOURCES.md) |

### Deutsch: Stick vorbereiten

1. [Deutsches Paket herunterladen](https://raw.githubusercontent.com/MaxWehrle/emergency-usb-stick/main/releases/DE-2026.11.09-r4.zip) und die ZIP-Datei entpacken.
2. Den **Inhalt des entpackten Ordners** auf einen USB-Stick kopieren. `START.html` soll direkt auf dem Stick liegen.
3. `START.html` vom Stick öffnen. Auf Android geht das über die Dateien-App; falls lokale HTML-Dateien nicht geöffnet werden, stehen alle Hinweise auch im Ordner `guides`.
4. Eigene Dateien in `personal` ergänzen. Den Stick offline testen und eine Testdatei zurück auf das Gerät kopieren. Eine zweite vollständige Kopie getrennt aufbewahren.

[Ausführlicher Starterguide für Windows und Android](https://github.com/MaxWehrle/emergency-usb-stick/blob/country/DE/STARTERGUIDE.md) · [Deutsche Fassung ansehen](https://github.com/MaxWehrle/emergency-usb-stick/tree/country/DE)

### English: prepare your drive

1. [Download the U.S. package](https://raw.githubusercontent.com/MaxWehrle/emergency-usb-stick/main/releases/US-2026.11.09-r1.zip) and extract the ZIP.
2. Copy **everything inside the extracted folder** to a USB drive. `START.html` should be directly on the drive.
3. Open `START.html` from the drive. On Android, use your Files app; if local HTML does not open, read the ordinary files in `guides`.
4. Add your own files in `personal`. Test offline and copy a test file back to your device. Keep a second complete copy elsewhere.

[Detailed Windows and Android guide](https://github.com/MaxWehrle/emergency-usb-stick/blob/country/US/STARTERGUIDE.md) · [View U.S. edition](https://github.com/MaxWehrle/emergency-usb-stick/tree/country/US)

**Bei akuter Gefahr gelten aktuelle örtliche Warnungen und Anweisungen. Digitale Kopien ersetzen keine Originaldokumente.** Current local alerts and orders take priority. Digital copies do not replace original documents.

## Branches and releases

- `main`: shared code, project entry, contribution rules, license, and published ZIPs.
- `country/DE`: Germany, `de-DE`; `country/US`: United States, `en-US`. Country branches include the complete offline package and regional sources. Add a country only after translation **and** regional review.
- `maintenance`: audit procedures, check templates, reusable agent prompts, and technical checks. [Maintenance prompts](https://github.com/MaxWehrle/emergency-usb-stick/blob/maintenance/maintenance/PROMPTS.md).

Use `country/<ISO-3166-1-alpha-2>` for country branches and BCP-47 tags for language variants. Releases use `<COUNTRY>-YYYY.MM.DD-rN`. For technical changes, review on `main`, then selectively cherry-pick or compare files into each country branch. Never automatically overwrite `content/`, `guides/`, `SOURCES.md`, `STARTERGUIDE.md`, or country folder names. Build and verify each country again after synchronization.

Release SHA-256 checksums: `DE-2026.11.09-r4.zip` = `c7f4206b86f26a6a419aedf37cf1b5d8d04aa08b4f812d5b2bb0bf9b6dcb6964`; `US-2026.11.09-r1.zip` = `6a8aab3bffa7e0b7450a1add7d6a6b6bd5adfd12ba408f9dcd73375d94e7a508`. Older releases remain in [releases](releases/).

GitHub Actions `schedule` runs from the default branch, and manual `workflow_dispatch` is kept there for visibility. Automated checks do not replace human review of safety, medical, legal, and regional claims.

Project code and original text: [MIT license](LICENSE). Linked third-party material remains with its rights holders and is not bundled. Report corrections through [GitHub issues](https://github.com/MaxWehrle/emergency-usb-stick/issues) without posting personal data. See [contribution rules](CONTRIBUTING.md).
