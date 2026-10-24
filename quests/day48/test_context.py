from quests.day48.context import compress, run_with_budget, split, tokens

SYSTEM = {"role": "system", "content": "You are a research agent."}
PIN = {"role": "user", "content": "Remember: the report is due Friday for Ananya.", "pinned": True}
STEPS = [{"role": "user" if i % 2 else "assistant", "content": f"step {i} " + "result text " * 6} for i in range(30)]


def test_48_1_split():
    msgs = [SYSTEM, PIN] + STEPS[:8]
    keep, old, recent = split(msgs, keep_last=4)
    assert keep == [SYSTEM, PIN]
    assert recent == STEPS[4:8]
    assert old == STEPS[:4]


def test_48_2_compress():
    msgs = [SYSTEM, PIN] + STEPS[:10]
    assert compress(msgs, budget=10_000) == msgs
    out = compress(msgs, budget=100)
    assert out[:2] == [SYSTEM, PIN] and out[-4:] == STEPS[6:10]
    assert out[2]["content"].startswith("Summary of earlier steps: step 0 result")
    assert tokens(out) <= 100


def test_48_2_drops_summary_if_needed():
    msgs = [SYSTEM, PIN] + STEPS[:10]
    out = compress(msgs, budget=75)
    assert out == [SYSTEM, PIN] + STEPS[6:10]


def test_48_3_thirty_steps_under_budget():
    final, peak = run_with_budget(STEPS, budget=90, start=[SYSTEM, PIN])
    assert peak <= 90, f"context hit {peak} tokens; the budget is 90"
    assert PIN in final, "the pinned fact must survive all 30 steps"
    assert final[-1] == STEPS[-1]
