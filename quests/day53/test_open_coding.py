from quests.day53.notes import NOTES
from quests.day53.open_coding import count_categories, examples, top_share


def test_53_1_counts():
    c = count_categories(NOTES)
    assert c == {"wrong policy cited": 12, "ignored the date": 8, "made up a number": 5, "too long": 3, "rude tone": 2}
    assert list(c) == ["wrong policy cited", "ignored the date", "made up a number", "too long", "rude tone"]


def test_53_2_where_to_focus():
    assert top_share(NOTES, 2) == 0.67
    assert top_share(NOTES, 1) == 0.4


def test_53_3_examples():
    ex = examples(NOTES, "rude tone", k=3)
    assert len(ex) == 2 and all(e.startswith("t") for e in ex)
    firsts = [n["trace"] for n in NOTES if n["category"] == "made up a number"][:3]
    assert examples(NOTES, "made up a number") == firsts
