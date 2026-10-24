import json

from quests.day49.approvals import decide, needs_approval, run

TOOLS = {
    "lookup": lambda order_id: f"{order_id}: lost by courier",
    "refund": lambda order_id, amount: f"refunded Rs {amount} for {order_id}",
    "send_email": lambda to, body: f"emailed {to}: {body}",
}
CALLS = [
    {"id": "c1", "name": "lookup", "input": {"order_id": "ORD-1042"}},
    {"id": "c2", "name": "refund", "input": {"order_id": "ORD-1042", "amount": 1200}},
    {"id": "c3", "name": "send_email", "input": {"to": "riya@example.com", "body": "Refund done!!"}},
]


def test_49_1_what_needs_approval():
    assert needs_approval(CALLS[1]) and needs_approval(CALLS[2])
    assert not needs_approval(CALLS[0])
    assert needs_approval({"id": "x", "name": "lookup", "input": {"amount": 9000}})


def test_49_2_pauses_at_risky_calls():
    out = run(CALLS, TOOLS)
    assert out["status"] == "paused" and out["waiting_for"] == "c2"
    cp = json.loads(out["checkpoint"])
    assert cp["index"] == 1 and cp["results"] == ["ORD-1042: lost by courier"]


def test_49_3_approve_edit_reject_and_resume():
    cp = run(CALLS, TOOLS)["checkpoint"]
    cp = decide(cp, "c2", "approve")
    out = run(CALLS, TOOLS, cp)
    assert out["status"] == "paused" and out["waiting_for"] == "c3"
    cp = decide(out["checkpoint"], "c3", "edit", {"to": "riya@example.com", "body": "Your refund of Rs 1,200 is on its way."})
    done = run(CALLS, TOOLS, cp)
    assert done == {"status": "done", "results": [
        "ORD-1042: lost by courier", "refunded Rs 1200 for ORD-1042", "emailed riya@example.com: Your refund of Rs 1,200 is on its way."]}


def test_49_3_reject():
    cp = decide(run(CALLS[:2], TOOLS)["checkpoint"], "c2", "reject")
    assert run(CALLS[:2], TOOLS, cp)["results"][-1] == "rejected by a person"
