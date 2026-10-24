import shutil
from pathlib import Path

from quests.day71.scan import clean, find_pii, scan

WORKSPACE = Path(__file__).parent / "workspace"


def test_71_1_find():
    assert find_pii("mail riya@example.com or call 9876543210") == ["email", "phone"]
    assert find_pii("order ORD-1042 for Rs 1200") == []


def test_71_2_scan():
    assert scan(WORKSPACE) == {
        "evals/golden.jsonl": ["pan"],
        "logs/app.log": ["email", "phone"],
        "traces/run-17.json": ["aadhaar"],
    }


def test_71_3_clean(tmp_path):
    work = tmp_path / "ws"
    shutil.copytree(WORKSPACE, work)
    assert clean(work) == 3
    assert scan(work) == {}
    text = (work / "logs" / "app.log").read_text()
    assert "[EMAIL]" in text and "[PHONE]" in text and "ORD-1042" in text
    assert (work / "logs" / "worker.log").read_text() == (WORKSPACE / "logs" / "worker.log").read_text()
