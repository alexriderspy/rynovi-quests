"""Day 63 · Cost dashboard

The three numbers a team checks every morning: how fast (p50 and p95 latency), how much each kind of task
costs, and which step eats the budget. quests/day63/runs.py has 200 runs.

Run `python quest.py 63` after each TODO.
"""
import math  # noqa: F401

from quests.day63.runs import PRICES, RUNS  # noqa: F401


def percentile(values: list[float], p: float) -> float:
    """TODO 63.1 · Nearest-rank percentile: sort the values, take the one at position ceil(p/100 × n) (1-based)."""
    raise NotImplementedError


def step_cost(step: dict) -> float:
    return step["tokens_in"] / 1e6 * PRICES[step["model"]]["in"] + step["tokens_out"] / 1e6 * PRICES[step["model"]]["out"]


def cost_per_task(runs: list[dict]) -> dict[str, float]:
    """TODO 63.2 · Average cost in rupees of one run of each task (sum of its steps), rounded to 3 decimals."""
    raise NotImplementedError


def costliest_step(runs: list[dict]) -> tuple[str, float]:
    """TODO 63.3 · Which step name costs the most across all runs: (name, total rupees rounded to 2 decimals)."""
    raise NotImplementedError
