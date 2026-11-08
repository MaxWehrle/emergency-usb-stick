# Wartungsabläufe

Jeder Lauf erhält einen öffentlichen Prüfvermerk mit **Datum, Land, Sprachvariante, Branch-Commit, Primärquelle, Prüfer, Entscheidung und offenen Punkten**. Personenbezogene Meldungsdetails werden vorher entfernt. Bei Konflikten gilt die aktuelle Anweisung der zuständigen lokalen Stelle; die Vorlage selbst wird erst nach belegter Prüfung geändert.

## 1. Quellen, Warnungen, Nummern, Links und Empfehlungen

**Eingaben:** Länder-Branch, `SOURCES.md`, `content/*.json`, letzte Prüfvermerke, zuständige Behörden und Primärquellen.

**Schritte:** `python maintenance/audit.py --country <Pfad> --check-links` ausführen. Jede als `zeitkritisch` markierte Karte gegen aktuelle Originalseite und zuständige regionale Stelle lesen. Nummern durch die zuständige nationale Regulierungs- oder Notrufstelle bestätigen. Publikationsdatum, Abrufdatum und URL in `SOURCES.md` nachführen. Bei Änderungen Karten und generierte Texte mit `python tools/build.py` aktualisieren.

**Prüfkriterien:** Jede sicherheitsrelevante Aussage hat eine belastbare Primärquelle; Nummern, Warnkanäle, Gebiet und Sprache passen zum Land. Links funktionieren oder sind mit Ersatzquelle dokumentiert. Aussage und Quelle widersprechen sich nicht.

**Ergebnis:** Prüfprotokoll, konkrete Dateidiffs und Liste weiter offener Punkte. Reine Erreichbarkeit einer URL ist keine inhaltliche Freigabe.

**Unbestätigt:** Nicht veröffentlichen; bestehende Aussage bei möglicher Gefahr entfernen oder mit klarer Einschränkung versehen und fachliche Prüfung anfordern. Keine vermuteten Nummern oder Handlungsanweisungen einsetzen.

## 2. Hardware und Bezugsquellen

**Eingaben:** Region, Nutzungsgeräte, benötigte Kapazität, bisherige Beispiele, Herstellerdatenblatt und Händlerseiten.

**Schritte:** Kapazitätsrechnung kontrollieren. Anschluss, Dateisystem-Hinweise, Herstellerangaben, Gesamtpreis und Verfügbarkeit auf Händlerseiten mit Abrufdatum erfassen. Affiliate-Parameter aus URLs entfernen. Nur selbst durchgeführte Windows-/Android-Gerätetests als solche nennen. Kaufbeispiele im `STARTERGUIDE.md` aktualisieren.

**Prüfkriterien:** Produktmodell und Speichervariante eindeutig; Händler für Zielregion erreichbar; Preis als Momentaufnahme gekennzeichnet; kein unbelegtes Haltbarkeits- oder Kompatibilitätsversprechen.

**Ergebnis:** Datierte Tabelle mit Produkt, Markt, Händler-URL, beobachtetem Preis, Herstellerbeleg und Teststatus.

**Unbestätigt:** Preis oder Verfügbarkeit weglassen und Status „nicht geprüft“ nennen; Produkt nicht als kompatibel bezeichnen.

## 3. Neues Land und Sprachvariante

**Eingaben:** ISO-Ländercode, BCP-47-Sprachcode, lokale Fachprüfer, amtliche Quellen, technische Basis von `main`.

**Schritte:** `country/<LAND>` vom aktuellen `main` anlegen. Alle Lagekarten fachlich neu regionalisieren: Notruf, Warnsystem, Wasser, Klima, Behörden, Recht und Bezugsquellen. Übersetzen, leichte Sprache prüfen, lokale Quellen mit Datum und Rechtebasis in `SOURCES.md` erfassen. `START.html` erzeugen und Offline-/Gerätetests durchführen. Regionale Prüfung im PR protokollieren.

**Prüfkriterien:** Land und Sprache explizit; keine ungeprüft übernommenen DE-Nummern, Gesetze oder Behörden; alle Quellen lizenziert oder nur verlinkt; mindestens neun relevante Karten und lokale Tests.

**Ergebnis:** neuer Länder-Branch erst nach vollständig dokumentierter regionaler Freigabe, dazu ZIP und README-Eintrag.

**Unbestätigt:** Branch nicht als verfügbar listen oder veröffentlichen. Eine reine Übersetzung bleibt Entwurf.

## 4. Sicherheit und Datenschutz

**Eingaben:** gesamter Branch und Historie, ZIP, `.gitignore`, `personal/`, `private/`, Abhängigkeiten.

**Schritte:** `python tools/verify.py`, `python maintenance/audit.py --country <Pfad>` und `git diff --check` ausführen. Mit `git ls-files` sowie `git log --all --name-only` Dateien und Historie auf Medien, PII, Schlüssel und Zugangsdaten prüfen. ZIP-Inhaltsliste kontrollieren. Verschlüsselungsanleitung gegen aktuelle Herstellerdokumentation prüfen; echte Wiederherstellung mit **synthetischer** Testdatei auf verfügbaren Geräten durchführen.

**Prüfkriterien:** keine privaten Daten oder fremden Medien im Repo/ZIP oder in der Historie; keine Passwortbeispiele als echte Geheimnisse; nur belegte Aussagen zur Verschlüsselung. Die `.gitignore` ist zusätzliche Sperre, kein Ersatz für Sichtprüfung.

**Ergebnis:** datierter Sicherheitsvermerk mit geprüften Commits, ZIP-Hash, Funden und Maßnahmen.

**Unbestätigt:** Veröffentlichung stoppen. Bei versehentlich veröffentlichten Geheimnissen Rotation und fachgerechte Bereinigung der Historie veranlassen; ein normaler Lösch-Commit allein reicht nicht.

## 5. Gemeinsame Änderungen in Länder-Branches

**Eingaben:** `main`-Commit, Zielland-Commit, betroffene technische Dateien, regionale Prüfstände.

**Schritte:** `git diff main...country/DE -- assets tools .github` und PR-Diff prüfen. Technischen Commit gezielt per `git cherry-pick <SHA>` übernehmen oder betroffene **technische Dateien** abgleichen. Regionale Dateien unter `content/`, `guides/`, `SOURCES.md`, `STARTERGUIDE.md` nicht pauschal überschreiben. `python tools/build.py`, `python tools/package.py`, `python tools/verify.py`, `python tests/check_offline.py` und `node tests/search.js` im Zielland laufen lassen.

**Prüfkriterien:** technische Funktion gleich, regionale Aussagen unverändert oder erneut fachlich geprüft; generierte Dateien synchron; Tests und Hashes aktualisiert.

**Ergebnis:** PR mit Herkunfts-Commit, Konfliktentscheidungen und Testprotokoll.

**Unbestätigt:** Änderung zurückhalten und Konflikt mit Länderprüfer klären; kein automatisches Überschreiben der regionalen Inhalte.

## 6. Release und Qualität

**Eingaben:** freigegebener Länder-Commit, Quellen- und Sicherheitsvermerke, Geräte-Testmatrix.

**Schritte:** Bauen (`python tools/build.py`), Paket erstellen (`python tools/package.py`), automatisierte Checks und Browser-/Gerätetest durchführen. `MANIFEST.sha256` und ZIP-SHA-256 protokollieren. Vor Veröffentlichung ZIP in leerem Ordner entpacken und `START.html`, Suche, Textdateien, Medienordner und Rückkopieren prüfen. Tag `DE-YYYY.MM.DD-rN` setzen und das ZIP als Release-Asset bereitstellen; README-Downloadlink prüfen.

**Prüfkriterien:** keine unerlaubten Drittinhalte, sichtbare Quellen- und Prüfstände, funktionierende lokale Links, responsive Ansicht, dokumentierte nicht durchführbare Tests. Fachlich geeignete menschliche Prüfung für Medizin, Sicherheit und regionales Recht liegt vor.

**Ergebnis:** Release mit Downloadlink, Commit, Prüfsummen und Changelog.

**Unbestätigt:** Kein Release. Im Entwurf offen ausweisen; ein bestandener CI-Lauf ist keine fachliche Freigabe.

## 7. Nutzerhinweise und Korrekturen

**Eingaben:** GitHub-Issue oder Meldung ohne private Angaben, betroffene Karte, Land und Sprache.

**Schritte:** Eingang bestätigen und private Daten aus öffentlichen Zitaten entfernen. Problem reproduzieren, Auswirkung priorisieren, Primärquelle prüfen. Bei akuter Gefahr eine klar bezeichnete vorläufige Warnung im README/Issue erwägen; konkrete Karte erst nach Prüfung ändern. PR, Tests und Rückmeldung an die meldende Person erstellen.

**Prüfkriterien:** Reproduktion oder Beleg, regionale Zuständigkeit, Quellenqualität, Datenschutz und Regressionstest.

**Ergebnis:** geschlossener Hinweis mit verlinktem PR oder begründeter Entscheidung; Prüfdatum im Quellenverzeichnis aktualisiert.

**Unbestätigt:** Als offen markieren, zusätzliche Quelle oder Fachprüfung anfordern. Keine Gerüchte als Anleitung übernehmen.
