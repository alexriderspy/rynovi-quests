# Mini-project 57 · Cheap checks before the judge

**Day 57 · about 30 minutes · code checks, regex, eval costs**

## The brief

An HR policy assistant answers questions with citations like `[1]`. The team grades every answer with an
LLM judge, and the bill is growing. Looking at the failures, you notice many are obvious: no citation, a
citation to a source that wasn't retrieved, leftover template text. Your lead says: *"don't pay a judge to
spot a missing citation. Catch what code can catch, and only send the rest."*

You're building that first, free layer of checks.

## What you'll build

- A `code_checks()` that flags missing citations, citations to unknown sources, answers that ramble, and leftover template text
- A `route()` that splits answers into ones that failed the code checks and ones that go on to the judge
- A `judge_cost_saved()` that works out how much money skipping those judge calls saves

You edit [`checks.py`](checks.py). The tests in [`test_checks.py`](test_checks.py) run your checks on
eight sample answers and check the routing and savings.

## Done means

- [ ] `python quest.py 57` is all green (3 checks)
- [ ] You can say which kinds of failure code can catch and which still need a judge or a person
- [ ] You can explain why the order is code checks first, judge second

## Run it

```bash
python quest.py 57   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Add a check that the answer refuses when there are no sources, and test it on a few cases of your own
- Send the `to_judge` answers to a real judge prompt and report the total eval cost before and after
- Run your checks over the golden set from one of your RAG projects and report how many answers they catch

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day57
git commit -m "Mini-project 57: cheap checks first"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
