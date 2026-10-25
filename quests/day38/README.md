# Mini-project 38 · Picking an LLM judge you trust

**Day 38 · about 30 minutes · LLM-as-a-judge, confusion matrix, true negative rate**

## The brief

Your team wants an LLM to grade the RAG assistant's answers, so nobody has to read 500 of them by
hand. There are two judge prompts: a one-liner, and one built from your written pass/fail criteria. Both
agree with your own labels about 9 times in 10. Your lead asks: *"so either one is fine, right?"*

You're building the numbers that answer that question properly.

## What you'll build

- `confusion()`: true and false positives and negatives for a judge, against your labels
- `agreement()`: the share of answers where the judge said what you said
- `tpr()` and `tnr()`: how often the judge passes good answers, and how often it catches bad ones
- `pick_judge()`: choose the judge whose weaker rate is the stronger one

You edit [`judge.py`](judge.py). Your 30 labels and both judges' verdicts are in [`labels.py`](labels.py)
(don't edit it). The tests in [`test_judge.py`](test_judge.py) check every number.

## Done means

- [ ] `python quest.py 38` is all green (4 checks)
- [ ] You can explain how a judge with about 87% agreement catches only 1 of your 5 failures
- [ ] You can say why true negative rate matters most for a judge

## Run it

```bash
python quest.py 38   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Write a real judge prompt and run it with an LLM over the Day 36 cases, then score it with your code
- Add Cohen's kappa to the report and compare it with plain agreement
- Bootstrap a confidence interval for each rate and show how unsure 5 failures make you

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day38
git commit -m "Mini-project 38: judge the judge"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
