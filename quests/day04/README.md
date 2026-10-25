# Mini-project 4 · Retry wrapper for a flaky API

**Day 4 · about 30 minutes · retries, exponential backoff, logging**

## The brief

Your team's nightly job calls a partner's API that fails about half the time: timeouts, `503`s, the
usual. Right now one failure kills the whole run. But some errors, like a `404`, will never fix
themselves, and retrying those only wastes time. Your lead wants it sorted: *"retry what's worth
retrying, back off so we don't flood them, and log every attempt so I can see what happened at 3 a.m."*

You're building the retry wrapper the whole team will call.

## What you'll build

- `call_with_retry()`, which retries a failing call with exponential backoff (wait 0.5s, then 1s, then 2s) and raises the last error if every attempt fails
- Fail fast: only `TransientError` (a timeout or a `503`) gets retried, and anything else, like a `404`, is raised at once with no waiting
- A warning log line before each wait, saying which attempt failed, why, and how long you'll wait

You edit [`flaky_server.py`](flaky_server.py). The tests in [`test_flaky_server.py`](test_flaky_server.py)
use a fake server that fails a set number of times, and pass in their own `sleep` so they run instantly.

## Done means

- [ ] `python quest.py 4` is all green (3 checks)
- [ ] You can explain why retrying a `404` is pointless but retrying a `503` often works
- [ ] You can say why the function takes `sleep` as an argument instead of calling `time.sleep` directly

## Run it

```bash
python quest.py 4   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Add random jitter to each wait, and write a few lines in this README on why it helps when many clients retry at once
- Turn it into a `@retry(attempts=4)` decorator you can put on any function
- Point it at a real endpoint that fails on purpose (like `https://httpbin.org/status/503`) and show the log output

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day04
git commit -m "Mini-project 4: retry wrapper"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
