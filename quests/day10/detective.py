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
    raise NotImplementedError


def find_total(text: str) -> float | None:
    """TODO 10.2 · Find the line "Total: Rs 12,449.00" and return 12449.0.
    Careful: "Subtotal: Rs ..." is NOT the total. Return None if there's no total.
    (hint: a regex like r"^Total: Rs ([\\d,]+\\.\\d\\d)" with re.MULTILINE, then remove the commas)"""
    raise NotImplementedError


def line_items(path: Path) -> list[dict]:
    """TODO 10.3 · Read the table on the first page and return one dict per row, skipping the header:
    {"item": "GPU hours (A100)", "qty": 12, "amount": 18000.0}"""
    raise NotImplementedError


def is_scan(path: Path) -> bool:
    """TODO 10.4 · True when the PDF has no text layer (so it needs OCR or a vision model), else False."""
    raise NotImplementedError
