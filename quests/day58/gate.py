"""Day 58 · Regression gate

Every pull request runs the evals. If any score drops below the last release, the build must fail,
loudly and specifically, so nobody merges a regression by accident.
Scores are dicts like {"faithfulness": 0.91, "hit_rate_at_5": 0.84}.

Run `python quest.py 58` after each TODO.
"""
import json  # noqa: F401
import sys  # noqa: F401


def drops(baseline: dict, current: dict, tolerance: float = 0.01) -> list[str]:
    """TODO 58.1 · One line per metric that fell by MORE than tolerance, in baseline order:
        "faithfulness: 0.91 -> 0.86"   (2 decimals)
    A metric missing from current counts as a drop: "faithfulness: 0.91 -> missing"."""
    raise NotImplementedError


def main(argv: list[str]) -> int:
    """TODO 58.2 · CLI: python gate.py baseline.json current.json
    Print each drop on its own line and return 1 if there are any; otherwise print "no regressions" and return 0.
    (In CI, a non-zero exit code fails the build.)"""
    raise NotImplementedError


def next_baseline(baseline: dict, current: dict, tolerance: float = 0.01) -> dict:
    """TODO 58.3 · After a merge, the new baseline is current, but only if there were no drops.
    Otherwise keep the old baseline. Return a new dict either way."""
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
