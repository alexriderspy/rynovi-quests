import hashlib

from quests.day69.sync import apply_sync, content_hash, plan_sync


def h(t):
    return hashlib.sha256(t.encode()).hexdigest()


SOURCE = {"a": "leave policy v2", "b": "vpn guide", "d": "new travel policy"}
INDEX = {"a": {"hash": h("leave policy v1"), "vector": [0.1]}, "b": {"hash": h("vpn guide"), "vector": [0.2]}, "c": {"hash": h("old draft"), "vector": [0.3]}}


def test_69_1_hash():
    assert content_hash("vpn guide") == h("vpn guide")


def test_69_2_plan():
    assert plan_sync(SOURCE, INDEX) == {"add": ["d"], "update": ["a"], "delete": ["c"], "unchanged": 1}


def test_69_3_apply_only_what_changed():
    index = {k: dict(v) for k, v in INDEX.items()}
    calls = []
    n = apply_sync(SOURCE, index, lambda t: calls.append(t) or [len(t)])
    assert n == 2 and sorted(calls) == ["leave policy v2", "new travel policy"]
    assert set(index) == {"a", "b", "d"}
    assert index["a"]["hash"] == h("leave policy v2") and index["b"]["vector"] == [0.2]
    assert plan_sync(SOURCE, index)["unchanged"] == 3
