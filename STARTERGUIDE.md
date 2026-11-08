# In fünf Schritten zum Notfall-Stick

**Deutschland · de-DE · Recherche 09.11.2026**

`ZIP herunterladen → entpacken → Ordnerinhalt auf Stick kopieren → eigene Dateien ergänzen → offline testen`

1. Laden Sie das deutsche ZIP über die Projekt-Startseite herunter und entpacken Sie es. Prüfen Sie, ob `START.html` sichtbar ist. Wenn Sie dieses Verzeichnis bereits sehen, ist das Paket schon entpackt.
2. Kopieren Sie **alle Dateien und Ordner innerhalb** des entpackten Verzeichnisses auf einen leeren USB-Stick. `START.html` soll direkt auf dem Stick liegen.
3. Öffnen Sie `START.html` unter Windows durch Doppelklick. Auf Android: USB-C-Stick oder passenden Adapter anschließen, im Dateimanager den Stick öffnen und `START.html` mit einem Browser öffnen. Die konkrete Bedienung hängt vom Gerät und der Android-Version ab.
4. Ergänzen Sie Ihre Dateien in `personal/Fotos/`, `personal/Karten/`, `personal/Dokumente/`. Nutzen Sie für sensible Daten die Anleitung in `private/README.txt`. Optional baut `python tools/build.py` die Linkliste auf der Startseite neu auf; Python ist dafür erforderlich, nicht für den Stick selbst.
5. Trennen Sie das Gerät vom Netz oder aktivieren Sie Flugmodus. Öffnen Sie `START.html`, suchen Sie eine Lagekarte, öffnen Sie eine Textdatei in `guides/` und kopieren Sie eine eigene Datei vom Stick zurück. Werfen Sie den Stick danach sicher aus.

## Größe wählen

Rechnen Sie den **tatsächlichen** Umfang Ihrer Dateien zusammen und addieren Sie mindestens 30 % Reserve für neue Dateien, Dateisystem und Aktualisierungen. Beispiel: 18 GB Medien + 2 GB Dokumente = 20 GB; mit 30 % Reserve 26 GB. Ein 32-GB-Stick ist nominell groß genug, ein 64-GB-Stick bietet mehr Spielraum. Die am Gerät angezeigte nutzbare Kapazität kann kleiner sein.

| Bibliothek | Beispielrechnung | Sinnvolle nominelle Größe |
|---|---:|---:|
| Klein: Dokumente und wenige Fotos | 5 GB × 1,3 = 6,5 GB | 16–32 GB |
| Mittel: viele Fotos und Karten | 35 GB × 1,3 = 45,5 GB | 64 GB |
| Groß: umfangreiche Medien | 140 GB × 1,3 = 182 GB | 256 GB |

## Kaufen und prüfen

- Wählen Sie die Kapazität nach Ihrer Rechnung. Für Windows-Rechner und Android-Geräte mit USB-C ist ein Stick mit **USB-A und USB-C** bequem; sonst einen passenden USB-C-Adapter einplanen. Ein Anschluss allein garantiert keine Lesbarkeit: Gerät, Dateisystem und Dateimanager müssen den Stick unterstützen.
- Kaufen Sie bei nachvollziehbaren Händlern, vergleichen Sie **Gesamtpreis inklusive Versand** und achten Sie auf Rückgabe- und Gewährleistungsbedingungen. Kein Stick ist ausfallsicher; zwei Kopien und Lesetests bleiben nötig.
- Beispiele im deutschen Markt, recherchiert am **09.11.2026**, ohne Affiliate-Links: [Sandisk Ultra Dual Drive Go 128 GB bei MediaMarkt](https://www.mediamarkt.de/de/product/_sandisk-ultra%C2%AE-dual-drive-go-2609988.html) (Shopseite zeigte 24,99 €) und [Sandisk Ultra Dual Drive Go 256 GB bei MediaMarkt](https://www.mediamarkt.de/de/product/_sandisk-ultrar-dual-drive-go-usb-type-ctm-usb-stick-256-gb-400-mbs-dunkelgrau-2982110.html) (Shopseite zeigte 39,99 €). Shoppreise und Verfügbarkeit können sich jederzeit ändern; die angezeigten Seiten können zwischengespeichert sein. Prüfen Sie den aktuellen Warenkorb vor Kauf. [Herstellerangaben zu Anschlüssen und Systemen](https://www.sandisk.com/products/usb-flash-drives/sandisk-ultra-dual-drive-go-usb-3-1-type-c?sku=SDDDC3-128G-G46) sind keine Prüfung Ihres konkreten Geräts.
- Formatieren Sie einen neuen Stick nur, wenn Sie sicher sind, dass keine benötigten Daten darauf liegen. Prüfen Sie Dateisystem und maximale Dateigrößen mit Ihren eigenen Windows- und Android-Geräten. Ein Geräteversuch wurde für dieses Projekt nicht durchgeführt.

## Zwei Kopien und Wiederherstellung

Erstellen Sie eine zweite vollständige Kopie und bewahren Sie sie an einem anderen Ort auf. Prüfen Sie nach jeder wichtigen Änderung beide Sticks: `START.html` öffnen, Stichwort suchen, ausgewählte Fotos und Dokumente lesen und mindestens eine Datei **auf ein anderes Gerät zurückkopieren**. Wiederholen Sie diesen Test regelmäßig, beispielsweise alle drei Monate. Tauschen Sie defekte oder nicht lesbare Medien aus. Bewahren Sie Tresorpasswort und Wiederherstellungsschlüssel **getrennt** vom Stick auf.

## Eigene Checkliste

- [ ] Kontaktliste und Treffpunkt ausgedruckt
- [ ] Wichtige Urkunden, Ausweise, Versicherungs- und Gesundheitsnachweise als persönliche Kopie
- [ ] Benötigte Medikamente, Ladegeräte und Powerbank berücksichtigt
- [ ] Eigene Fotos und Offline-Karten mit Nutzungsrecht ergänzt
- [ ] Verschlüsselten Bereich auf Windows **und** Android mit einer Testdatei geprüft
- [ ] Zweite Kopie und Rückkopier-Test durchgeführt

Digitale Kopien ersetzen Originaldokumente nicht. Erkundigen Sie sich bei der zuständigen Stelle, ob ein Original oder eine beglaubigte Kopie benötigt wird.
