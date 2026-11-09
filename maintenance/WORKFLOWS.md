# Wartungsabläufe

Jeder Lauf erhält einen öffentlichen Prüfvermerk mit **Datum, Land, Sprachvariante, Branch-Commit, Primärquelle, Prüfer, Entscheidung und offenen Punkten**. Personenbezogene Meldungsdetails werden vorher entfernt. Bei Konflikten gilt die aktuelle Anweisung der zuständigen lokalen Stelle; die Vorlage selbst wird erst nach belegter Prüfung geändert.

**Aktuelle Pfade:** Das deutsche Paket nutzt `Infrastruktur`, `Anleitungen`, `Eigene-Dateien`, `Vertrauliche-Dateien` und `00-LIESMICH-DE.pdf/.txt`. Das US-Paket nutzt `Infrastructure`, `Guides`, `My-Files`, `Private-Files` und `00-READ-ME-US.pdf/.txt`. Der Quelltext liegt im jeweiligen Infrastrukturordner unter `content`, `tools`, `assets` und `guides`; im ZIP unter `Quellcode` beziehungsweise `Source-Code`. `maintenance/audit.py` akzeptiert sowohl einen Länderbranch-Ordner als auch das Release-ZIP.

## 1. Quellen, Warnungen, Nummern, Links und Empfehlungen

**Eingaben:** Länder-Branch, `Infrastruktur/QUELLEN.md` beziehungsweise `Infrastructure/SOURCES.md`, `<Infrastruktur>/content/*.json`, letzte Prüfvermerke, zuständige Behörden und Primärquellen.

**Schritte:** `python maintenance/audit.py --country <Pfad> --check-links` ausführen. Jede als zeitkritisch markierte Karte gegen die aktuelle Originalseite und zuständige regionale Stelle lesen. Nummern durch die zuständige nationale Regulierungs- oder Notrufstelle bestätigen. Publikationsdatum, Abrufdatum und URL im lokalisierten Quellenverzeichnis nachführen. Bei Änderungen Karten und generierte Texte mit `python <Infrastruktur>/tools/build.py` aktualisieren.

**Prüfkriterien:** Jede sicherheitsrelevante Aussage hat eine belastbare Primärquelle; Nummern, Warnkanäle, Gebiet und Sprache passen zum Land. Links funktionieren oder sind mit Ersatzquelle dokumentiert. Aussage und Quelle widersprechen sich nicht.

**Ergebnis:** Prüfprotokoll, konkrete Dateidiffs und Liste weiter offener Punkte. Reine Erreichbarkeit einer URL ist keine inhaltliche Freigabe.

**Unbestätigt:** Nicht veröffentlichen; bestehende Aussage bei möglicher Gefahr entfernen oder mit klarer Einschränkung versehen und fachliche Prüfung anfordern. Keine vermuteten Nummern oder Handlungsanweisungen einsetzen.

## 2. Hardware und Bezugsquellen

**Eingaben:** Region, Nutzungsgeräte, benötigte Kapazität, bisherige Beispiele, Herstellerdatenblatt und Händlerseiten.

**Schritte:** Kapazitätsrechnung kontrollieren. Anschluss, Dateisystem-Hinweise, Herstellerangaben, Gesamtpreis und Verfügbarkeit auf Händlerseiten mit Abrufdatum erfassen. Affiliate-Parameter aus URLs entfernen. Nur selbst durchgeführte Windows-/Android-Gerätetests als solche nennen. Kaufbeispiele in `Infrastruktur/ANLEITUNG.md` oder `Infrastructure/GET-STARTED.md` sowie in der sichtbaren PDF/TXT-Anleitung aktualisieren.

**Prüfkriterien:** Produktmodell und Speichervariante eindeutig; Händler für Zielregion erreichbar; Preis als Momentaufnahme gekennzeichnet; kein unbelegtes Haltbarkeits- oder Kompatibilitätsversprechen.

**Ergebnis:** Datierte Tabelle mit Produkt, Markt, Händler-URL, beobachtetem Preis, Herstellerbeleg und Teststatus.

**Unbestätigt:** Preis oder Verfügbarkeit weglassen und Status „nicht geprüft“ nennen; Produkt nicht als kompatibel bezeichnen.

## 3. Neues Land und Sprachvariante

**Eingaben:** ISO-Ländercode, BCP-47-Sprachcode, lokale Fachprüfer, amtliche Quellen, technische Basis von `main`.

**Schritte:** `country/<LAND>` vom aktuellen `main` anlegen. Alle Lagekarten fachlich neu regionalisieren: Notruf, Warnsystem, Wasser, Klima, Behörden, Recht und Bezugsquellen. Oberfläche, alle nutzerseitigen Ordner, PDF/TXT-Namen, Dateien und Vorlagen übersetzen. Lokale Quellen mit Datum und Rechtebasis im lokalisierten Quellenverzeichnis erfassen. `START.html`, PDF, TXT und ZIP erzeugen und Offline-/Gerätetests durchführen. Regionale Prüfung im PR protokollieren.

**Prüfkriterien:** Land und Sprache explizit; keine ungeprüft übernommenen DE-Nummern, Gesetze oder Behörden; alle Quellen lizenziert oder nur verlinkt; mindestens neun relevante Karten und lokale Tests.

**Ergebnis:** neuer Länder-Branch erst nach vollständig dokumentierter regionaler Freigabe, dazu ZIP und README-Eintrag.

**Unbestätigt:** Branch nicht als verfügbar listen oder veröffentlichen. Eine reine Übersetzung bleibt Entwurf.

## 4. Sicherheit und Datenschutz

**Eingaben:** gesamter Branch und Historie, ZIP, `.gitignore`, `Eigene-Dateien`/`My-Files`, `Vertrauliche-Dateien`/`Private-Files`, Abhängigkeiten.

**Schritte:** `python <Infrastruktur>/tools/verify.py`, `python maintenance/audit.py --country <Pfad-oder-ZIP>` und `git diff --check` ausführen. Mit `git ls-files` sowie `git log --all --name-only` Dateien und Historie auf Medien, PII, Schlüssel und Zugangsdaten prüfen. ZIP-Inhaltsliste kontrollieren. Die einzige mitgelieferte PDF ist die selbst erstellte Anleitung im Paketwurzelverzeichnis. Verschlüsselungsanleitung gegen aktuelle Herstellerdokumentation prüfen; echte Wiederherstellung mit **synthetischer** Testdatei auf verfügbaren Geräten durchführen.

**Prüfkriterien:** keine privaten Daten oder fremden Medien im Repo/ZIP oder in der Historie; keine Passwortbeispiele als echte Geheimnisse; nur belegte Aussagen zur Verschlüsselung. Die `.gitignore` ist zusätzliche Sperre, kein Ersatz für Sichtprüfung.

**Ergebnis:** datierter Sicherheitsvermerk mit geprüften Commits, ZIP-Hash, Funden und Maßnahmen.

**Unbestätigt:** Veröffentlichung stoppen. Bei versehentlich veröffentlichten Geheimnissen Rotation und fachgerechte Bereinigung der Historie veranlassen; ein normaler Lösch-Commit allein reicht nicht.

## 5. Gemeinsame Änderungen in Länder-Branches

**Eingaben:** `main`-Commit, Zielland-Commit, betroffene technische Dateien, regionale Prüfstände.

**Schritte:** `git diff main...country/DE -- assets tools` und PR-Diff prüfen. Technische Dateien auf `main` liegen unter `assets/` und `tools/`, im Länderbranch unter `Infrastruktur/assets/` und `Infrastruktur/tools/` beziehungsweise `Infrastructure/assets/` und `Infrastructure/tools/`. Daher gezielt einzelne Dateien oder Änderungen übertragen; ein pauschaler Cherry-Pick mit Pfadverschiebung ist ungeeignet. Regionale `content/`, `guides/`, Quellen, PDF/TXT und nutzerseitige Ordner nie pauschal überschreiben. Danach `python <Infrastruktur>/tools/build.py`, `python <Infrastruktur>/tools/make_readme_pdf.py`, `python <Infrastruktur>/tools/package.py`, `python <Infrastruktur>/tools/verify.py` und vorhandene Tests im Zielland ausführen.

**Prüfkriterien:** technische Funktion gleich, regionale Aussagen unverändert oder erneut fachlich geprüft; generierte Dateien synchron; Tests und Hashes aktualisiert.

**Ergebnis:** PR mit Herkunfts-Commit, Konfliktentscheidungen und Testprotokoll.

**Unbestätigt:** Änderung zurückhalten und Konflikt mit Länderprüfer klären; kein automatisches Überschreiben der regionalen Inhalte.

## 6. Release und Qualität

**Eingaben:** freigegebener Länder-Commit, Quellen- und Sicherheitsvermerke, Geräte-Testmatrix.

**Schritte:** HTML, PDF/TXT und ZIP mit den Werkzeugen im Länder-Infrastrukturordner bauen. Automatisierte Checks und Browser-/Gerätetest durchführen. `Infrastruktur/PRUEFSUMMEN.sha256` oder `Infrastructure/CHECKSUMS.sha256` und ZIP-SHA-256 protokollieren. ZIP in leerem Ordner entpacken und `START.html`, Suche, PDF/TXT, lokalisierte Ordner, Medienergänzung und Rückkopieren prüfen. Tag `<LAND>-YYYY.MM.DD-rN` setzen, ZIP auf `main/releases/` veröffentlichen und den direkten README-Downloadlink prüfen.

**Prüfkriterien:** keine unerlaubten Drittinhalte, sichtbare Quellen- und Prüfstände, funktionierende lokale Links, responsive Ansicht, dokumentierte nicht durchführbare Tests. Fachlich geeignete menschliche Prüfung für Medizin, Sicherheit und regionales Recht liegt vor.

**Ergebnis:** Release mit Downloadlink, Commit, Prüfsummen und Changelog.

**Unbestätigt:** Kein Release. Im Entwurf offen ausweisen; ein bestandener CI-Lauf ist keine fachliche Freigabe.

## 7. Nutzerhinweise und Korrekturen

**Eingaben:** GitHub-Issue oder Meldung ohne private Angaben, betroffene Karte, Land und Sprache.

**Schritte:** Eingang bestätigen und private Daten aus öffentlichen Zitaten entfernen. Problem reproduzieren, Auswirkung priorisieren, Primärquelle prüfen. Bei akuter Gefahr eine klar bezeichnete vorläufige Warnung im README/Issue erwägen; konkrete Karte erst nach Prüfung ändern. PR, Tests und Rückmeldung an die meldende Person erstellen.

**Prüfkriterien:** Reproduktion oder Beleg, regionale Zuständigkeit, Quellenqualität, Datenschutz und Regressionstest.

**Ergebnis:** geschlossener Hinweis mit verlinktem PR oder begründeter Entscheidung; Prüfdatum im Quellenverzeichnis aktualisiert.

**Unbestätigt:** Als offen markieren, zusätzliche Quelle oder Fachprüfung anfordern. Keine Gerüchte als Anleitung übernehmen.
