"""Day 69 · Fresh index

Re-embedding everything every night is slow and costly. Sync the index with its source instead:
embed new documents, re-embed changed ones, delete removed ones, and leave the rest alone.
The index stores, per document id: {"hash": <content hash>, "vector": <embedding>}.

Run `python quest.py 69` after each TODO.
"""
import hashlib  # noqa: F401
from typing import Callable


def content_hash(text: str) -> str:
    """TODO 69.1 · sha256 of the UTF-8 text, as a hex string."""
    raise NotImplementedError


def plan_sync(source: dict[str, str], index: dict[str, dict]) -> dict:
    """TODO 69.2 · Compare source {id: text} with the index. Return
        {"add": ids in source but not index, "update": ids whose hash changed,
         "delete": ids in index but not source, "unchanged": how many need nothing}
    with every id list sorted."""
    raise NotImplementedError


def apply_sync(source: dict[str, str], index: dict[str, dict], embed: Callable[[str], list[float]]) -> int:
    """TODO 69.3 · Carry out the plan on `index` in place: embed() only for add and update, store the new hash
    and vector, delete removed ids. Return how many times you called embed."""
    raise NotImplementedError
