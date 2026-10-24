from quests.day33.chop import fixed_chunks, hit_rate, recursive_chunks, search
from quests.day33.corpus import HANDBOOK


def test_33_1_fixed_chunks():
    assert fixed_chunks("abcdefghij", size=4) == ["abcd", "efgh", "ij"]
    assert fixed_chunks("abcdefghij", size=4, overlap=2) == ["abcd", "cdef", "efgh", "ghij", "ij"]
    assert all(len(c) <= 200 for c in fixed_chunks(HANDBOOK))


def test_33_2_recursive_chunks():
    chunks = recursive_chunks(HANDBOOK, size=400)
    assert all(0 < len(c) <= 400 for c in chunks)
    assert "Leave policy" in chunks
    assert any(c.startswith("Every full-time employee gets 24 days") for c in chunks), "chunks should start at sentence or paragraph boundaries"
    assert all(c == c.strip() for c in chunks)


def test_33_3_search():
    chunks = ["the cat sat", "learning budget is big", "budget for learning and books"]
    assert search(chunks, "learning budget", k=2) == ["learning budget is big", "budget for learning and books"]


def test_33_4_measure_both():
    fixed = hit_rate(fixed_chunks(HANDBOOK, size=200), k=3)
    smart = hit_rate(recursive_chunks(HANDBOOK, size=400), k=3)
    assert 0 <= fixed <= 1 and 0 <= smart <= 1
    assert smart >= 0.9, f"recursive chunks found {smart:.0%} of answers; expected at least 90%"
    assert smart > fixed, f"recursive ({smart:.0%}) should beat fixed-size chunks ({fixed:.0%}) here"
