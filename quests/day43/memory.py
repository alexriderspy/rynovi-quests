"""Day 43 · Remember me

Long-term memory: facts about a user that survive across sessions. The hard parts are saving the
right things, recalling only what's relevant, and replacing facts that changed (people move cities).

Run `python quest.py 43` after each TODO.
"""
import re  # noqa: F401


class MemoryStore:
    def __init__(self) -> None:
        self.facts: dict[tuple[str, str], str] = {}  # (user, key) -> value

    def remember(self, user: str, key: str, value: str) -> None:
        """TODO 43.1 · Save a fact. Saving the same (user, key) again REPLACES the old value."""
        raise NotImplementedError

    def get(self, user: str, key: str) -> str | None:
        """TODO 43.1 · The value, or None."""
        raise NotImplementedError

    def forget(self, user: str, key: str) -> None:
        """TODO 43.1 · Remove a fact (the user asked you to). Forgetting something unknown is fine."""
        raise NotImplementedError

    def recall(self, user: str, query: str, k: int = 3) -> list[str]:
        """TODO 43.2 · The user's most relevant facts for a query, as "key: value" strings.
        Score = how many lowercase words of the query appear in "key value". Leave out score 0.
        Highest score first; ties in the order the facts were first saved. Only this user's facts."""
        raise NotImplementedError

    def extract(self, user: str, message: str) -> list[tuple[str, str]]:
        """TODO 43.3 · Pull facts out of a message and remember them. Patterns (case-insensitive):
            "my name is X"   -> ("name", X)
            "i live in X"    -> ("city", X)
            "i work at X"    -> ("employer", X)
            "i prefer X"     -> ("preference", X)
        X runs until a full stop, comma or the end of the message, stripped.
        Return the (key, value) pairs found, in the order above."""
        raise NotImplementedError
