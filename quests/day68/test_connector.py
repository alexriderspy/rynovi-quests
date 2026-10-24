from quests.day68.connector import fetch_all, to_index
from quests.day68.fake_api import FakeDrive


def test_68_1_all_pages():
    api = FakeDrive()
    files = fetch_all(api)
    assert [f["id"] for f in files] == [f"f{i}" for i in range(1, 12)]


def test_68_2_rate_limits():
    api = FakeDrive()
    fetch_all(api)
    assert api.waits >= 1, "this API rate-limits after 4 calls: you must wait() and retry"
    assert api.calls == 7, "6 pages plus one rate-limited call that you retried"


def test_68_3_index_with_permissions():
    idx = to_index(fetch_all(FakeDrive()))
    assert [d["id"] for d in idx] == ["f1", "f2", "f4", "f5", "f6", "f7", "f9", "f10", "f11"]
    assert idx[-1] == {"id": "f11", "title": "Offsite plan", "allowed": ["hr", "leadership"]}
