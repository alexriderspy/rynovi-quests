"""Day 32 · The verdict

You trained a fine-tune. Did it help? Three models labelled the 36 newest issues (quests/day32/data.py):
  baseline  TF-IDF + logistic regression
  base      the untrained LLM with a good prompt
  finetune  your LoRA fine-tune
Answer with numbers, not vibes. Run `python quest.py 32` after each TODO.
"""
from quests.day32.data import COST_PER_1K, ISSUES  # noqa: F401

LABELS = ["bug", "feature", "question"]
MODELS = ["baseline", "base", "finetune"]


def accuracy(model: str) -> float:
    """TODO 32.1 · Share of issues where the model's label equals the true label (0 to 1)."""
    raise NotImplementedError


def f1(model: str, label: str) -> float:
    """TODO 32.2 · F1 for one label: 2·P·R / (P + R), where
      precision P = correct predictions of `label` / all predictions of `label`
      recall    R = correct predictions of `label` / all issues truly `label`
    Return 0.0 if P + R is 0."""
    raise NotImplementedError


def macro_f1(model: str) -> float:
    """TODO 32.3 · The plain average of f1 over the three labels. Better than accuracy when classes differ in size."""
    raise NotImplementedError


def verdict() -> str:
    """TODO 32.4 · Pick the model to ship:
      the one with the highest macro F1, BUT if a cheaper model (COST_PER_1K) is within 0.02 macro F1
      of the best, ship the cheaper one instead. Return its name."""
    raise NotImplementedError
