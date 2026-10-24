"""Checks how you worked with the agent, not just the result."""
import hashlib
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
TESTS_SHA = "0c24374c88830f29917bd00e461e6c8f3b65609f1a8b3a1afb5142091b4d4b42"


def test_12_1_plan_first():
    plan = HERE / "PLAN.md"
    assert plan.exists(), "ask your agent for a plan and save it as quests/day12/PLAN.md"
    bullets = [l for l in plan.read_text().splitlines() if l.strip().startswith("- ")]
    assert len(bullets) >= 3, f"PLAN.md needs at least 3 bullet points, found {len(bullets)}"


def test_12_3_tests_untouched():
    sha = hashlib.sha256((HERE / "test_textstats.py").read_bytes()).hexdigest()
    assert sha == TESTS_SHA, "test_textstats.py was changed. The agent has to fix the code, not the tests: git checkout quests/day12/test_textstats.py"


def test_12_3_small_commits():
    out = subprocess.run(["git", "log", "--format=%s", "--", str(HERE / "textstats.py")], capture_output=True, text=True, cwd=HERE).stdout
    yours = [s for s in out.splitlines() if not s.startswith("rynovi:")]
    assert len(yours) >= 2, f"commit your work on textstats.py in at least 2 steps (found {len(yours)} commit(s) of yours)"
