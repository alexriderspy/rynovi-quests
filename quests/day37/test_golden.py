import json

import pytest

from quests.day37.golden import CATEGORIES, GOLDEN, GoldenCase, coverage, gaps, load_golden

GOOD = {"question": "How many sick days do I get?", "category": "leave", "expect": "answer", "must_include": ["12"], "source": "Leave policy"}


def write(tmp_path, rows):
    p = tmp_path / "g.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    return p


def test_37_1_schema():
    assert GoldenCase(**GOOD).category == "leave"
    for bad in [GOOD | {"category": "food"}, GOOD | {"question": "Sick?"}, GOOD | {"must_include": []},
                GOOD | {"source": None}, GOOD | {"expect": "refuse"}]:
        with pytest.raises(Exception):
            GoldenCase(**bad)
    assert GoldenCase(question="What is the CEO's salary?", category="out_of_scope", expect="refuse").must_include == []


def test_37_1_loader(tmp_path):
    assert len(load_golden(write(tmp_path, [GOOD, GOOD | {"question": "How many paid leave days a year?"}]))) == 2
    with pytest.raises(ValueError, match="line 2"):
        load_golden(write(tmp_path, [GOOD, GOOD | {"category": "food"}]))


def test_37_2_coverage_and_gaps():
    cases = [GoldenCase(**GOOD), GoldenCase(**GOOD | {"question": "How long is parental leave?"})]
    cov = coverage(cases)
    assert cov == {c: (2 if c == "leave" else 0) for c in CATEGORIES}
    assert gaps(cases, 2) == ["wfh", "expenses", "learning", "security", "out_of_scope"]


def test_37_3_your_golden_set_is_good_enough():
    cases = load_golden(GOLDEN)
    assert len(cases) >= 30, f"{len(cases)} cases so far; grow golden.jsonl to at least 30"
    assert gaps(cases, 3) == [], f"categories with fewer than 3 cases: {gaps(cases, 3)}"
    refusals = sum(c.expect == "refuse" for c in cases)
    assert refusals >= 5, f"only {refusals} refuse cases; add questions the handbook can't answer"
    qs = [c.question.strip().lower() for c in cases]
    assert len(qs) == len(set(qs)), "some questions appear twice"
