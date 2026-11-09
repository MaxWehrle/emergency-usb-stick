# Design and architecture plan · Emergency USB Stick

Reviewed Nov 9, 2026. This plan applies to the German and U.S. editions. It records the basis for the design; it is **not** proof that every person or device can use the package. That requires real user and device testing.

## Tasks the package must support

1. Download, extract, copy, and open the package without internet.
2. Find a relevant situation quickly and read a clear next action.
3. Add personal files, find them in a file manager, and copy one back.
4. Recognize the date and limits of offline guidance, then follow current local orders.

## Evidence and design decisions

| Evidence | Decision | Check |
|---|---|---|
| The [CDC Clear Communication Index](https://www.cdc.gov/ccindex/tool/how-to-use.html) calls for a clear main message and action at the beginning; it draws on communication research. | The first section shows emergency contact guidance, the offline limit, and search. | Review the first screen and copy. |
| The [GOV.UK emergency service guidance](https://www.gov.uk/service-manual/agile-delivery/making-services-in-an-emergency) notes that fear can affect comprehension and recommends short sentences, fewer links, and visible update times. | No promotional hero area. Each situation shows a title and short summary first; steps expand on selection and carry review dates. | Copy and link review; user testing still needed. |
| [WCAG 2.2 Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) describes use at 320 CSS pixels without two-dimensional scrolling; [WCAG 2.2 Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum) specifies at least 24 × 24 CSS pixels for pointer targets. | One column on narrow screens, large search and link targets, clear focus, scalable type. | Test 320 px and 200/400% zoom; physical device testing still needed. |
| An [experimental hazard-message study](https://www.sciencedirect.com/science/article/pii/S2212420922001364) found better understanding with action and time cues. A static offline guide is not a live warning. | Cards begin with actions. The interface does not invent current location or timing; it clearly defers to current local alerts. | Source review of each country card. |
| [GOV.UK interface-writing guidance](https://www.gov.uk/service-manual/design/writing-for-user-interfaces) favors names that match users' language and lower cognitive load. | U.S. folders use `Guides`, `My-Files`, and `Private-Files`; German folders use `Anleitungen`, `Eigene-Dateien`, and `Vertrauliche-Dateien`. Source code and project details sit behind one Infrastructure folder. | Inspect the ZIP root for each country. |

## File architecture

The extracted package root contains only `START.html`, a country-specific PDF guide, the same instructions as `.txt`, and clearly named user folders. `Infrastructure` or `Infrastruktur` holds sources, license, project documentation, and code. The PDF explains the fallback when local HTML will not open.

Situation guides are ordinary `.txt` files. The HTML page and search are an additional route. Search uses no external library. Without JavaScript, all topics remain visible. Added personal files remain accessible in their folders without running the optional index tool. No private user files are bundled.

## Country scope and risk

Country and language are separate (`US`/`en-US`, `DE`/`de-DE`). Phone numbers, agencies, water guidance, and regional risks are not copied from another country. The U.S. edition is a national baseline with a blank local template; it cannot supply current rules for a state, tribal nation, territory, county, or city.

The offline page is not a live alert service. Safety, medical, evacuation, and local information require continuing primary-source checks and traceable suitable review before publication. Color alone never carries an instruction. PDF and TXT carry the same usage steps.

## Acceptance and remaining evidence

- Automated: ZIP root, internal links, PDF/TXT, text guides, search, media indexing, checksums, and privacy scan.
- Visual: 320 px, wide screen, zoom, print layout, PDF rendering, and contrast.
- With people: observe participants with varied experience and ages completing the four tasks without help. Record errors, search terms, and completion time, then revise.
- With devices: test Windows File Explorer and multiple Android file managers, browsers, USB drives, and adapters. Never generalize from one device test.

Until these tests are done, "intuitive for everyone" remains a **design goal**, not a verified claim.
