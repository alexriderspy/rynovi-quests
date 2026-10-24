from pathlib import Path

import pytest

from quests.day51.privilege import allowed, lethal_trifecta, safe_path


def test_51_1_allow_list():
    assert allowed("support_agent", "draft_reply")
    assert not allowed("support_agent", "refund")
    assert not allowed("intern_bot", "read_ticket")


def test_51_2_folder_sandbox(tmp_path):
    root = tmp_path / "workspace"
    (root / "notes").mkdir(parents=True)
    assert safe_path(root, "notes/a.txt") == (root / "notes" / "a.txt").resolve()
    for bad in ["../secrets.txt", "notes/../../x", "/etc/passwd"]:
        with pytest.raises(PermissionError):
            safe_path(root, bad)


def test_51_3_lethal_trifecta():
    inbox = {"name": "read_inbox", "untrusted_content": True, "private_data": True}
    web = {"name": "fetch_url", "untrusted_content": True, "external_comms": True}
    kb = {"name": "search_kb", "private_data": True}
    assert lethal_trifecta([inbox, web]) == ["private_data", "untrusted_content", "external_comms"]
    assert lethal_trifecta([inbox, kb]) == []
