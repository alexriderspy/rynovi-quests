# Mini-project 32 · Ship-or-not report for a fine-tune

**Day 32 · about 30 minutes · accuracy, per-label F1, cost**

## The brief

You fine-tuned a model to label GitHub issues as bug, feature or question. Now the team has to decide
whether to ship it. There are three options: a cheap TF-IDF baseline, the untrained LLM with a good prompt,
and your LoRA fine-tune. Your manager doesn't want a demo: *"show me the numbers, and if the cheap one is
nearly as good, we're shipping the cheap one."*

You're writing the report that makes the call. All three models have already labelled the 36 newest issues
in [`data.py`](data.py), with the cost of each.

## What you'll build

- `accuracy()`: the share of issues each model labelled correctly
- `f1()`: precision, recall and F1 for one label, with a safe `0.0` when a label is never predicted
- `macro_f1()`: the plain average of F1 over the three labels, so a small class counts as much as a big one
- `verdict()`: pick the model with the best macro F1, unless a cheaper one is within 0.02 of it

You edit [`verdict.py`](verdict.py). The tests in [`test_verdict.py`](test_verdict.py) check every number
and the final pick, including a near tie where the cheap model should win.

## Done means

- [ ] `python quest.py 32` is all green (4 checks)
- [ ] You can say which model you'd ship and give its macro F1 and cost in one sentence
- [ ] You can explain why macro F1 can tell a different story from accuracy

## Run it

```bash
python quest.py 32   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Print a confusion matrix for each model and add the one for your pick to this README
- Bootstrap the 36 issues (resample them 1,000 times) to see how sure you can be that the fine-tune really beats the baseline
- Run your own Day 31 model on the same issues and add it as a fourth row

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day32
git commit -m "Mini-project 32: fine-tune ship-or-not report"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
