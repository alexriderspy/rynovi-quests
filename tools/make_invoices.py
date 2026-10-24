"""Makes the three day-10 invoices. You don't need to run this; the PDFs are in the repo."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

OUT = Path(__file__).parent.parent / "quests" / "day10" / "invoices"
OUT.mkdir(parents=True, exist_ok=True)
styles = getSampleStyleSheet()

doc = SimpleDocTemplate(str(OUT / "digital.pdf"), pagesize=A4)
doc.build([
    Paragraph("Chai Point Supplies Pvt Ltd", styles["Title"]),
    Paragraph("Invoice no: CPS-2026-0412", styles["Normal"]),
    Paragraph("Bill to: Rynovi Labs, Bengaluru", styles["Normal"]),
    Spacer(1, 12),
    Paragraph("Masala chai, 40 cups and 12 boxes of biscuits for the team offsite.", styles["Normal"]),
    Spacer(1, 12),
    Paragraph("Subtotal: Rs 10,550.00", styles["Normal"]),
    Paragraph("GST (18%): Rs 1,899.00", styles["Normal"]),
    Paragraph("<b>Total: Rs 12,449.00</b>", styles["Normal"]),
])

doc = SimpleDocTemplate(str(OUT / "table.pdf"), pagesize=A4)
rows = [["Item", "Qty", "Amount"], ["GPU hours (A100)", "12", "18,000.00"], ["Vector DB, monthly", "1", "4,500.50"], ["Support plan", "2", "3,000.00"]]
table = Table(rows, colWidths=[260, 60, 120])
table.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.8, colors.black), ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey)]))
doc.build([
    Paragraph("CloudDesk Infra", styles["Title"]),
    Paragraph("Invoice no: CD-7781", styles["Normal"]),
    Spacer(1, 12),
    table,
    Spacer(1, 12),
    Paragraph("<b>Total: Rs 25,500.50</b>", styles["Normal"]),
])

img = Image.new("L", (1240, 1754), 245)
draw = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
except OSError:
    font = ImageFont.load_default()
for i, line in enumerate(["Sharma Stationers", "Invoice no: SS-0098", "Notebooks x 20", "Pens x 50", "Total: Rs 2,340.00"]):
    draw.text((120, 160 + i * 90), line, fill=20, font=font)
img.rotate(1.2, fillcolor=245).save(OUT / "scan.pdf")
print("made", sorted(p.name for p in OUT.iterdir()))
