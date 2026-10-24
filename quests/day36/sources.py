"""Day 36 · Show your sources

In a company, an answer nobody can check is useless, and a confident wrong answer is worse.
quests/day36/cases.py has 6 answers from a RAG assistant. Some cite sources that don't exist,
some cite nothing, and one should never have been answered at all.

Run `python quest.py 36` after each TODO.
"""
import re  # noqa: F401

from quests.day36.cases import CASES  # noqa: F401

REFUSAL = "I couldn't find that in the documents."


def cited_ids(answer: str) -> list[int]:
    """TODO 36.1 · The source numbers cited like [1] or [2], in order of appearance, without repeats."""
    raise NotImplementedError


def citation_problems(answer: str, sources: list[dict]) -> list[str]:
    """TODO 36.2 · What's wrong with the citations?
      "no citations"            when the answer cites nothing
      "missing source {n}"      for each cited number that isn't one of the sources' ids
    An answer with only valid citations gives []."""
    raise NotImplementedError


def should_refuse(sources: list[dict], threshold: float = 0.5) -> bool:
    """TODO 36.3 · Refuse when retrieval came back weak: no sources, or the best score is below threshold."""
    raise NotImplementedError


def final_answer(case: dict) -> str:
    """TODO 36.4 · What the user should actually see:
      REFUSAL if should_refuse(case["sources"]) or the answer has any citation problems,
      otherwise the model's answer unchanged."""
    raise NotImplementedError
