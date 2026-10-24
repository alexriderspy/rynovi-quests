"""Day 60 · Stream it

Nobody waits 20 seconds staring at a blank screen. Stream the model's tokens as they're produced, using
server-sent events (SSE): each chunk is a line "data: <text>" followed by a blank line.

fake_llm() below stands in for a real model. Run `python quest.py 60` after each TODO.
Try it for real: fastapi dev quests/day60/app.py, then curl -N "localhost:8000/stream?q=hello"
"""
import time
from collections.abc import Iterator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse  # noqa: F401

app = FastAPI()


def fake_llm(prompt: str, delay: float = 0.01) -> Iterator[str]:
    """Yields the reply word by word. Prompts containing "slow" take 1 second per word. Don't edit."""
    for word in f"You asked about {prompt}. Here is a short answer.".split():
        time.sleep(1.0 if "slow" in prompt else delay)
        yield word


# TODO 60.1 · GET /health returns {"status": "ok"}. Load balancers call this to know you're alive.

# TODO 60.2 · GET /stream?q=... returns a StreamingResponse with media_type "text/event-stream".
#   For each word from fake_llm(q) send "data: <word>\n\n", and finish with "data: [DONE]\n\n".

# TODO 60.3 · Never let one slow request hang: stop streaming once 2 seconds have passed since the request
#   started, send "data: [TIMEOUT]\n\n" instead of [DONE], and end. (Check time.monotonic() between words.)
