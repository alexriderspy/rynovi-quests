"""Day 52 · Read the trace

A trace is the whole story of one run: every model call and tool call, with timings, tokens and errors.
quests/day52/trace.py has one run of the service copilot. Answer the three questions every on-call
engineer asks: what was slow, what did it cost, and what broke?

Run `python quest.py 52` after each TODO.
"""
from quests.day52.trace import PRICES, TRACE  # noqa: F401


def duration_ms(span: dict) -> int:
    return span["end_ms"] - span["start_ms"]


def slowest_step(trace: list[dict]) -> tuple[str, int]:
    """TODO 52.1 · The slowest span that isn't the root (the root has parent None): (name, duration in ms)."""
    raise NotImplementedError


def cost_rs(trace: list[dict]) -> float:
    """TODO 52.2 · Total cost of the run in rupees, rounded to 4 decimals. For every "llm" span:
        tokens_in / 1e6 * PRICES[model]["in"] + tokens_out / 1e6 * PRICES[model]["out"]"""
    raise NotImplementedError


def failures(trace: list[dict]) -> list[str]:
    """TODO 52.3 · For every span with an "error", a line "<name> failed under <parent's name>: <error>",
    in trace order."""
    raise NotImplementedError
