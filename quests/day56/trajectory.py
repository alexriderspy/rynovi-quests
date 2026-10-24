"""Day 56 · Score the trajectory

A right final answer isn't enough for an agent. How it got there matters: the right tools, in a sensible
order, without wandering. quests/day56/runs.py has 20 runs with the expected tools for each task.

Run `python quest.py 56` after each TODO.
"""
from quests.day56.runs import RUNS  # noqa: F401


def success_rate(runs: list[dict]) -> float:
    """TODO 56.1 · Share of runs that finished the task."""
    raise NotImplementedError


def used_right_tools(run: dict) -> bool:
    """TODO 56.2 · True if the expected tools appear in the run's steps in the same order
    (other calls may sit in between: it's a subsequence check)."""
    raise NotImplementedError


def wasted_steps(run: dict) -> int:
    """TODO 56.3 · Extra calls beyond what was needed: len(steps) - len(expected_tools), never below 0."""
    raise NotImplementedError


def report(runs: list[dict]) -> dict:
    """TODO 56.3 · {"success": success_rate, "right_tools": share of runs with used_right_tools,
    "avg_wasted": mean wasted steps rounded to 2 decimals, "wanderers": run ids with more than 3 wasted steps}"""
    raise NotImplementedError
