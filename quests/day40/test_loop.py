import pytest

from quests.day40.fake_model import ScriptedModel
from quests.day40.loop import run_agent, run_tool

TOOLS = {"weather": lambda city: f"32°C and sunny in {city}", "add": lambda a, b: a + b, "boom": lambda: 1 / 0}


def test_40_1_runs_a_tool():
    out = run_tool(TOOLS, {"id": "t1", "name": "add", "input": {"a": 2, "b": 3}})
    assert out == {"tool_use_id": "t1", "content": "5", "is_error": False}


def test_40_1_errors_dont_crash():
    out = run_tool(TOOLS, {"id": "t2", "name": "fly", "input": {}})
    assert out["is_error"] is True and out["content"] == "error: unknown tool fly"
    out = run_tool(TOOLS, {"id": "t3", "name": "boom", "input": {}})
    assert out["is_error"] is True and out["content"].startswith("error:")


def test_40_2_answers_directly():
    res = run_agent(ScriptedModel([{"type": "text", "text": "Hi!"}]), TOOLS, "hello")
    assert res.text == "Hi!" and res.steps == 1
    assert res.messages == [{"role": "user", "content": "hello"}, {"role": "assistant", "content": "Hi!"}]


def test_40_2_uses_tools_then_answers():
    model = ScriptedModel([
        {"type": "tool_use", "id": "t1", "name": "weather", "input": {"city": "Pune"}},
        {"type": "tool_use", "id": "t2", "name": "add", "input": {"a": 32, "b": 1}},
        {"type": "text", "text": "Pune is 32°C. Tomorrow 33°C."},
    ])
    res = run_agent(model, TOOLS, "Weather in Pune?")
    assert res.steps == 3 and res.text.startswith("Pune is 32")
    assert len(res.messages) == 6
    second_call = model.seen[1]
    assert second_call[-1] == {"role": "user", "content": [{"tool_use_id": "t1", "content": "32°C and sunny in Pune", "is_error": False}]}


def test_40_3_step_limit():
    model = ScriptedModel([])  # keeps asking for tools forever
    with pytest.raises(RuntimeError, match="step limit"):
        run_agent(model, {"search": lambda q: "nothing"}, "find it", max_steps=5)
    assert len(model.seen) == 5
