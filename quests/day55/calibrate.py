"""Day 55 · Calibrate the judge

You tuned a judge until it agreed with you. But was that luck? Check it on answers it was never tuned on,
then use its known error rates to correct the pass rate it reports on production traffic.
quests/day55/data.py has your labels vs the judge, split into "dev" and "test", plus 1,000 production verdicts.

Run `python quest.py 55` after each TODO.
"""
from quests.day55.data import LABELLED, PRODUCTION  # noqa: F401


def rates(rows: list[dict]) -> tuple[float, float]:
    """TODO 55.1 · (TPR, TNR) of the judge against your labels. "pass" is positive.
    TPR = judge pass among your passes; TNR = judge fail among your fails."""
    raise NotImplementedError


def holds_up(min_rate: float = 0.75) -> bool:
    """TODO 55.2 · Compute rates on the dev split and on the test split. The judge holds up if BOTH rates on
    test are at least min_rate AND neither test rate is more than 0.1 below its dev rate."""
    raise NotImplementedError


def corrected_pass_rate() -> float:
    """TODO 55.3 · The judge says p_obs of PRODUCTION passed, but it makes mistakes. Using TPR and TNR from the
    TEST split, estimate the true pass rate:  (p_obs + TNR - 1) / (TPR + TNR - 1)
    clipped to [0, 1] and rounded to 3 decimals."""
    raise NotImplementedError
