# Mini-project 37 · Golden set for a handbook bot

**Day 37 · about 40 minutes · Pydantic, JSONL, test coverage**

## The brief

Your team keeps changing the handbook assistant's prompt and chunking, and every change is judged
by someone trying three questions and saying "looks better". Your lead wants a real test set:
*"thirty questions we trust, covering every topic, including the ones it should refuse."*

You're building the golden set and the code that keeps it honest.

## What you'll build

- A Pydantic `GoldenCase` schema, with a rule that answer cases need a source and refuse cases don't
- A loader that reads `golden.jsonl` and tells you exactly which line is broken
- `coverage()` and `gaps()`: how many cases each category has, and which ones are too thin
- A grown `golden.jsonl`: at least 30 cases, at least 3 per category, at least 5 refusals, no duplicates

You edit [`golden.py`](golden.py) and [`golden.jsonl`](golden.jsonl). Write new cases from the handbook in
[`../day33/corpus.py`](../day33/corpus.py). The tests in [`test_golden.py`](test_golden.py) check the code and your set.

## Done means

- [ ] `python quest.py 37` is all green (3 checks)
- [ ] You've checked every `must_include` you wrote against the handbook text itself
- [ ] You can explain why a golden set needs refusal cases, not only answer cases

## Run it

```bash
python quest.py 37   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Run Day 33's search over every answer case and report which questions retrieval gets wrong
- Add a `difficulty` field (easy, paraphrase, multi-part) and show coverage by difficulty too
- Write a check that flags near-duplicate questions, not just exact ones

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day37
git commit -m "Mini-project 37: golden set"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
