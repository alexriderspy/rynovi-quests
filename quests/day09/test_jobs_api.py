import pytest
from fastapi.testclient import TestClient

from quests.day09 import jobs_api

client = TestClient(jobs_api.app)


@pytest.fixture(autouse=True)
def fresh_jobs():
    jobs_api.reset()


def test_9_1_list_jobs():
    r = client.get("/jobs")
    assert r.status_code == 200
    assert [j["id"] for j in r.json()] == [1, 2, 3]
    assert r.json()[0] == {"id": 1, "title": "AI Engineer", "company": "Sarvam", "salary_lpa": 24.0}


def test_9_1_get_one_job():
    r = client.get("/jobs/2")
    assert r.status_code == 200 and r.json()["company"] == "Swiggy"


def test_9_1_missing_job_is_404():
    r = client.get("/jobs/99")
    assert r.status_code == 404, f"expected 404, got {r.status_code}"
    assert r.json() == {"detail": "job not found"}


def test_9_2_create_job():
    r = client.post("/jobs", json={"title": "LLM Engineer", "company": "Krutrim", "salary_lpa": 30})
    assert r.status_code == 201, f"expected 201 Created, got {r.status_code}"
    assert r.json() == {"id": 4, "title": "LLM Engineer", "company": "Krutrim", "salary_lpa": 30.0}
    assert client.get("/jobs/4").json()["company"] == "Krutrim"


def test_9_2_rejects_bad_input():
    assert client.post("/jobs", json={"title": "X", "company": "Ola"}).status_code == 422
    assert client.post("/jobs", json={"title": "Analyst", "company": "Ola", "salary_lpa": -2}).status_code == 422
    assert client.post("/jobs", json={"company": "Ola"}).status_code == 422


def test_9_3_filter_by_salary():
    r = client.get("/jobs", params={"min_salary": 10})
    assert r.status_code == 200
    assert [j["id"] for j in r.json()] == [1]


def test_9_4_delete_job():
    r = client.delete("/jobs/2")
    assert r.status_code == 204 and r.content == b""
    assert client.get("/jobs/2").status_code == 404
    assert client.delete("/jobs/2").status_code == 404
