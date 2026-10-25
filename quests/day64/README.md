# Mini-project 64 · Model gateway with fallback and cache

**Day 64 · about 35 minutes · fallbacks, caching, load testing**

## The brief

A fintech's support copilot calls one hosted model. Last week the provider had an outage during the
evening rush, and the copilot was down for an hour. The platform lead wants a gateway in front of it:
*"if the main model fails, fall back to our local one, stop paying twice for the same question, and show
me the p95 before we ship."*

You're building that gateway, and the load test that proves it.

## What you'll build

- A `Gateway.ask()` that tries each model in order, moves on when one fails, and counts the latency of
  every model it tried
- A cache keyed on the normalised question, so a repeat costs 1 ms and calls no model at all
- A load test that sends a batch of prompts through the gateway and reports requests, failures, p95
  latency and cache hit rate

You edit [`gateway.py`](gateway.py). The models there are fakes with fixed latencies, so the numbers are
repeatable. The tests in [`test_gateway.py`](test_gateway.py) check the fallback, the cache and the load
test report.

## Done means

- [ ] `python quest.py 64` is all green (3 checks)
- [ ] You can explain why a fallback request is slower than a normal one
- [ ] You can say why only successful answers should go into the cache

## Run it

```bash
python quest.py 64   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Add a circuit breaker: after three failures in a row, skip the main model for the next 30 seconds
- Give cache entries a time to live, so answers expire after an hour
- Put the gateway behind a FastAPI endpoint (Day 60) and load test it with `locust` or `hey`

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day64
git commit -m "Mini-project 64: model gateway"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
