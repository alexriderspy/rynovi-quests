# Mini-project 56 · Trajectory scores for agent runs

**Day 56 · about 30 minutes · agent evals, trajectories, subsequence checks**

## The brief

A service copilot books visits, issues refunds and answers FAQs. Most runs end with the right answer, so
the team thinks it's fine. But the bill says otherwise: some runs call the same search tool again and
again before finishing. The lead asks: *"don't just tell me if it finished. Did it use the right tools, in
the right order, and how many steps did it waste?"*

You're building the scorer that looks at how each run got there, not only where it ended.

## What you'll build

- A `success_rate()` that gives the share of the 20 runs that finished the task
- A `used_right_tools()` check that the expected tools appear in order, with other calls allowed in between
- A `wasted_steps()` count and a `report()` that sums it all up and names the runs that wandered most

You edit [`trajectory.py`](trajectory.py). The 20 runs are in [`runs.py`](runs.py), and the tests in
[`test_trajectory.py`](test_trajectory.py) check each score and the final report.

## Done means

- [ ] `python quest.py 56` is all green (3 checks)
- [ ] You can explain why a run can succeed and still score badly on its trajectory
- [ ] You can say why the tool check is a subsequence check and not an exact match

## Run it

```bash
python quest.py 56   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Add a cost score: give each tool a rupee price and report the money wasted by the wanderers
- Break the report down by task (`book_visit`, `refund`, `answer_faq`) to see which one wanders most
- Record real runs from the agent you built on Day 40 and score them with the same functions

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day56
git commit -m "Mini-project 56: trajectory scores"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
