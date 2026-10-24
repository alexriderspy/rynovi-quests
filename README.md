# Rynovi quests

Small coding levels that go with the [Rynovi](https://rynovi.vercel.app) 90-day AI engineer roadmap.
Each day's quest is a file with a few `TODO`s and tests. Fill in a TODO, run the quest, watch the level turn green.

```bash
git clone https://github.com/alexriderspy/rynovi-quests.git
cd rynovi-quests
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python quest.py      # every quest and your XP
python quest.py 2    # play day 2
```

| Day | Quest | You'll practise |
|---|---|---|
| 2 | The job board bouncer | Pydantic models, field and model validators, collecting errors |
| 3 | The speed run | `async`/`await`, `asyncio.gather`, semaphores, timeouts |
| 4 | The flaky server | Retries, exponential backoff, failing fast, logging |
| 5 | Bug hunt | Writing pytest tests that catch 3 planted bugs |
| 9 | The job API | FastAPI endpoints, status codes, validation, query parameters |
| 10 | Invoice detective | Reading text and tables from PDFs, spotting scans |
| 11 | Ship it in a box | A Dockerfile and a compose.yaml for an API with Postgres (needs Docker running) |
| 12 | Agent on a leash | Working with a coding agent: plan first, small reviewed commits, tests untouched |
| 14 | Trust but verify | Schemas for model output, checking the maths, routing to review |

Stuck for more than 10 minutes? Re-watch today's clip in the app, then try again. Don't peek in `quests/day05/_bugs` until you've caught them.
