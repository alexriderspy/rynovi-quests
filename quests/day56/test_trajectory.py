import pytest

from quests.day56.runs import RUNS
from quests.day56.trajectory import report, success_rate, used_right_tools, wasted_steps


def test_56_1_success():
    assert success_rate(RUNS) == pytest.approx(16 / 20)


def test_56_2_right_tools():
    ok = {"run": "x", "expected_tools": ["a", "b", "c"], "steps": ["a", "z", "b", "c"]}
    wrong_order = {"run": "y", "expected_tools": ["a", "b"], "steps": ["b", "a"]}
    missing = {"run": "z", "expected_tools": ["a", "b"], "steps": ["a", "z"]}
    assert used_right_tools(ok) and not used_right_tools(wrong_order) and not used_right_tools(missing)


def test_56_3_waste_and_report():
    assert wasted_steps({"expected_tools": ["a"], "steps": ["a", "a", "a"]}) == 2
    assert wasted_steps({"expected_tools": ["a", "b"], "steps": ["a"]}) == 0
    rep = report(RUNS)
    assert rep["success"] == pytest.approx(0.8)
    assert rep["right_tools"] == pytest.approx(0.8)
    assert rep["wanderers"] == ["r02", "r07", "r12", "r17"]
    assert rep["avg_wasted"] == pytest.approx(1.0)
