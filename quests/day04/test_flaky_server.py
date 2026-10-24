import logging

import pytest

from quests.day04.flaky_server import PermanentError, TransientError, call_with_retry


class Server:
    """Fails `fail_times` times, then answers "ok"."""

    def __init__(self, fail_times: int, error: type[Exception] = TransientError):
        self.fail_times, self.error, self.calls = fail_times, error, 0

    def __call__(self) -> str:
        self.calls += 1
        if self.calls <= self.fail_times:
            raise self.error(f"call {self.calls} failed")
        return "ok"


def test_4_1_recovers_with_backoff():
    waits: list[float] = []
    server = Server(fail_times=2)
    assert call_with_retry(server, attempts=4, base_delay=0.5, sleep=waits.append) == "ok"
    assert server.calls == 3
    assert waits == [0.5, 1.0], f"expected waits [0.5, 1.0], got {waits}"


def test_4_1_gives_up_after_attempts():
    waits: list[float] = []
    server = Server(fail_times=99)
    with pytest.raises(TransientError, match="call 4 failed"):
        call_with_retry(server, attempts=4, base_delay=0.5, sleep=waits.append)
    assert server.calls == 4
    assert waits == [0.5, 1.0, 2.0]


def test_4_2_permanent_errors_fail_fast():
    waits: list[float] = []
    server = Server(fail_times=1, error=PermanentError)
    with pytest.raises(PermanentError):
        call_with_retry(server, sleep=waits.append)
    assert server.calls == 1 and waits == [], "a 404 won't fix itself: don't retry it"


def test_4_2_other_errors_fail_fast():
    server = Server(fail_times=1, error=KeyError)
    with pytest.raises(KeyError):
        call_with_retry(server, sleep=lambda s: None)
    assert server.calls == 1


def test_4_3_logs_each_retry(caplog):
    caplog.set_level(logging.WARNING, logger="rynovi.retry")
    call_with_retry(Server(fail_times=2), base_delay=0.5, sleep=lambda s: None)
    msgs = [r.getMessage() for r in caplog.records if r.name == "rynovi.retry"]
    assert msgs == ["attempt 1 failed: call 1 failed; retrying in 0.5s", "attempt 2 failed: call 2 failed; retrying in 1.0s"]
