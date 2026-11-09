# Kopierbare Agenten-Prompts

Platzhalter in `{geschweiften Klammern}` vor Benutzung ersetzen. Dem Agenten nur öffentliche, bereinigte Informationen geben. Jede Antwort muss zwischen **belegt**, **nicht geprüft** und **Änderungsvorschlag** unterscheiden. Der Agent darf keine Quellen, Gerätetests oder Prüfer erfinden und sicherheitskritische Inhalte nicht selbst freigeben.

`{INFRA}` steht für `Infrastruktur` (DE) oder `Infrastructure` (US), `{GUIDES}` für `Anleitungen` oder `Guides`, `{EIGENE}` für `Eigene-Dateien` oder `My-Files`, `{PRIVAT}` für `Vertrauliche-Dateien` oder `Private-Files`. Jede Länderfassung muss diese Pfade selbst festlegen; Deutsch und Englisch sind keine Länderkennungen.

## Quellenprüfung

```text
Prüfe country/{LAND} in Sprache {SPRACHE}, Commit {SHA}, Stand {DATUM}. Lies {INFRA}/QUELLEN.md bzw. {INFRA}/SOURCES.md und jede zeitkritische Karte in {INFRA}/content/. Recherchiere zuständige aktuelle Primärquellen für Warnungen, Notrufnummern, Links und regionale Empfehlungen. Liefere je Aussage: Datei, exakte Fundstelle, Herausgeber, URL, Veröffentlichungsdatum falls belegt, Abrufdatum, Bewertung und konkreten Diff-Vorschlag. Markiere unbestätigte Angaben. Führe python maintenance/audit.py --country {PFAD} --check-links aus. Veröffentliche nichts; Medizin, Sicherheit und Recht benötigen menschliche Prüfung.
```

## Hardware und Bezugsquellen

```text
Prüfe Kaufbeispiele für {LAND} am {DATUM}. Verwende Herstellerangaben und echte Händlerseiten der Region. Erfasse Modell/Variante, Anschlüsse, nominelle Kapazität, beobachteten Gesamtpreis und Verfügbarkeit mit URL und Datum. Entferne Affiliate-Parameter. Unterscheide Herstellerangabe von eigenem Gerätetest. Aktualisiere nur belegte Angaben in {INFRA}/ANLEITUNG.md bzw. {INFRA}/GET-STARTED.md sowie im PDF/TXT-Liesmich; Preise sind Momentaufnahmen. Nenne nicht prüfbare Punkte offen.
```

## Regionalisierung

```text
Bereite einen neuen Branch country/{LAND} für {SPRACHE} vor. Beginne mit main, regionalisiere alle Themen anhand zuständiger lokaler Primärquellen: Warnsystem, Nummern, Wasser, Gesundheit, Wetter, Behörden, Recht, Hardwaremarkt. Berücksichtige Bundesstaaten, Territorien oder andere Unterregionen mit einer klaren lokalen Vorlage, wenn nationale Angaben allein nicht reichen. Übernimm keine Angaben anderer Länder ungeprüft. Übersetze auch Oberfläche, alle sichtbaren Ordnernamen, PDF/TXT-Anleitung, persönliche Vorlagen und Tests. Erfasse Quelle, Nutzungsrechte, Veröffentlichungs- und Prüfdatum. Erzeuge START.html und normale Textdateien, prüfe offline und auf verfügbaren Geräten. Liste fehlende Fachprüfungen; kennzeichne den Branch bis zu deren Abschluss ausdrücklich als Entwurf.
```

## Sicherheit und Datenschutz

```text
Untersuche {BRANCH} und seine vollständige Git-Historie auf persönliche Daten, Schlüssel, Zugangsdaten und unerlaubte Medien. Prüfe ZIP-Inhalt, .gitignore, {PRIVAT}/ und {EIGENE}/. Die länderspezifische PDF im Paketwurzelverzeichnis ist erlaubt; andere Medien benötigen explizite Rechteprüfung. Verwende nur synthetische Testdateien. Prüfe die Verschlüsselungsanleitung gegen offizielle Dokumentation und protokolliere tatsächlich durchgeführte Wiederherstellungstests pro Gerät. Liefere Fundstellen, Risiko und konkrete Bereinigung. Bei unbestätigter Sicherheit Veröffentlichung stoppen; keine Geheimnisse in Antwort oder Log kopieren.
```

## Gemeinsame Änderungen

```text
Übertrage die technischen Änderungen aus main Commit {SHA} nach country/{LAND}. Zeige zuerst den Diff und die betroffenen Pfade. Ordne main/tools und main/assets den Pfaden {INFRA}/tools und {INFRA}/assets zu. Übernimm technische Dateien gezielt; überschreibe regionale {INFRA}/content/, {INFRA}/guides/, Quellen, PDF/TXT und {GUIDES}/ nur nach erneuter regionaler Prüfung. Baue START.html, PDF/TXT und ZIP neu, führe alle verfügbaren Tests aus und protokolliere Konflikte, Herkunfts-Commit und offene Punkte. Bei ungeklärtem Konflikt keinen Merge vorschlagen.
```

## Release

```text
Prüfe country/{LAND} Commit {SHA} für Release {TAG}. Verifiziere Quellenstand, menschliche Fachprüfung, Datenschutz, Lizenzen, Offline-Start, Suche, lokale Links, ZIP, PDF/TXT im Wurzelverzeichnis, lokalisierte Ordner, Medienergänzung, schmale Ansicht und verfügbare Windows-/Android-Geräte. Führe python maintenance/audit.py --country {ZIP} aus. Erzeuge SHA-256 für Paketdateien und ZIP. Liefere eine Go/No-go-Tabelle mit Belegen und offenem Teststatus. Veröffentliche nur bei vollständiger Freigabe; ein grüner technischer Test ersetzt keine fachliche Prüfung.
```

## Nutzerhinweis

```text
Bearbeite den bereinigten Nutzerhinweis {ISSUE_URL} zu {LAND}/{SPRACHE}. Enthält die Meldung private Daten, zitiere sie nicht öffentlich. Reproduziere den Fehler, prüfe zuständige Primärquellen und schätze die Auswirkung ein. Gib einen konkreten Patch mit Tests, Quellen und Prüfdatum oder eine begründete Ablehnung. Kennzeichne unbelegte Aussagen; bei Sicherheitsrisiko bis zur menschlichen Prüfung keine neue Handlungsanweisung veröffentlichen.
```
