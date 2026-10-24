import pytest

from quests.day35.fusion import hit_at_k, report, rrf


def test_35_1_rrf():
    fused = rrf([["a", "b", "c"], ["c", "b", "d"]], k=60)
    assert set(fused[:2]) == {"b", "c"}, "b and c appear in both lists, so they beat a and d"
    assert fused[:2] == ["c", "b"], "c is 1st and 3rd (1/61 + 1/63), just ahead of b, 2nd twice (2/62)"
    assert set(fused) == {"a", "b", "c", "d"}
    assert rrf([["x", "y"]]) == ["x", "y"]


def test_35_1_rrf_scores():
    assert rrf([["a", "b"], ["b", "a"]], k=1) == ["a", "b"], "a tie keeps the first one seen"


def test_35_2_hit_rates():
    assert hit_at_k("bm25", 3) == pytest.approx(0.5)
    assert hit_at_k("dense", 3) == pytest.approx(0.5)
    assert hit_at_k("hybrid", 3) == pytest.approx(1.0)


def test_35_3_report():
    r = report(3)
    assert set(r) == {"bm25", "dense", "hybrid"}
    assert r["hybrid"] > max(r["bm25"], r["dense"])
