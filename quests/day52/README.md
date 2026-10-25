# Mini-project 52 · Trace reader for a copilot run

**Day 52 · about 30 minutes · tracing, spans, cost per run**

## The brief

A service copilot drafts replies to customer emails. One reply took over nine seconds and came back wrong.
The on-call engineer pulls up the trace of that run and asks the usual three questions: *"what was slow,
what did it cost, and what broke?"* Reading spans by eye works once, not every night.

You're building the small script that answers those questions from any trace.

## What you'll build

- A `slowest_step()` that finds the slowest span, skipping the root that covers the whole run
- A `cost_rs()` that adds up the rupee cost of every model call from its tokens and the price table
- A `failures()` that lists each span with an error, along with the step it ran under

You edit [`read_trace.py`](read_trace.py). The run you're reading is in [`trace.py`](trace.py), and the
tests in [`test_read_trace.py`](test_read_trace.py) check your three answers against it.

## Done means

- [ ] `python quest.py 52` is all green (3 checks)
- [ ] You can say which step you'd make faster first in this run, and why
- [ ] You can explain what the `parent` field tells you about where an error happened

## Run it

```bash
python quest.py 52   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Draw the trace as a text waterfall chart in the terminal, one bar per span, indented under its parent
- Export a trace from a real tracer (Langfuse, LangSmith or OpenTelemetry) and point your functions at it
- Run your functions over many traces and report p95 latency and average cost per run

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day52
git commit -m "Mini-project 52: trace reader"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
