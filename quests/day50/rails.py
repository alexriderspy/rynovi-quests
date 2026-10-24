"""Day 50 · Rails

Guardrails are plain code around the model: what goes in, what comes out, and how far a run can go.
Today: keep Indian personal data out of prompts and logs, stop runaway agents, and check drafts
before they reach a customer.

Run `python quest.py 50` after each TODO.
"""
import re  # noqa: F401


def redact(text: str) -> str:
    """TODO 50.1 · Replace personal data with placeholders:
      Aadhaar  12 digits, optionally in groups of 4 separated by spaces or hyphens   -> [AADHAAR]
      PAN      5 capital letters, 4 digits, 1 capital letter (ABCDE1234F)            -> [PAN]
      phone    an Indian mobile: optional +91 or 0, then 10 digits starting 6-9       -> [PHONE]
      email    something@something.something                                         -> [EMAIL]
    Do Aadhaar before phone, so a 12-digit number isn't half-eaten by the phone rule."""
    raise NotImplementedError


class BudgetExceeded(Exception):
    pass


class Budget:
    def __init__(self, max_steps: int = 10, max_cost_rs: float = 20.0):
        self.max_steps, self.max_cost_rs = max_steps, max_cost_rs
        self.steps, self.cost_rs = 0, 0.0

    def charge(self, cost_rs: float) -> None:
        """TODO 50.2 · Count one step and add its cost. If that takes steps over max_steps or cost over
        max_cost_rs, raise BudgetExceeded with a message saying which limit was hit ("steps" or "cost")."""
        raise NotImplementedError


BLOCKED_PHRASES = ["guarantee", "100% refund", "legal advice", "we promise"]


def check_draft(draft: str) -> list[str]:
    """TODO 50.3 · Problems with a draft reply before it goes to a customer:
      "contains personal data"   if redact() would change it
      "promises: <phrase>"       for each BLOCKED_PHRASES phrase in it (ignore case), in list order
    A clean draft gives []."""
    raise NotImplementedError
