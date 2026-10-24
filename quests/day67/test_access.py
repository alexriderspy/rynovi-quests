from quests.day67.access import DOCS, AuditLog, can_read, search


def test_67_1_can_read():
    assert can_read("riya", DOCS[3]) and can_read("arjun", DOCS[1])
    assert not can_read("arjun", DOCS[0]) and not can_read("stranger", DOCS[1])


def test_67_2_search_respects_permissions():
    assert search("meera", "salary bands budget") == ["d1"], "meera may see d1, not the board notes"
    assert search("arjun", "salary bands") == []
    assert search("riya", "vpn outage") == ["d4", "d3"]
    assert search("arjun", "vpn outage") == ["d3"]


def test_67_3_audit_log():
    log = AuditLog()
    log.search("riya", "vpn outage")
    log.search("arjun", "vpn setup")
    log.search("riya", "vpn guide")
    assert log.entries[0] == {"user": "riya", "query": "vpn outage", "doc_ids": ["d4", "d3"]}
    assert log.who_saw("d3") == ["riya", "arjun"]
    assert log.who_saw("d1") == []
    assert "text" not in str(log.entries[0].keys())
