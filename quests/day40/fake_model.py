"""A pretend LLM that replies from a script, so the quest needs no API key. Don't edit this file.

Each reply is either
  {"type": "text", "text": "..."}                                   the final answer
  {"type": "tool_use", "id": "t1", "name": "...", "input": {...}}   a request to run a tool
It records every message list it was called with, so the tests can check what you sent back.
"""


class ScriptedModel:
    def __init__(self, replies: list[dict]):
        self.replies = list(replies)
        self.seen: list[list[dict]] = []

    def reply(self, messages: list[dict]) -> dict:
        self.seen.append([dict(m) for m in messages])
        if not self.replies:
            return {"type": "tool_use", "id": "loop", "name": "search", "input": {"q": "again"}}
        return self.replies.pop(0)
