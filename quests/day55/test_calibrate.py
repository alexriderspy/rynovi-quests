import pytest

from quests.day55.calibrate import corrected_pass_rate, holds_up, rates
from quests.day55.data import LABELLED


def test_55_1_rates():
    dev = [r for r in LABELLED if r["split"] == "dev"]
    tpr, tnr = rates(dev)
    assert tpr == pytest.approx(0.9) and tnr == pytest.approx(0.85)


def test_55_2_holds_up():
    assert holds_up(0.75) is True
    assert holds_up(0.85) is False


def test_55_3_corrected_rate():
    assert corrected_pass_rate() == pytest.approx(0.667, abs=1e-3)
