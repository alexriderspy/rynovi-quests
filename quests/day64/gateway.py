"""Day 64 · Gateway

Model providers go down and rate-limit you. A gateway sits in front of them: it tries the main model,
falls back to a second one when it fails, and answers repeated questions from a cache.
The "models" here are fakes with known latencies, so the load test is repeatable.

Run `python quest.py 64` after each TODO.
"""
import math  # noqa: F401
import re  # noqa: F401


class ModelDown(Exception):
    pass


class FakeModel:
    """Answers after `latency_ms`. Fails on every call while down is True, or on prompts containing a fail word."""

    def __init__(self, name: str, latency_ms: int, fail_words: tuple[str, ...] = (), down: bool = False):
        self.name, self.latency_ms, self.fail_words, self.down, self.calls = name, latency_ms, fail_words, down, 0

    def complete(self, prompt: str) -> str:
        self.calls += 1
        if self.down or any(w in prompt for w in self.fail_words):
            raise ModelDown(self.name)
        return f"{self.name}: answer to {prompt}"


class Gateway:
    def __init__(self, models: list[FakeModel]):
        self.models = models
        self.cache: dict[str, str] = {}
        self.hits = 0

    def ask(self, prompt: str) -> tuple[str, int]:
        """Return (answer, latency_ms).

        TODO 64.1 · Try each model in order. A model that raises ModelDown costs its latency and you move on.
                   Latency is the sum of the latencies of every model you tried. If all fail, raise ModelDown("all").
        TODO 64.2 · Cache by the normalised prompt (lowercase, squashed spaces, stripped). A cache hit costs 1 ms,
                   calls no model, and adds 1 to self.hits. Only successful answers are cached.
        """
        raise NotImplementedError


def p95(latencies: list[int]) -> int:
    """TODO 64.3 · Nearest-rank 95th percentile (sorted, position ceil(0.95 × n), 1-based)."""
    raise NotImplementedError


def load_test(gateway: Gateway, prompts: list[str]) -> dict:
    """TODO 64.3 · Send every prompt through the gateway. Return
        {"requests": n, "failed": how many raised ModelDown, "p95_ms": p95 of the successful latencies,
         "cache_hit_rate": hits / n rounded to 2 decimals}"""
    raise NotImplementedError
