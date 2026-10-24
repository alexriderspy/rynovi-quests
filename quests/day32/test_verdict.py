import pytest

from quests.day32 import verdict as v


def test_32_1_accuracy():
    assert v.accuracy("baseline") == pytest.approx(31 / 36)
    assert v.accuracy("base") == pytest.approx(23 / 36)
    assert v.accuracy("finetune") == pytest.approx(32 / 36)


def test_32_2_f1_per_label():
    assert v.f1("baseline", "bug") == pytest.approx(0.9333, abs=1e-3)
    assert v.f1("base", "question") == pytest.approx(0.5, abs=1e-3)
    assert v.f1("finetune", "question") == pytest.approx(0.8333, abs=1e-3)


def test_32_2_f1_when_never_predicted():
    import quests.day32.data as d
    saved = list(d.ISSUES)
    d.ISSUES[:] = [{"title": "x", "label": "bug", "baseline": "feature", "base": "bug", "finetune": "bug"}]
    try:
        assert v.f1("baseline", "question") == 0.0
    finally:
        d.ISSUES[:] = saved


def test_32_3_macro_f1():
    assert v.macro_f1("baseline") == pytest.approx(0.8432, abs=1e-3)
    assert v.macro_f1("base") == pytest.approx(0.6302, abs=1e-3)
    assert v.macro_f1("finetune") == pytest.approx(0.8885, abs=1e-3)


def test_32_4_verdict():
    assert v.verdict() == "finetune"


def test_32_4_cheaper_wins_a_near_tie(monkeypatch):
    monkeypatch.setattr(v, "macro_f1", lambda m: {"baseline": 0.875, "base": 0.6, "finetune": 0.89}[m])
    assert v.verdict() == "baseline", "baseline is within 0.02 and much cheaper, so ship it"
