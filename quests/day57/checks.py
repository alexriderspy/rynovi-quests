"""Day 57 · Cheap checks first

LLM judges cost money and time. Plain code catches a lot of failures for free: missing citations,
citations to sources that don't exist, rambling, leftover template text. Run those first and only send
what passes to a judge.

Run `python quest.py 57` after each TODO.
"""
import re  # noqa: F401

ANSWERS = [
    {"id": "q1", "answer": "Interns get 8 casual leaves [1].", "sources": [1, 2]},
    {"id": "q2", "answer": "Hotels are capped at Rs 6,000 a night [3].", "sources": [1]},
    {"id": "q3", "answer": "You can work from home on Mondays and Fridays.", "sources": [1]},
    {"id": "q4", "answer": "The learning budget is [insert amount] a year [1].", "sources": [1]},
    {"id": "q5", "answer": " ".join(["Expenses must be filed within 30 days [1]."] * 15), "sources": [1]},
    {"id": "q6", "answer": "Sick leave needs a doctor's note after 2 days [2].", "sources": [1, 2]},
    {"id": "q7", "answer": "Parental leave is 26 weeks for the birth parent [1].", "sources": [1]},
    {"id": "q8", "answer": "TODO: answer this", "sources": []},
]


def code_checks(item: dict, max_words: int = 60) -> list[str]:
    """TODO 57.1 · Which free checks fail, in this order:
      "no citation"           the answer cites nothing like [1]
      "bad citation"          it cites a number not in item["sources"]
      "too long"              more than max_words words
      "template text"         it contains "TODO" or "[insert"
    """
    raise NotImplementedError


def route(items: list[dict]) -> dict[str, list[str]]:
    """TODO 57.2 · {"failed_code_checks": ids failing any code check, "to_judge": ids passing all of them}, in order."""
    raise NotImplementedError


def judge_cost_saved(items: list[dict], cost_per_judge_call: float) -> float:
    """TODO 57.3 · Money saved by not sending failed items to the judge: number failed × cost, rounded to 2 decimals."""
    raise NotImplementedError
