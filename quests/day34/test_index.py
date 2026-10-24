import numpy as np
import pytest

from quests.day34.index import VectorIndex, cosine

DOCS = {
    "leave": ([0.9, 0.1, 0.0], {"dept": "hr", "year": 2026}),
    "payroll": ([0.7, 0.6, 0.1], {"dept": "hr", "year": 2025}),
    "vpn": ([0.0, 0.2, 0.95], {"dept": "it", "year": 2026}),
    "laptop": ([0.1, 0.3, 0.8], {"dept": "it", "year": 2025}),
    "travel": ([0.3, 0.9, 0.2], {"dept": "finance", "year": 2026}),
}


@pytest.fixture
def index():
    ix = VectorIndex()
    for i, (v, m) in DOCS.items():
        ix.add(i, v, m)
    return ix


def test_34_1_cosine():
    assert cosine(np.array([1, 0]), np.array([2, 0])) == pytest.approx(1.0)
    assert cosine(np.array([1, 0]), np.array([0, 3])) == pytest.approx(0.0)
    assert cosine(np.array([1, 1]), np.array([-1, -1])) == pytest.approx(-1.0)


def test_34_2_search_ranks_by_similarity(index):
    hits = index.search([1.0, 0.0, 0.0], k=2)
    assert [h[0] for h in hits] == ["leave", "payroll"]
    assert hits[0][1] == pytest.approx(cosine(np.array([1.0, 0, 0]), np.array(DOCS["leave"][0])), abs=1e-6)


def test_34_2_stores_unit_vectors(index):
    assert all(np.linalg.norm(v) == pytest.approx(1.0) for v in index.vectors)


def test_34_2_add_replaces(index):
    index.add("leave", [0.0, 0.0, 1.0], {"dept": "hr"})
    assert len(index.ids) == 5
    assert index.search([0.0, 0.0, 1.0], k=1)[0][0] == "leave"


def test_34_3_filters(index):
    assert [h[0] for h in index.search([0.0, 0.0, 1.0], k=3, where={"dept": "hr"})] == ["payroll", "leave"]
    assert [h[0] for h in index.search([0.0, 0.0, 1.0], k=3, where={"dept": "it", "year": 2025})] == ["laptop"]


def test_34_4_delete(index):
    index.delete("vpn")
    assert "vpn" not in [h[0] for h in index.search([0.0, 0.0, 1.0], k=5)]
    with pytest.raises(KeyError):
        index.delete("vpn")
