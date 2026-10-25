# Mini-project 48 · Context budget for a research agent

**Day 48 · about 30 minutes · context engineering, token budgets, summarisation**

## The brief

Your team's research agent runs for 30 steps or more. By step 20 the context is full of old tool outputs,
it costs more per call, and the agent forgets the one thing that mattered. Your lead puts it simply:
*"keep it under budget, but it must never forget that the report is due Friday."*

You're building the part that decides what stays in the context and what gets squashed.

## What you'll build

- A `split()` that sorts messages into three groups: kept (the system prompt and pinned facts), old, and recent
- A `compress()` that leaves the context alone when it fits, and otherwise replaces old steps with one summary, dropping even that if it's still too big
- A `run_with_budget()` that plays out a 30-step run and reports the biggest the context ever got

You edit [`context.py`](context.py). The tests in [`test_context.py`](test_context.py) run a 30-step
agent under a 90-token budget and check the pinned fact survives.

## Done means

- [ ] `python quest.py 48` is all green (3 checks)
- [ ] You can explain why recent steps are kept word for word while older ones get summarised
- [ ] You can name something in your own projects that should be pinned

## Run it

```bash
python quest.py 48   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Swap the word count for a real tokenizer (for example `tiktoken`) and see how your budget changes
- Replace the stand-in `summarise()` with a call to a small, cheap model and compare the summaries
- Plot context size per step with and without compression, and add the chart to this README

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day48
git commit -m "Mini-project 48: context budget"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
