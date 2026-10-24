from quests.day70.cdc import apply, replay

EVENTS = [
    {"lsn": 1, "op": "insert", "id": "c1", "row": {"name": "Riya", "city": "Pune"}},
    {"lsn": 2, "op": "insert", "id": "c2", "row": {"name": "Arjun", "city": "Delhi"}},
    {"lsn": 4, "op": "delete", "id": "c2"},
    {"lsn": 3, "op": "update", "id": "c1", "row": {"city": "Bengaluru"}},
    {"lsn": 2, "op": "insert", "id": "c2", "row": {"name": "Arjun", "city": "Delhi"}},
    {"lsn": 5, "op": "insert", "id": "c3", "row": {"name": "Meera", "city": "Chennai"}},
]


def test_70_1_apply():
    t = {}
    apply(t, EVENTS[0]); apply(t, EVENTS[3])
    assert t == {"c1": {"name": "Riya", "city": "Bengaluru"}}
    apply(t, {"lsn": 9, "op": "delete", "id": "nope"})


def test_70_2_replay_is_safe():
    table, last = replay(EVENTS)
    assert last == 5
    assert table == {"c1": {"name": "Riya", "city": "Bengaluru"}, "c3": {"name": "Meera", "city": "Chennai"}}
    again, last2 = replay(EVENTS + EVENTS)
    assert again == table and last2 == 5


def test_70_3_resume():
    first, last = replay(EVENTS[:2])
    snapshot = {k: dict(v) for k, v in first.items()}
    table, last = replay(EVENTS, first, last)
    assert first == snapshot, "don't modify the table you were given"
    assert table == {"c1": {"name": "Riya", "city": "Bengaluru"}, "c3": {"name": "Meera", "city": "Chennai"}}
