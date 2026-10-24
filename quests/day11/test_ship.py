"""Checks for day 11. These run real Docker commands, so Docker must be running."""
import json
import shutil
import subprocess
import time
import urllib.request
from pathlib import Path

import pytest

HERE = Path(__file__).parent
COMPOSE = ["docker", "compose", "-f", str(HERE / "compose.yaml"), "-p", "rynovi-quest-11"]


def sh(cmd: list[str], timeout: int = 600) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


@pytest.fixture(scope="module", autouse=True)
def docker_running():
    if not shutil.which("docker") or sh(["docker", "info"], 30).returncode != 0:
        pytest.fail("Docker isn't running. Start Docker Desktop (or colima start), then try again.")


def test_11_1_dockerfile_builds():
    r = sh(["docker", "build", "-t", "rynovi-quest-11", str(HERE)])
    assert r.returncode == 0, "docker build failed: " + (r.stderr.strip().splitlines() or ["no output"])[-1]
    r = sh(["docker", "run", "--rm", "rynovi-quest-11", "python", "-c", "import fastapi, psycopg, uvicorn"], 120)
    assert r.returncode == 0, "the image is missing the app's requirements"


def test_11_2_compose_has_both_services():
    r = sh(COMPOSE + ["config", "--format", "json"], 60)
    assert r.returncode == 0, "compose.yaml isn't valid: " + (r.stderr.strip().splitlines() or ["?"])[-1]
    services = json.loads(r.stdout)["services"]
    assert {"api", "db"} <= set(services), f"expected services api and db, found {sorted(services)}"
    assert any(str(p.get("published")) == "8000" for p in services["api"].get("ports", [])), "publish port 8000 on api"
    assert services["db"].get("image", "").startswith("postgres"), "db should use a postgres image"
    assert "db" in services["api"].get("depends_on", {}), "api should depend on db"


def test_11_3_stack_is_healthy():
    try:
        up = sh(COMPOSE + ["up", "-d", "--build"], 900)
        assert up.returncode == 0, "docker compose up failed: " + (up.stderr.strip().splitlines() or ["?"])[-1]
        body, deadline = None, time.time() + 90
        while time.time() < deadline:
            try:
                with urllib.request.urlopen("http://localhost:8000/health", timeout=3) as resp:
                    body = json.loads(resp.read())
                if body.get("db") == "ok":
                    break
            except Exception:
                pass
            time.sleep(2)
        assert body == {"api": "ok", "db": "ok"}, f"/health said {body}"
    finally:
        sh(COMPOSE + ["down", "-v"], 300)
