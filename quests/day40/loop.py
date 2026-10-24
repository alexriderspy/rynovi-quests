"""Day 40 · The loop

An agent is a model plus tools plus a loop. The model asks for a tool, your code runs it and sends the
result back, and this repeats until the model answers. Here the model is scripted (fake_model.py),
so you can focus on the loop.

Run `python quest.py 40` after each TODO.
"""
from dataclasses import dataclass, field
from typing import Callable

Tools = dict[str, Callable[..., object]]


@dataclass
class AgentResult:
    text: str
    messages: list[dict] = field(default_factory=list)
    steps: int = 0


def run_tool(tools: Tools, call: dict) -> dict:
    """TODO 40.1 · Run one tool call {"id", "name", "input"} and return a tool result:
        {"tool_use_id": call["id"], "content": str(result), "is_error": False}
    If the tool doesn't exist, or it raises, don't crash: return
        {"tool_use_id": call["id"], "content": "error: <what went wrong>", "is_error": True}
    (for a missing tool, the content must say "error: unknown tool <name>")."""
    raise NotImplementedError


def run_agent(model, tools: Tools, user_message: str, max_steps: int = 8) -> AgentResult:
    """TODO 40.2 · The loop. Start with messages = [{"role": "user", "content": user_message}].
    Each step: reply = model.reply(messages).
      - text reply: append {"role": "assistant", "content": reply["text"]} and return
        AgentResult(text, messages, steps) where steps is how many times you called the model.
      - tool_use reply: append {"role": "assistant", "content": [reply]}, run it with run_tool, then append
        {"role": "user", "content": [tool_result]}, and go round again.

    TODO 40.3 · Never loop forever: if the model still hasn't answered after max_steps calls,
    raise RuntimeError("step limit reached")."""
    raise NotImplementedError
