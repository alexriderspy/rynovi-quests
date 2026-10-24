from langgraph.checkpoint.memory import InMemorySaver

from quests.day44.graph import build_graph, chat, classify, math


def test_44_1_nodes():
    assert classify({"question": "add 2 and 40"}) == {"route": "math", "steps": ["classify"]}
    assert classify({"question": "hello there"})["route"] == "chat"
    assert math({"question": "add 2 and 40"}) == {"answer": "42", "steps": ["math"]}
    assert chat({"question": "why is the sky blue"})["answer"] == "Let me think about: why is the sky blue"


def test_44_2_routes_through_the_graph():
    g = build_graph()
    out = g.invoke({"question": "what is 10 plus 5 plus 1"})
    assert out["answer"] == "16" and out["steps"] == ["classify", "math"]
    out = g.invoke({"question": "tell me about agents"})
    assert out["steps"] == ["classify", "chat"]


def test_44_3_pause_and_resume_from_a_checkpoint():
    g = build_graph(checkpointer=InMemorySaver(), interrupt_before=["math"])
    cfg = {"configurable": {"thread_id": "riya-1"}}
    first = g.invoke({"question": "add 20 and 22"}, cfg)
    assert "answer" not in first, "the run should pause before the math node"
    assert g.get_state(cfg).next == ("math",)
    done = g.invoke(None, cfg)  # resume from the checkpoint
    assert done["answer"] == "42" and done["steps"] == ["classify", "math"]
