"""Day 67 · Who sees what

In a company, the assistant must only ever see what the person asking may see. Filter BEFORE ranking,
never after, and log every access (who asked, and which documents were used: never the document text).

Run `python quest.py 67` after each TODO.
"""
import re  # noqa: F401

DOCS = [
    {"id": "d1", "text": "Salary bands for 2026 engineering levels", "roles": {"hr", "leadership"}},
    {"id": "d2", "text": "Leave policy: 24 days paid leave for everyone", "roles": {"everyone"}},
    {"id": "d3", "text": "VPN setup guide for laptops", "roles": {"everyone"}},
    {"id": "d4", "text": "Incident report: VPN outage root cause", "roles": {"it"}},
    {"id": "d5", "text": "Board meeting notes on salary budgets", "roles": {"leadership"}},
]
USERS = {"riya": {"everyone", "it"}, "arjun": {"everyone"}, "meera": {"everyone", "hr"}}


def can_read(user: str, doc: dict) -> bool:
    """TODO 67.1 · True if the user has any of the doc's roles. Unknown users can read nothing."""
    raise NotImplementedError


def search(user: str, query: str, k: int = 2) -> list[str]:
    """TODO 67.2 · Ids of the k best docs THIS user can read. Score = number of lowercase query words found in
    the doc's lowercase text. Drop score 0. Highest first; ties keep DOCS order. Filter before you rank."""
    raise NotImplementedError


class AuditLog:
    def __init__(self) -> None:
        self.entries: list[dict] = []

    def search(self, user: str, query: str, k: int = 2) -> list[str]:
        """TODO 67.3 · Run search() and append {"user", "query", "doc_ids"} to entries. Return the ids."""
        raise NotImplementedError

    def who_saw(self, doc_id: str) -> list[str]:
        """TODO 67.3 · Users who were ever given this doc, in first-seen order, no repeats."""
        raise NotImplementedError
