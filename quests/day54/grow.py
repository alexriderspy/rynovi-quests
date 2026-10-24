"""Day 54 · Grow the set

Your golden set must grow with every new failure you find, without losing old cases (a bug you fixed
once can come back). Cases are dicts: {"id": "...", "input": "...", "expect": "...", "category": "..."}.

Run `python quest.py 54` after each TODO.
"""
import re  # noqa: F401


def normalise(text: str) -> str:
    """TODO 54.1 · Lowercase, strip punctuation (keep letters, digits and spaces), squash spaces.
    Two inputs that normalise the same are duplicates."""
    raise NotImplementedError


def add_cases(golden: list[dict], new: list[dict]) -> tuple[list[dict], list[str]]:
    """TODO 54.2 · Return (grown golden set, ids of new cases skipped as duplicates).
    Keep every old case, in order. Append new cases whose normalised input isn't already in the set
    (including duplicates within `new` itself: the first one wins)."""
    raise NotImplementedError


def bump_version(version: str, golden_before: list[dict], golden_after: list[dict]) -> str:
    """TODO 54.3 · Versions look like "v3". If the set changed (different number of cases), return the next
    version ("v4"); otherwise return the same one. Scores are only comparable within one version."""
    raise NotImplementedError
