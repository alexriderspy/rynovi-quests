# Mini-project 11 · Dockerised API with Postgres

**Day 11 · about 40 minutes · Docker, Docker Compose, health checks**

## The brief

A two-person startup has a small FastAPI service that talks to Postgres. It works on the founder's laptop
and nowhere else: the new intern spent a whole day installing the right Python and database versions. The
founder wants that to never happen again: *"one command, and the API and the database are both up and
talking to each other. On anyone's machine."*

You're putting the API in a box. The app in [`app/`](app/) is already written; it has a `/health` endpoint
that reports on both the API and the database.

## What you'll build

- A `Dockerfile` that builds an image for the API, installing the requirements first so code changes rebuild fast
- A `compose.yaml` with two services, `api` and `db` (Postgres 16), with the port and database URL wired up
- A clean start: a database health check, so the API only starts once Postgres is ready and `/health` says both are `ok`

You edit [`Dockerfile`](Dockerfile) and [`compose.yaml`](compose.yaml). The tests in
[`test_ship.py`](test_ship.py) run real Docker commands: they build your image, start the stack and call
`http://localhost:8000/health`.

## Done means

- [ ] `python quest.py 11` is all green (3 checks)
- [ ] You can explain why `requirements.txt` is copied and installed before the rest of the code
- [ ] You can say why `depends_on` alone isn't enough, and what `condition: service_healthy` adds

## Run it

Docker must be running first (Docker Desktop, or `colima start`). The first run downloads images, so give
it a few minutes.

```bash
python quest.py 11                                       # builds, starts and checks the stack, then shuts it down
docker compose -f quests/day11/compose.yaml up --build   # run it yourself, then open http://localhost:8000/health
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Add a named volume for Postgres so data survives `docker compose down`, and show it in this README
- Make the image smaller (a multi-stage build, a `.dockerignore`) and note the size before and after
- Box up Day 9's jobs API the same way, with jobs stored in Postgres

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day11
git commit -m "Mini-project 11: Dockerised API with Postgres"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
