import pytest

from quests.day57.checks import ANSWERS, code_checks, judge_cost_saved, route


def test_57_1_code_checks():
    assert code_checks(ANSWERS[0]) == []
    assert code_checks(ANSWERS[1]) == ["bad citation"]
    assert code_checks(ANSWERS[2]) == ["no citation"]
    assert code_checks(ANSWERS[3]) == ["template text"]
    assert code_checks(ANSWERS[4]) == ["too long"]
    assert code_checks(ANSWERS[7]) == ["no citation", "template text"]


def test_57_2_route():
    assert route(ANSWERS) == {"failed_code_checks": ["q2", "q3", "q4", "q5", "q8"], "to_judge": ["q1", "q6", "q7"]}


def test_57_3_savings():
    assert judge_cost_saved(ANSWERS, 0.42) == pytest.approx(2.1)
