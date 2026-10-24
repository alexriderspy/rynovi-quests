import asyncio
import time

from quests.day03 import fake_web
from quests.day03.speed_run import fetch_all, fetch_all_limited, fetch_all_safe, fetch_one

URLS = [f"https://example.com/page/{i}" for i in range(20)]


def timed(coro):
    fake_web.reset()
    t = time.perf_counter()
    out = asyncio.run(coro)
    return out, time.perf_counter() - t


def test_3_1_fetch_one():
    out, _ = timed(fetch_one(URLS[0]))
    assert out == (URLS[0], len(f"<html><body>{URLS[0]}</body></html>"))


def test_3_2_all_at_once():
    out, secs = timed(fetch_all(URLS))
    assert [u for u, _ in out] == URLS, "keep the results in the same order as the urls"
    assert secs < 1.0, f"took {secs:.1f}s: are you awaiting them one by one?"
    assert fake_web.max_running > 10


def test_3_3_respects_the_limit():
    out, secs = timed(fetch_all_limited(URLS, limit=3))
    assert [u for u, _ in out] == URLS
    assert fake_web.max_running <= 3, f"{fake_web.max_running} fetches ran at once; the limit is 3"
    assert fake_web.max_running > 1, "the limit is 3, not 1: run them in parallel"
    assert secs < 2.5


def test_3_4_skips_slow_pages():
    urls = URLS[:5] + ["https://example.com/slow/1", "https://example.com/slow/2"]
    out, secs = timed(fetch_all_safe(urls, timeout=0.5))
    assert secs < 1.5, f"took {secs:.1f}s: the slow pages should time out after 0.5s"
    assert dict(out)["https://example.com/slow/1"] is None
    assert all(n for u, n in out if "slow" not in u)
