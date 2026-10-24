"""Day 9 · The job API

A tiny jobs board API. The "database" is the JOBS dict below. The tests call your API with
FastAPI's TestClient, so you don't need to run a server (but you can: fastapi dev quests/day09/jobs_api.py).

Run `python quest.py 9` after each TODO.
"""
from fastapi import FastAPI, HTTPException, Response  # noqa: F401
from pydantic import BaseModel, Field  # noqa: F401

app = FastAPI(title="Rynovi jobs")

START = {
    1: {"title": "AI Engineer", "company": "Sarvam", "salary_lpa": 24.0},
    2: {"title": "ML Intern", "company": "Swiggy", "salary_lpa": 6.0},
    3: {"title": "Data Scientist", "company": "Zepto", "salary_lpa": None},
}
JOBS: dict[int, dict] = {}


def reset() -> None:
    """Put the starting jobs back. The tests call this before each test."""
    JOBS.clear()
    JOBS.update({k: dict(v) for k, v in START.items()})


reset()


class JobIn(BaseModel):
    # TODO 9.2 · Fields for a new job:
    #   title: str with at least 2 characters (Field(min_length=2))
    #   company: str
    #   salary_lpa: float or None, default None, can't be negative
    pass


# TODO 9.1 · Two endpoints:
#   GET /jobs           -> a list of every job, each as {"id": ..., "title": ..., "company": ..., "salary_lpa": ...}
#   GET /jobs/{job_id}  -> that one job, same shape. If it doesn't exist: 404 with detail "job not found"
#                          (raise HTTPException(status_code=404, detail="job not found"))

# TODO 9.2 · POST /jobs takes a JobIn, stores it with the next id (biggest id + 1),
#            and returns the new job (with its id) and status code 201.

# TODO 9.3 · Let GET /jobs take an optional query parameter min_salary (a float).
#            /jobs?min_salary=10 returns only jobs whose salary_lpa is at least 10 (jobs with no salary are left out).

# TODO 9.4 · DELETE /jobs/{job_id} removes the job and returns status 204 with no body.
#            Deleting a job that doesn't exist gives 404 "job not found".
