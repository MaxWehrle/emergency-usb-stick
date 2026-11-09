"""Build the large-print country read-me PDF from content/readme_pdf.json.

Requires ReportLab; the USB release contains the finished PDF, not this tool.
"""
from pathlib import Path
import json

from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
    Spacer, Table, TableStyle,
)

rl_config.invariant = 1
root = Path(__file__).resolve().parents[1]
data = json.loads((root / "content/readme_pdf.json").read_text(encoding="utf-8"))
if len(data["steps"]) != 5 or len(data["folders"]) < 4:
    raise ValueError("Expected five setup steps and at least four folder descriptions")

page_size = A4 if data["locale"] == "de-DE" else letter
forest = colors.HexColor("#173F3C")
muted = colors.HexColor("#405A56")
light = colors.HexColor("#EDF5F2")
orange = colors.HexColor("#B56818")
white = colors.white

body = ParagraphStyle("body", fontName="Helvetica", fontSize=12.5,
                      leading=18, textColor=forest, spaceAfter=0)
small = ParagraphStyle("small", parent=body, fontSize=10.5, leading=15)
title = ParagraphStyle("title", parent=body, fontName="Helvetica-Bold",
                       fontSize=25, leading=29, spaceAfter=10)
heading = ParagraphStyle("heading", parent=body, fontName="Helvetica-Bold",
                         fontSize=17, leading=22, spaceBefore=14, spaceAfter=10)
row_title = ParagraphStyle("row-title", parent=body, fontName="Helvetica-Bold",
                           fontSize=12.5, leading=18)
number_style = ParagraphStyle("number", parent=body, fontName="Helvetica-Bold",
                              fontSize=16, leading=19, textColor=white,
                              alignment=TA_LEFT)

out = root / data["filename"]
doc = SimpleDocTemplate(str(out), pagesize=page_size,
                        rightMargin=19 * mm, leftMargin=19 * mm,
                        topMargin=20 * mm, bottomMargin=20 * mm,
                        title=data["title"], author="Emergency USB Stick",
                        subject=data["subtitle"])
width = page_size[0] - 38 * mm
story = [Paragraph(data["eyebrow"], ParagraphStyle("eyebrow", parent=small,
          fontName="Helvetica-Bold", textColor=orange, spaceAfter=10)),
         Paragraph(data["title"], title), Paragraph(data["subtitle"], small),
         Spacer(1, 13), HRFlowable(width=width, thickness=1.5, color=forest),
         Spacer(1, 12), Paragraph(data["lead"], body),
         Paragraph(data["steps_title"], heading)]

for index, item in enumerate(data["steps"], 1):
    number = Table([[Paragraph(str(index), number_style)]], colWidths=[31], rowHeights=[31])
    number.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), forest),
                                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                                ("TOPPADDING", (0, 0), (-1, -1), 4),
                                ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    content = Paragraph(f'<b>{item["title"]}</b><br/>{item["text"]}', body)
    row = Table([[number, content]], colWidths=[43, width - 43])
    row.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                             ("LEFTPADDING", (0, 0), (-1, -1), 0),
                             ("RIGHTPADDING", (0, 0), (0, -1), 10),
                             ("TOPPADDING", (0, 0), (-1, -1), 6),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
    story.append(KeepTogether([row, Spacer(1, 3)]))

story += [Spacer(1, 9), Table([[Paragraph(data["first_page_note"], small)]],
                            colWidths=[width], style=TableStyle([
                                ("BACKGROUND", (0, 0), (-1, -1), light),
                                ("BOX", (0, 0), (-1, -1), 0.5, forest),
                                ("LEFTPADDING", (0, 0), (-1, -1), 13),
                                ("RIGHTPADDING", (0, 0), (-1, -1), 13),
                                ("TOPPADDING", (0, 0), (-1, -1), 11),
                                ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
                            ])), PageBreak(),
          Paragraph(data["folders_title"], title),
          Paragraph(data["folders_intro"], body), Spacer(1, 12)]

for folder in data["folders"]:
    row = Table([[Paragraph(folder["name"], row_title),
                  Paragraph(folder["description"], body)]],
                colWidths=[width * 0.37, width * 0.63])
    row.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), light),
                             ("VALIGN", (0, 0), (-1, -1), "TOP"),
                             ("LINEBELOW", (0, 0), (-1, -1), 1, white),
                             ("LEFTPADDING", (0, 0), (-1, -1), 11),
                             ("RIGHTPADDING", (0, 0), (-1, -1), 11),
                             ("TOPPADDING", (0, 0), (-1, -1), 9),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
    story.append(row)

story += [Paragraph(data["help_title"], heading), Paragraph(data["help"], body),
          Spacer(1, 13), Paragraph(data["privacy"], small),
          Spacer(1, 8), Paragraph(data["safety"], small)]

if data.get("device_sections"):
    story += [PageBreak(), Paragraph(data["device_title"], title),
              Paragraph(data["device_intro"], body), Spacer(1, 8)]
    for section in data["device_sections"]:
        story.append(Paragraph(section["title"], heading))
        for i, step in enumerate(section["steps"], 1):
            story.append(Paragraph(f"<b>{i}.</b> {step}",
                                   ParagraphStyle(f"device-{len(story)}", parent=body, spaceAfter=8)))

if data.get("care_sections"):
    story += [PageBreak(), Paragraph(data["care_title"], title),
              Paragraph(data["care_intro"], body)]
    for section in data["care_sections"]:
        story.append(Paragraph(section["title"], heading))
        for item in section["items"]:
            story.append(Paragraph(item,
                                   ParagraphStyle(f"care-{len(story)}", parent=body, spaceAfter=8)))

def page_footer(canvas, document):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#BED0CA"))
    canvas.line(19 * mm, 16 * mm, page_size[0] - 19 * mm, 16 * mm)
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(muted)
    canvas.drawString(19 * mm, 11 * mm, data["footer"])
    canvas.drawRightString(page_size[0] - 19 * mm, 11 * mm, str(document.page))
    canvas.restoreState()

doc.build(story, onFirstPage=page_footer, onLaterPages=page_footer)
plain = [data["title"], data["subtitle"], "", data["lead"], "", data["steps_title"], ""]
plain += [f'{i}. {item["title"]}\n{item["text"]}\n' for i, item in enumerate(data["steps"], 1)]
plain += [data["first_page_note"].replace("<b>", "").replace("</b>", ""), "",
          data["folders_title"], data["folders_intro"], ""]
plain += [f'{folder["name"]}\n{folder["description"]}\n' for folder in data["folders"]]
plain += [data["help_title"], data["help"], "", data["privacy"], "", data["safety"], ""]
if data.get("device_sections"):
    plain += [data["device_title"], data["device_intro"], ""]
    for section in data["device_sections"]:
        plain += [section["title"]]
        plain += [f"{i}. {step}" for i, step in enumerate(section["steps"], 1)]
        plain += [""]
if data.get("care_sections"):
    plain += [data["care_title"], data["care_intro"], ""]
    for section in data["care_sections"]:
        plain += [section["title"], *section["items"], ""]
(root / data["txt_filename"]).write_text("\n".join(plain), encoding="utf-8", newline="\n")
print(f"Created {out}")
