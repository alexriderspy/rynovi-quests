from quests.day54.grow import add_cases, bump_version, normalise

GOLDEN = [
    {"id": "g1", "input": "How many casual leaves do interns get?", "expect": "8", "category": "leave"},
    {"id": "g2", "input": "Hotel limit in metro cities?", "expect": "6,000", "category": "expenses"},
]
NEW = [
    {"id": "n1", "input": "how many CASUAL leaves do interns get", "expect": "8", "category": "leave"},
    {"id": "n2", "input": "Is public Wi-Fi allowed without VPN?", "expect": "no", "category": "security"},
    {"id": "n3", "input": "Is public wi-fi allowed   without VPN", "expect": "no", "category": "security"},
    {"id": "n4", "input": "What's the CEO's salary?", "expect": "refuse", "category": "out_of_scope"},
]


def test_54_1_normalise():
    assert normalise("  How many CASUAL leaves, do interns get?? ") == "how many casual leaves do interns get"
    assert normalise("Wi-Fi") == "wifi"


def test_54_2_add_cases():
    grown, skipped = add_cases(GOLDEN, NEW)
    assert [c["id"] for c in grown] == ["g1", "g2", "n2", "n4"]
    assert skipped == ["n1", "n3"]
    assert GOLDEN[0] in grown and len(GOLDEN) == 2, "don't change the original list"


def test_54_3_versions():
    grown, _ = add_cases(GOLDEN, NEW)
    assert bump_version("v3", GOLDEN, grown) == "v4"
    assert bump_version("v9", GOLDEN, list(GOLDEN)) == "v9"
    assert bump_version("v12", GOLDEN, grown) == "v13"
