import pytest

from quests.day63.dashboard import cost_per_task, costliest_step, percentile
from quests.day63.runs import RUNS


def test_63_1_percentiles():
    assert percentile([5, 1, 9, 3], 50) == 3
    assert percentile([5, 1, 9, 3], 95) == 9
    lat = [r["latency_ms"] for r in RUNS]
    assert percentile(lat, 50) == 4063
    assert percentile(lat, 95) == 6607


def test_63_2_cost_per_task():
    assert cost_per_task(RUNS) == {"classify_email": pytest.approx(0.059), "answer_question": pytest.approx(1.775), "book_visit": pytest.approx(2.226)}


def test_63_3_costliest_step():
    assert costliest_step(RUNS) == ("retrieve_and_answer", pytest.approx(223.31))
