# Mini-project 55 · Calibrate an LLM judge

**Day 55 · about 30 minutes · LLM-as-a-judge, TPR and TNR, dev and test splits**

## The brief

Your team uses an LLM judge to grade the assistant's answers. On production traffic it says 70% of
answers pass, and the product manager wants to put that number in the weekly update. Your lead isn't sure:
*"you tuned that judge until it agreed with you. Does it hold up on answers it never saw, and is 70% the
real number?"* You have 120 answers you labelled yourself, split into dev and test.

You're building the check that tells the team whether to trust the judge, and what the true pass rate is.

## What you'll build

- A `rates()` that measures how often the judge agrees with you on passes (TPR) and on fails (TNR)
- A `holds_up()` that checks the judge on the test split and makes sure it didn't drop much from dev
- A `corrected_pass_rate()` that uses the judge's known mistakes to estimate the real production pass rate

You edit [`calibrate.py`](calibrate.py). Your labels and the production verdicts are in
[`data.py`](data.py), and the tests in [`test_calibrate.py`](test_calibrate.py) check your rates and
the corrected number.

## Done means

- [ ] `python quest.py 55` is all green (3 checks)
- [ ] You can explain why the rates come from the test split, not the dev split you tuned on
- [ ] You can say in one sentence why the corrected pass rate differs from the 70% the judge reports

## Run it

```bash
python quest.py 55   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Add a confidence interval to the corrected pass rate by bootstrapping the test split
- Label 50 answers from one of your own projects, run a real judge prompt on them and calibrate it the same way
- Show how the corrected rate moves as TPR and TNR change, in a small table or chart

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day55
git commit -m "Mini-project 55: calibrate the judge"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
