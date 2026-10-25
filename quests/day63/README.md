# Mini-project 63 · Cost dashboard for a copilot

**Day 63 · about 30 minutes · percentiles, token pricing, tracing**

## The brief

A property company runs a copilot that sorts emails, answers tenant questions and books flat visits. It's
been live for a month and the bill keeps growing. Their head of engineering wants three numbers on a screen
every morning: *"how fast is it, what does each kind of task cost us in rupees, and which step is eating
the money?"*

You have 200 traced runs from one day in production. You're building the numbers behind that screen.

## What you'll build

- A `percentile()` function (nearest rank) to get p50 and p95 latency across all runs
- A cost report: the average rupee cost of one run of each task, adding up the tokens of every step
- A finder for the single step name that costs the most across the whole day

You edit [`dashboard.py`](dashboard.py), which reads the runs and prices from [`runs.py`](runs.py) (don't
edit that one). The tests in [`test_dashboard.py`](test_dashboard.py) check each number against the real
data.

## Done means

- [ ] `python quest.py 63` is all green (3 checks)
- [ ] You can explain why teams watch p95 latency and not just the average
- [ ] You can say which task is the most expensive and why, from its steps

## Run it

```bash
python quest.py 63   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Turn the numbers into a one-page HTML or Streamlit dashboard with a latency histogram
- Work out how much the bill would drop if the costliest step moved to the small model, and add it to this README
- Add a cost-per-1,000-runs projection per task so the team can plan a monthly budget

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day63
git commit -m "Mini-project 63: cost dashboard"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
