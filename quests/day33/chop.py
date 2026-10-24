"""Day 33 · Chop shop

RAG retrieves chunks, not documents, so how you cut decides what can be found.
You'll write two splitters, search with the keyword score in corpus.py, and measure hit rate:
the share of questions whose answer text is inside one of the top-k chunks.

Run `python quest.py 33` after each TODO.
"""
from quests.day33.corpus import HANDBOOK, QUESTIONS, score  # noqa: F401


def fixed_chunks(text: str, size: int = 200, overlap: int = 0) -> list[str]:
    """TODO 33.1 · Cut text into pieces of `size` characters. Each new piece starts `size - overlap`
    characters after the previous one. Drop pieces that are only whitespace."""
    raise NotImplementedError


def recursive_chunks(text: str, size: int = 400) -> list[str]:
    """TODO 33.2 · Split on paragraphs ("\\n\\n") first. A paragraph longer than `size` is split on ". "
    (keep the full stop on each sentence), and sentences are joined back while they fit in `size`.
    Strip each chunk and drop empty ones. Every chunk must be at most `size` characters."""
    raise NotImplementedError


def search(chunks: list[str], query: str, k: int = 3) -> list[str]:
    """TODO 33.3 · The k chunks with the highest score(query, chunk), best first.
    On ties, keep the original chunk order (sorted() is stable)."""
    raise NotImplementedError


def hit_rate(chunks: list[str], k: int = 3) -> float:
    """TODO 33.4 · For every (question, answer) in QUESTIONS, is the answer text inside any of
    search(chunks, question, k)? Return the share that hit (0 to 1)."""
    raise NotImplementedError
