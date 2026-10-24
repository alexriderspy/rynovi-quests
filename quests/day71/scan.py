"""Day 71 · Where does data go

Personal data leaks into places nobody thinks about: logs, traces, eval sets. Under India's DPDP Act,
every copy is a liability. quests/day71/workspace/ is a small project folder. Find the leaks, then fix them.

Run `python quest.py 71` after each TODO.
"""
import re  # noqa: F401
from pathlib import Path

PATTERNS = {
    "aadhaar": r"(?<!\d)\d{4}[ -]?\d{4}[ -]?\d{4}(?!\d)",
    "pan": r"\b[A-Z]{5}\d{4}[A-Z]\b",
    "phone": r"(?<!\d)(?:\+91[ -]?|0)?[6-9]\d{9}(?!\d)",
    "email": r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+",
}


def find_pii(text: str) -> list[str]:
    """TODO 71.1 · Which kinds of personal data (keys of PATTERNS) appear in the text, sorted."""
    raise NotImplementedError


def scan(folder: Path) -> dict[str, list[str]]:
    """TODO 71.2 · For every file under folder (recursively), the kinds of PII it contains.
    Return {path relative to folder, with forward slashes: sorted kinds} for files that have any, sorted by path."""
    raise NotImplementedError


def clean(folder: Path) -> int:
    """TODO 71.3 · Rewrite every file that has PII, replacing each match with "[<KIND>]" (e.g. "[EMAIL]").
    Do aadhaar before phone. Return how many files you changed. Afterwards scan(folder) must be {}."""
    raise NotImplementedError
