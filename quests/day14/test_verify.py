import pytest
from pydantic import ValidationError

from quests.day14.outputs import OUTPUTS
from quests.day14.verify import Invoice, Line, parse, problems, route


def test_14_1_schema():
    inv = Invoice(vendor="A", invoice_no="A-1", lines=[Line(description="x", qty="2", unit_price="9.5")], total=19)
    assert inv.lines[0].qty == 2 and inv.lines[0].unit_price == 9.5
    with pytest.raises(ValidationError):
        Line(description="x", qty=0, unit_price=1)
    with pytest.raises(ValidationError):
        Invoice(vendor="A", invoice_no="A-1", lines=[], total=-1)


def test_14_2_parses_good_replies():
    inv = parse(OUTPUTS[0])
    assert isinstance(inv, Invoice) and inv.invoice_no == "CP-101" and inv.lines[0].qty == 40


def test_14_2_rejects_broken_replies():
    assert parse(OUTPUTS[2]) is None, "text around the JSON isn't valid JSON"
    assert parse(OUTPUTS[5]) is None, "qty 'one' isn't a number"
    assert parse(OUTPUTS[7]) is None, "a negative total breaks the schema"
    assert parse(OUTPUTS[9]) is None, "qty 0 breaks the schema"


def test_14_3_checks_the_maths():
    assert problems(parse(OUTPUTS[0])) == []
    assert problems(parse(OUTPUTS[1])) == []
    assert problems(parse(OUTPUTS[3])) == ["total mismatch"]
    assert problems(parse(OUTPUTS[6])) == [], "349.5 x 18 = 6291.0, within 1 rupee of 6291.4"
    assert problems(parse(OUTPUTS[8])) == ["total mismatch"]


def test_14_3_empty_invoice():
    assert "no lines" in problems(parse(OUTPUTS[4]))


def test_14_4_routes_everything():
    assert route(OUTPUTS) == {
        "accepted": ["CP-101", "CD-7781", "ZM-31"],
        "review": ["reply 2", "OH-55", "BD-2", "reply 5", "reply 7", "AZ-77", "reply 9"],
    }
