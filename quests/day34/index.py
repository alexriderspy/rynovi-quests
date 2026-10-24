"""Day 34 · Nearest neighbours

A vector database, in miniature. Every chunk is stored as a vector plus metadata.
Search finds the stored vectors closest to the query by cosine similarity.

Use NumPy. Run `python quest.py 34` after each TODO.
"""
import numpy as np  # noqa: F401


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    """TODO 34.1 · Cosine similarity: dot(a, b) / (|a| · |b|). 1 means same direction, 0 means unrelated."""
    raise NotImplementedError


class VectorIndex:
    def __init__(self) -> None:
        self.ids: list[str] = []
        self.vectors: list[np.ndarray] = []
        self.meta: list[dict] = []

    def add(self, id: str, vector, meta: dict | None = None) -> None:
        """TODO 34.2 · Store the id, the vector (as a float NumPy array, divided by its length so it has length 1)
        and the metadata (an empty dict if None). Adding an id that already exists replaces it."""
        raise NotImplementedError

    def search(self, query, k: int = 3, where: dict | None = None) -> list[tuple[str, float]]:
        """TODO 34.2 · Return the k best (id, score) pairs, highest cosine first. Because stored vectors
        have length 1, the score is just the dot product with the normalised query.

        TODO 34.3 · `where` filters by metadata BEFORE ranking: {"dept": "hr"} keeps only items whose
        meta["dept"] == "hr". Every key in `where` must match."""
        raise NotImplementedError

    def delete(self, id: str) -> None:
        """TODO 34.4 · Remove an item so it never shows up in search again. Deleting a missing id raises KeyError."""
        raise NotImplementedError
