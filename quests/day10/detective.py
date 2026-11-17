"""Day 10 · Invoice detective

Three invoices in quests/day10/invoices/:
  digital.pdf  a normal PDF with real text in it
  table.pdf    line items in a table
  scan.pdf     a photo of a page: no text layer at all

Use pdfplumber (pip install pdfplumber). Run `python quest.py 10` after each TODO.
"""
import re  # noqa: F401
from pathlib import Path

import pdfplumber  # noqa: F401

INVOICES = Path(__file__).parent / "invoices"


def extract_text(path: Path) -> str:
    """TODO 10.1 · Return the text of every page joined with newlines.
    A page with no text gives None from extract_text(); treat that as ""."""
    with pdfplumber.open(path) as pdf:
        return "\n".join(
            page.extract_text() or ""
            for page in pdf.pages
        )
    # raise NotImplementedError


def find_total(text: str) -> float | None:
    """TODO 10.2 · Find the line "Total: Rs 12,449.00" and return 12449.0.
    Careful: "Subtotal: Rs ..." is NOT the total. Return None if there's no total.
    (hint: a regex like r"^Total: Rs ([\\d,]+\\.\\d\\d)" with re.MULTILINE, then remove the commas)"""
    match = re.search(
        r"^Total: Rs ([\d,]+\.\d{2})",
        text,
        re.MULTILINE
    )

    if not match:
        return None

    return float(match.group(1).replace(",", ""))
    # raise NotImplementedError


def line_items(path: Path) -> list[dict]:
    """TODO 10.3 · Read the table on the first page and return one dict per row, skipping the header:
    {"item": "GPU hours (A100)", "qty": 12, "amount": 18000.0}"""
    # raise NotImplementedError
    with pdfplumber.open(path) as pdf:
        table = pdf.pages[0].extract_table()

    if not table:
        return []

    items = []

    for row in table[1:]:  # Skip header
        items.append({
            "item": row[0],
            "qty": int(row[1]),
            "amount": float(row[2].replace(",", ""))
        })

    return items


def is_scan(path: Path) -> bool:
    """TODO 10.4 · True when the PDF has no text layer (so it needs OCR or a vision model), else False."""
    # raise NotImplementedError
    with pdfplumber.open(path) as pdf:
        return not any(
            (page.extract_text() or "").strip()
            for page in pdf.pages
        )
