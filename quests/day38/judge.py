"""Day 38 · Judge the judge

An LLM judge is only useful if it agrees with you, on the failures most of all.
quests/day38/labels.py has 30 answers you labelled pass or fail, and what two judges said.
"pass" counts as the positive class.

Run `python quest.py 38` after each TODO.
"""
from quests.day38.labels import LABELS  # noqa: F401


def confusion(judge: str) -> dict[str, int]:
    """TODO 38.1 · Compare LABELS[i][judge] with LABELS[i]["human"] and count
      tp: judge pass, human pass     fp: judge pass, human fail
      tn: judge fail, human fail     fn: judge fail, human pass
    Return {"tp": .., "fp": .., "tn": .., "fn": ..}."""
    raise NotImplementedError


def agreement(judge: str) -> float:
    """TODO 38.2 · Share of answers where the judge and you said the same thing."""
    raise NotImplementedError


def tpr(judge: str) -> float:
    """TODO 38.3 · True positive rate: of the answers you passed, the share the judge passed. tp / (tp + fn)"""
    raise NotImplementedError


def tnr(judge: str) -> float:
    """TODO 38.3 · True negative rate: of the answers you failed, the share the judge failed. tn / (tn + fp)
    This is the one that matters: a judge that passes everything is useless."""
    raise NotImplementedError


def pick_judge(judges: tuple[str, ...] = ("judge_v1", "judge_v2")) -> str:
    """TODO 38.4 · Pick the judge whose WORSE rate, min(tpr, tnr), is highest."""
    raise NotImplementedError
