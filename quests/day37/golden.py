"""Day 37 · Golden set

A golden set is the list of real questions with what a good answer must contain. Every change to
your RAG assistant gets scored against it, so it has to be correct and it has to cover everything.

quests/day37/golden.jsonl has 8 cases, one JSON object per line. You'll validate it, find the gaps,
and then grow it (by hand, from the handbook in quests/day33/corpus.py) until it's good enough.

Run `python quest.py 37` after each TODO.
"""
import json  # noqa: F401
from pathlib import Path
from typing import Literal  # noqa: F401

from pydantic import BaseModel, Field, ValidationError, model_validator  # noqa: F401

GOLDEN = Path(__file__).parent / "golden.jsonl"
CATEGORIES = ["leave", "wfh", "expenses", "learning", "security", "out_of_scope"]


class GoldenCase(BaseModel):
    # TODO 37.1 · Fields:
    #   question: str, at least 10 characters
    #   category: one of CATEGORIES (hint: Literal["leave", "wfh", ...])
    #   expect: "answer" or "refuse"
    #   must_include: list[str], default empty
    #   source: str or None, default None
    # and a model validator: an "answer" case needs at least one must_include item AND a source;
    # a "refuse" case must have an empty must_include. Raise ValueError otherwise.
    pass


def load_golden(path: Path = GOLDEN) -> list[GoldenCase]:
    """TODO 37.1 · Read the file line by line (skip blank lines), parse each as JSON and validate it.
    If a line is broken, raise ValueError(f"line {n}: ...") with n counting from 1."""
    raise NotImplementedError


def coverage(cases: list[GoldenCase]) -> dict[str, int]:
    """TODO 37.2 · How many cases per category, including categories with 0."""
    raise NotImplementedError


def gaps(cases: list[GoldenCase], min_per_category: int = 3) -> list[str]:
    """TODO 37.2 · Categories with fewer than min_per_category cases, in CATEGORIES order."""
    raise NotImplementedError

# TODO 37.3 · Now grow golden.jsonl itself until:
#   - it has at least 30 cases
#   - every category has at least 3
#   - at least 5 are "refuse" cases (questions the handbook can't answer)
#   - no question appears twice (ignoring case)
# Write real questions an employee would ask, and check each answer against the handbook.
