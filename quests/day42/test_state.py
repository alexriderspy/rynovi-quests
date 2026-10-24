from quests.day42.state import SupportState, build_context, tokens, trim_history, update_state

CHAT = [
    {"role": "system", "content": "You are a support agent."},
    {"role": "user", "content": "Hi, my order ORD-1042 never arrived and I am upset"},
    {"role": "assistant", "content": "Sorry about that, let me check"},
    {"role": "user", "content": "It was a birthday gift for my sister"},
    {"role": "assistant", "content": "I understand, checking the courier now"},
    {"role": "user", "content": "Please hurry"},
]


def test_42_1_update_state():
    s = SupportState()
    update_state(s, {"customer_id": "C-77", "order_id": "ORD-1042"})
    update_state(s, {"status": "lost", "note": "courier lost it"})
    assert s.customer_id == "C-77" and s.order_id == "ORD-1042", "a result without ids must not wipe them"
    assert s.notes == ["courier lost it"] and s.approved is False
    update_state(s, {"approved": True})
    assert s.approved is True


def test_42_2_trim_keeps_system_and_recent():
    out = trim_history(CHAT, budget=20)
    assert out[0] == CHAT[0]
    assert out[-1] == CHAT[-1]
    assert sum(tokens(m) for m in out) <= 20
    assert out == [CHAT[0], CHAT[3], CHAT[4], CHAT[5]]


def test_42_2_whole_history_when_it_fits():
    assert trim_history(CHAT, budget=1000) == CHAT
    assert trim_history(CHAT, budget=1000) is not CHAT


def test_42_3_state_survives_trimming():
    s = SupportState(customer_id="C-77", order_id="ORD-1042")
    ctx = build_context(s, CHAT[1:], budget=20)
    assert ctx[0] == {"role": "system", "content": "state: customer_id=C-77, order_id=ORD-1042, approved=False"}
    assert not any("ORD-1042" in str(m["content"]) for m in ctx[1:]), "the old message was trimmed..."
    assert "ORD-1042" in ctx[0]["content"], "...but the order id survives in state"
    assert sum(tokens(m) for m in ctx) <= 20
