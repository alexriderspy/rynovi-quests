"""Day 42 · State vs memory

Two different things:
  state    facts this run depends on (the customer id, the order id, whether it's approved).
           Keep them in a structured object, not buried in chat text.
  history  the messages so far. It grows every step, so you trim it to fit the context window.

Tokens here are just words (len(text.split())), to keep it simple.
Run `python quest.py 42` after each TODO.
"""
from dataclasses import dataclass, field


@dataclass
class SupportState:
    customer_id: str | None = None
    order_id: str | None = None
    approved: bool = False
    notes: list[str] = field(default_factory=list)


def update_state(state: SupportState, tool_result: dict) -> SupportState:
    """TODO 42.1 · Copy customer_id, order_id and approved from a tool result into the state,
    but only the keys that are present (a result without order_id must not wipe the one you have).
    If the result has a "note", append it to notes. Return the same state object."""
    raise NotImplementedError


def tokens(message: dict) -> int:
    return len(str(message["content"]).split())


def trim_history(messages: list[dict], budget: int) -> list[dict]:
    """TODO 42.2 · Keep the conversation within `budget` tokens:
      - a first message with role "system" is always kept
      - then keep the MOST RECENT messages that still fit, whole messages only, in their original order
    Return a new list."""
    raise NotImplementedError


def build_context(state: SupportState, messages: list[dict], budget: int) -> list[dict]:
    """TODO 42.3 · State must survive trimming. Return
        [{"role": "system", "content": "state: customer_id=<..>, order_id=<..>, approved=<..>"}]
    followed by trim_history(messages, budget - tokens(that system message))."""
    raise NotImplementedError
