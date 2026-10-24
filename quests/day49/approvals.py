"""Day 49 · Approval gate

Some actions need a person to say yes first: emailing a customer, booking a visit, refunding money.
Your run pauses at a risky tool call, saves a checkpoint (JSON, so it could wait for hours in a database),
and resumes once someone approves, edits or rejects it.

Run `python quest.py 49` after each TODO.
"""
import json  # noqa: F401

RISKY = {"send_email", "book_visit", "refund"}


def needs_approval(call: dict) -> bool:
    """TODO 49.1 · True for risky tools, and also for ANY call whose input has "amount" over 5000."""
    raise NotImplementedError


def run(calls: list[dict], tools: dict, checkpoint: str | None = None) -> dict:
    """TODO 49.2 · Work through calls (each {"id", "name", "input"}) starting from the checkpoint.
    The checkpoint is a JSON string {"index": int, "results": [...], "decisions": {call_id: decision}}
    (start fresh with index 0, results [], decisions {} when it's None).

    For each call from index onwards:
      - needs approval and no decision yet: STOP and return
            {"status": "paused", "waiting_for": call["id"], "checkpoint": <json string of the current state>}
      - decision {"action": "approve"}: run it as is
      - decision {"action": "edit", "input": {...}}: run it with the new input
      - decision {"action": "reject"}: don't run it; its result is "rejected by a person"
      - no approval needed: run it
    A result is str(tools[name](**input)). When all calls are done return {"status": "done", "results": [...]}."""
    raise NotImplementedError


def decide(checkpoint: str, call_id: str, action: str, new_input: dict | None = None) -> str:
    """TODO 49.3 · Record a person's decision in the checkpoint and return the new JSON string.
    action is "approve", "edit" (with new_input) or "reject"."""
    raise NotImplementedError
