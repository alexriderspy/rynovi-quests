"""Day 53 · Open coding

Error analysis: read real traces, write one plain note per failure, then group the notes into categories
and count them. The biggest categories are where to spend your time.
quests/day53/notes.py has 30 notes already tagged with a category.

Run `python quest.py 53` after each TODO.
"""
from quests.day53.notes import NOTES  # noqa: F401


def count_categories(notes: list[dict]) -> dict[str, int]:
    """TODO 53.1 · How many notes in each category, most common first (dicts keep insertion order).
    Ties: alphabetical."""
    raise NotImplementedError


def top_share(notes: list[dict], n: int = 2) -> float:
    """TODO 53.2 · The share of all failures (0 to 1) covered by the n biggest categories, rounded to 2 decimals."""
    raise NotImplementedError


def examples(notes: list[dict], category: str, k: int = 3) -> list[str]:
    """TODO 53.3 · The first k trace ids in that category, in the order they appear. You'll show these
    to the team so everyone sees real failures, not just a number."""
    raise NotImplementedError
