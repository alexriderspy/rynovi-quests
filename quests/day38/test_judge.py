import pytest

from quests.day38.judge import agreement, confusion, pick_judge, tnr, tpr


def test_38_1_confusion():
    assert confusion("judge_v1") == {"tp": 25, "fp": 4, "tn": 1, "fn": 0}
    assert confusion("judge_v2") == {"tp": 23, "fp": 1, "tn": 4, "fn": 2}


def test_38_2_agreement_looks_fine_for_both():
    assert agreement("judge_v1") == pytest.approx(26 / 30)
    assert agreement("judge_v2") == pytest.approx(27 / 30)


def test_38_3_rates_tell_the_truth():
    assert tpr("judge_v1") == pytest.approx(1.0)
    assert tnr("judge_v1") == pytest.approx(0.2), "v1 catches only 1 of your 5 failures"
    assert tpr("judge_v2") == pytest.approx(23 / 25)
    assert tnr("judge_v2") == pytest.approx(0.8)


def test_38_4_pick():
    assert pick_judge() == "judge_v2"
