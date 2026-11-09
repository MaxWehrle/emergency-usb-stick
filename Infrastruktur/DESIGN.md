# Design- und Architekturplan · Notfall-Stick

Stand: 09.11.2026. Dieser Plan gilt für die deutschen und US-amerikanischen Länderpakete. Er dokumentiert die Entwurfsgrundlage; er ist **kein** Nachweis, dass jede Person oder jedes Gerät das Paket erfolgreich bedienen kann. Dafür sind echte Nutzungs- und Gerätetests erforderlich.

## Nutzeraufgaben

1. Ein Paket herunterladen, entpacken, auf einen Stick kopieren und ohne Internet öffnen.
2. Bei Bedarf eine relevante Situation schnell finden und eine konkrete nächste Handlung lesen.
3. Eigene Dateien ergänzen, direkt über den Dateimanager finden und zurückkopieren.
4. Den Stand und die Grenzen der Offline-Hinweise erkennen und aktuelle amtliche Meldungen vorziehen.

## Beobachtung und Entscheidung

| Beobachtung / Quelle | Umsetzung | Prüfung |
|---|---|---|
| Die [CDC Clear Communication Index](https://www.cdc.gov/ccindex/tool/how-to-use.html) fordert eine erkennbare Hauptaussage und Handlung zu Beginn; der Index beruht auf Kommunikationsforschung. | Startseite zeigt zuerst Notrufhinweis, Offline-Grenze und Suche. | Sichtprüfung der ersten Bildschirmhöhe und Textprüfung. |
| Der [GOV.UK Service Manual zur Krisengestaltung](https://www.gov.uk/service-manual/agile-delivery/making-services-in-an-emergency) weist auf eingeschränktes Verstehen unter Stress hin und empfiehlt kurze Sätze, wenige Links und sichtbare Aktualität. | Keine lange Werbe-Hero-Sektion. Karten zeigen zunächst Thema und Kurzbeschreibung; Details werden auf Wunsch geöffnet. Jede Karte trägt ein Prüfdatum. | Text- und Linkprüfung; Nutzertest ausstehend. |
| [WCAG 2.2 Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) beschreibt Nutzung bei einer Breite von 320 CSS-Pixeln ohne horizontales Scrollen; [WCAG 2.2 Zielgröße](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum) nennt mindestens 24 × 24 CSS-Pixel für Zeigerziele. | Eine Spalte auf schmalen Ansichten, große Such- und Linkflächen, klarer Tastaturfokus, skalierbare Schrift. | Browserprüfung bei 320 px und 200/400 % Zoom; Gerätetest ausstehend. |
| Eine [experimentelle Studie zu Gefahrenmeldungen](https://www.sciencedirect.com/science/article/pii/S2212420922001364) fand bessere Verständlichkeit für zeit- und handlungsbezogene Hinweise. Die untersuchten Warnungen sind nicht mit einem statischen Offline-Guide gleichzusetzen. | Jede Karte beginnt mit Handlungsschritten. Aktuelle Orts- und Zeitangaben werden nicht vorgetäuscht; stattdessen steht sichtbar, dass örtliche Warnungen Vorrang haben. | Fachliche Quellenprüfung jeder Länderkarte. |
| [GOV.UK zum Schreiben für Benutzeroberflächen](https://www.gov.uk/service-manual/design/writing-for-user-interfaces) empfiehlt Namen aus der Sprache der Nutzer und geringe kognitive Last. | Deutsche Ordner heißen `Anleitungen`, `Eigene-Dateien`, `Vertrauliche-Dateien`; US-Ordner `Guides`, `My-Files`, `Private-Files`. Technische Quellen liegen in einem einzigen Infrastrukturordner. | ZIP-Inhaltsprüfung pro Land. |

## Dateiarchitektur

Im Root des entpackten Pakets liegen `START.html`, eine länderspezifische `00-LIESMICH...pdf`/`00-READ-ME...pdf`, dieselbe Anleitung als `.txt`, `README.md` für GitHub sowie die für Nutzer wichtigen Ordner. `Infrastruktur` bzw. `Infrastructure` bündelt Quellen, Lizenz, Projektunterlagen und Code. Die PDF erklärt auch, was zu tun ist, wenn lokale HTML-Dateien auf einem Gerät nicht geöffnet werden.

Die Lagekarten sind als `.txt` direkt zugänglich; HTML und Suche ergänzen diesen Weg. Die Suche läuft ohne externe Bibliotheken. Ohne JavaScript bleiben alle Themen sichtbar. Neue eigene Dateien liegen auch ohne Indexprogramm in ihren Ordnern. Vertrauliche Dateien werden **nicht** mitgeliefert.

## Sprache, Sicherheit und Aktualität

Land und Sprache werden getrennt ausgewiesen (`DE`/`de-DE`, `US`/`en-US`). Notrufnummern, Behörden, Wasserhinweise und regionale Risiken werden nicht aus einer anderen Länderfassung übernommen. Die US-Ausgabe bietet eine nationale Grundlage und eine leere lokale Vorlage; sie ersetzt keine aktuelle Regel für Bundesstaat, Tribal Nation, Territorium, County oder Stadt.

Die Oberfläche hat keine Live-Warnfunktion. Hinweise zu Warnungen, Medizin, Evakuierung oder lokalen Diensten benötigen wiederkehrende Quellenprüfung und vor Veröffentlichung nachvollziehbare fachliche Kontrolle. Farbe allein trägt keine Anweisung. PDF und TXT enthalten dieselben Nutzungsschritte.

## Abnahme und offene Evidenz

- Automatisiert: ZIP ohne technische Root-Ordner, interne Links, PDF/TXT, Textkarten, Suche, Katalog-Neuaufbau, Prüfsummen und Datenschutz-Scan.
- Visuell: 320 px, breiter Bildschirm, Zoom, Druckansicht, PDF-Rendering und Kontrast.
- Mit Menschen: mindestens mehrere Personen mit unterschiedlicher Erfahrung und Altersspanne sollen ohne Hilfe die vier Nutzeraufgaben ausführen. Fehler, Suchbegriffe und Dauer dokumentieren; Texte anschließend überarbeiten.
- Mit Geräten: Windows-Datei-Explorer und verschiedene Android-Dateimanager/Browser sowie tatsächliche USB-C-Adapter testen. Keine allgemeine Kompatibilität aus einem Einzeltest ableiten.

Bis solche Tests vorliegen, bleibt „für alle intuitiv“ ein **Gestaltungsziel**, keine belegte Eigenschaft.
