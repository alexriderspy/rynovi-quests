import time

from fastapi.testclient import TestClient

from quests.day60.app import app

client = TestClient(app)


def events(text: str) -> list[str]:
    return [line[len("data: "):] for line in text.split("\n\n") if line.startswith("data: ")]


def test_60_1_health():
    r = client.get("/health")
    assert r.status_code == 200 and r.json() == {"status": "ok"}


def test_60_2_streams_tokens():
    with client.stream("GET", "/stream", params={"q": "RAG"}) as r:
        assert r.headers["content-type"].startswith("text/event-stream")
        body = "".join(r.iter_text())
    ev = events(body)
    assert ev[:4] == ["You", "asked", "about", "RAG."]
    assert ev[-1] == "[DONE]"


def test_60_3_times_out():
    t = time.monotonic()
    with client.stream("GET", "/stream", params={"q": "something slow"}) as r:
        body = "".join(r.iter_text())
    assert time.monotonic() - t < 4, "the request should stop after about 2 seconds"
    ev = events(body)
    assert ev[-1] == "[TIMEOUT]" and 1 <= len(ev) - 1 <= 3
