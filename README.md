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
| 29 | Chat template by hand | ChatML and Llama 3 formats, generation prompts, valid conversations |
| 30 | LoRA by hand | A LoRA layer in NumPy, parameter counts, merging |
| 32 | The verdict | Accuracy vs per-label F1 vs cost: should you ship the fine-tune? |
| 33 | Chop shop | Fixed and recursive chunking, measuring hit rate |
| 34 | Nearest neighbours | A tiny vector index: cosine, top-k, metadata filters |
| 35 | Best of both | Hybrid search with reciprocal rank fusion |
| 36 | Show your sources | Checking citations and refusing on weak retrieval |
| 37 | Golden set | Validating and growing an eval set |
| 38 | Judge the judge | Agreement vs true positive and negative rates for LLM judges |

Stuck for more than 10 minutes? Re-watch today's clip in the app, then try again. Don't peek in `quests/day05/_bugs` until you've caught them.
