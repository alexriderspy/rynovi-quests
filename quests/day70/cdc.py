"""Day 70 · Change data capture

Instead of copying a whole table every hour, read the stream of changes. Each event has a log sequence
number (lsn) that only goes up:
    {"lsn": 7, "op": "insert" | "update" | "delete", "id": "c1", "row": {...}}   (no "row" for delete)
Streams repeat events after a retry and can arrive slightly out of order, so replay must be safe.

Run `python quest.py 70` after each TODO.
"""


def apply(table: dict[str, dict], event: dict) -> None:
    """TODO 70.1 · insert/update put event["row"] at event["id"] (update merges into the existing row);
    delete removes it (deleting a missing id is fine)."""
    raise NotImplementedError


def replay(events: list[dict], table: dict | None = None, last_lsn: int = 0) -> tuple[dict, int]:
    """TODO 70.2 · Apply events in lsn order, skipping any with lsn <= the last applied lsn (so repeats and
    already-applied events do nothing). Return (table, last applied lsn).

    TODO 70.3 · Start from an existing table and last_lsn when given, so a crashed sync can resume.
    Don't modify the table that was passed in: work on a copy."""
    raise NotImplementedError
