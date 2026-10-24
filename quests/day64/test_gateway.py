import pytest

from quests.day64.gateway import FakeModel, Gateway, ModelDown, load_test, p95


def models(primary_down=False):
    return [FakeModel("claude", 800, fail_words=("overload",), down=primary_down), FakeModel("qwen-local", 300)]


def test_64_1_fallback():
    gw = Gateway(models())
    assert gw.ask("hello") == ("claude: answer to hello", 800)
    assert gw.ask("overload me") == ("qwen-local: answer to overload me", 1100)
    gw2 = Gateway([FakeModel("a", 100, down=True), FakeModel("b", 100, down=True)])
    with pytest.raises(ModelDown):
        gw2.ask("anything")


def test_64_2_cache():
    gw = Gateway(models())
    gw.ask("What is RAG?")
    ans, ms = gw.ask("  what is   rag? ")
    assert ms == 1 and gw.hits == 1 and ans.startswith("claude")
    assert gw.models[0].calls == 1, "a cache hit must not call any model"


def test_64_3_load_test():
    prompts = [f"question {i % 40}" for i in range(100)] + ["overload " + str(i) for i in range(10)]
    rep = load_test(Gateway(models()), prompts)
    assert rep == {"requests": 110, "failed": 0, "p95_ms": 1100, "cache_hit_rate": 0.55}
    down = load_test(Gateway([FakeModel("a", 50, down=True)]), ["x", "y"])
    assert down["failed"] == 2
    assert p95([5, 1, 9, 3]) == 9
