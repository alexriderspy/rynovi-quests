from quests.day36.cases import CASES
from quests.day36.sources import REFUSAL, citation_problems, cited_ids, final_answer, should_refuse


def test_36_1_cited_ids():
    assert cited_ids("A [1] and B [3], again [1].") == [1, 3]
    assert cited_ids("No sources here.") == []


def test_36_2_problems():
    assert citation_problems(CASES[0]["answer"], CASES[0]["sources"]) == []
    assert citation_problems(CASES[1]["answer"], CASES[1]["sources"]) == ["missing source 3"]
    assert citation_problems(CASES[4]["answer"], CASES[4]["sources"]) == ["no citations"]
    assert citation_problems(CASES[2]["answer"], CASES[2]["sources"]) == []


def test_36_3_refuse_on_weak_retrieval():
    assert should_refuse(CASES[3]["sources"]) is True
    assert should_refuse(CASES[0]["sources"]) is False
    assert should_refuse([]) is True


def test_36_4_what_users_see():
    shown = [final_answer(c) for c in CASES]
    assert shown == [CASES[0]["answer"], REFUSAL, CASES[2]["answer"], REFUSAL, REFUSAL, CASES[5]["answer"]]
