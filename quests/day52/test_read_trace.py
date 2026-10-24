import pytest

from quests.day52.read_trace import cost_rs, failures, slowest_step
from quests.day52.trace import TRACE


def test_52_1_slowest_step():
    assert slowest_step(TRACE) == ("draft_reply", 5250)


def test_52_2_cost():
    assert cost_rs(TRACE) == pytest.approx(4.5544, abs=1e-4)


def test_52_3_failures():
    assert failures(TRACE) == ["lookup_order failed under plan: 404 order not found"]
