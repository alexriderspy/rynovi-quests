# Mini-project 9 · Jobs API for a hiring board

**Day 9 · about 35 minutes · FastAPI, Pydantic, HTTP status codes**

## The brief

A small hiring startup lists AI jobs on its website. Today the list lives in a spreadsheet that someone
copies onto the site by hand. They want a proper API instead: the website reads jobs from it, recruiters
add new ones, and stale jobs get deleted. Their frontend developer has one request: *"use the right status
codes, so I know when something failed and why."*

You're building that API.

## What you'll build

- `GET /jobs` lists every job, and `GET /jobs/{id}` returns one, with a clean `404` when it doesn't exist
- `POST /jobs` creates a job, rejects bad input automatically (Pydantic) and answers `201 Created`
- `GET /jobs?min_salary=10` filters by salary with a query parameter
- `DELETE /jobs/{id}` removes a job and answers `204 No Content`

You edit [`jobs_api.py`](jobs_api.py). The tests in [`test_jobs_api.py`](test_jobs_api.py) call your API
the way the frontend would.

## Done means

- [ ] `python quest.py 9` is all green (4 checks)
- [ ] You've opened the auto-generated docs at `http://localhost:8000/docs` and tried each endpoint
- [ ] You can explain why creating returns `201` and deleting returns `204`

## Run it

```bash
python quest.py 9                     # checks your work and points at the next TODO
fastapi dev quests/day09/jobs_api.py  # run it for real, then open http://localhost:8000/docs
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Swap the in-memory dict for SQLite (Day 8's SQL) so jobs survive a restart
- Add `PATCH /jobs/{id}` to update just the salary
- Add a `search` query parameter that matches the title or company

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day09
git commit -m "Mini-project 9: jobs API"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
