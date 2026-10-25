# Mini-project 53 · Error analysis for an HR bot

**Day 53 · about 30 minutes · error analysis, open coding, prioritising**

## The brief

A company's HR assistant answers questions about leave, travel and expenses. Employees keep complaining,
and the team has a long list of ideas to fix it. Before anyone changes a prompt, the lead asks: *"which
failures actually happen most? Show me numbers and a few real examples."* You've already read 30 failed
traces and written one note for each.

You're turning those notes into a clear answer about where to focus.

## What you'll build

- A `count_categories()` that counts failures per category, biggest first
- A `top_share()` that says how much of all failures the top categories cover
- An `examples()` that pulls the first few trace ids from a category, so the team sees real cases

You edit [`open_coding.py`](open_coding.py). The 30 notes are in [`notes.py`](notes.py), and the tests
in [`test_open_coding.py`](test_open_coding.py) check your counts and examples.

## Done means

- [ ] `python quest.py 53` is all green (3 checks)
- [ ] You can say which two categories you'd fix first and what share of failures they cover
- [ ] You can explain why showing real trace ids helps more than a number on its own

## Run it

```bash
python quest.py 53   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Read 20 to 30 traces from one of your own projects, write your own notes and run the same analysis
- Add a bar chart of failures by category to this README
- Ask a model to suggest categories for untagged notes, then compare its grouping with yours

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day53
git commit -m "Mini-project 53: error analysis"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
