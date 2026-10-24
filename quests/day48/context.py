"""Day 48 · Context budget

Long agent runs fill the context with old tool outputs until the model loses the plot.
You'll keep a 30-step run under a token budget: pinned facts always stay, recent steps stay,
and everything older gets squashed into one summary.

Tokens are words here: len(content.split()). summarise() is a stand-in for a cheap model call.
Run `python quest.py 48` after each TODO.
"""


def tokens(messages: list[dict]) -> int:
    return sum(len(str(m["content"]).split()) for m in messages)


def summarise(messages: list[dict]) -> str:
    """Pretend summary: the first 3 words of each message. Don't edit."""
    return " / ".join(" ".join(str(m["content"]).split()[:3]) for m in messages)


def split(messages: list[dict], keep_last: int = 4) -> tuple[list[dict], list[dict], list[dict]]:
    """TODO 48.1 · Split into (keep, old, recent):
      keep    the first message if it's a system message, plus every message with "pinned": True
      recent  the last `keep_last` messages that aren't in keep
      old     everything else, in order"""
    raise NotImplementedError


def compress(messages: list[dict], budget: int, keep_last: int = 4) -> list[dict]:
    """TODO 48.2 · If tokens(messages) <= budget, return them unchanged.
    Otherwise return keep + [summary] + recent, where summary is
        {"role": "user", "content": "Summary of earlier steps: " + summarise(old)}
    If that's STILL over budget, drop the summary. (Pinned and recent messages always stay.)"""
    raise NotImplementedError


def run_with_budget(steps: list[dict], budget: int, start: list[dict]) -> tuple[list[dict], int]:
    """TODO 48.3 · Simulate a long run: begin with `start`, then for each step append it and compress.
    Return (final messages, the largest token count the context ever had AFTER compressing)."""
    raise NotImplementedError
