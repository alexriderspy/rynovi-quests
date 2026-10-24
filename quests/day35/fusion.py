"""Day 35 · Best of both

Keyword search (BM25) nails exact things like "XJ-204". Embedding search nails paraphrases like
"get my money back". quests/day35/rankings.py has both rankings for 10 queries. Fuse them.

Run `python quest.py 35` after each TODO.
"""
from quests.day35.rankings import QUERIES  # noqa: F401


def rrf(rankings: list[list[str]], k: int = 60) -> list[str]:
    """TODO 35.1 · Reciprocal rank fusion. A document at position p (1 = top) in a ranking earns 1 / (k + p).
    Add up its points across all rankings and return every document, highest total first.
    On ties, the document seen first (scanning the rankings in order) comes first."""
    raise NotImplementedError


def hit_at_k(source: str, k: int = 3) -> float:
    """TODO 35.2 · source is "bm25", "dense" or "hybrid". For each query, take that ranking
    (for "hybrid": rrf([bm25, dense])) and check if the relevant document is in the top k.
    Return the share of queries that hit."""
    raise NotImplementedError


def report(k: int = 3) -> dict[str, float]:
    """TODO 35.3 · {"bm25": ..., "dense": ..., "hybrid": ...} hit rates at k, so you can see the win."""
    raise NotImplementedError
