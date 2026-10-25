# Mini-project 14 · Checker for model-extracted invoices

**Day 14 · about 35 minutes · Pydantic schemas, validation, review routing**

## The brief

An accounts team uses a model to read vendor invoices and return JSON. Most replies are fine. Some have
chatty text around the JSON, some have `"qty": "one"`, and some look perfect but the line items don't add
up to the total. Right now all of it goes straight into the books. The finance lead is clear: *"I'd rather
check ten invoices by hand than pay one wrong one."*

You're building the checker that sits between the model and the database. You get 10 real-looking model
replies in [`outputs.py`](outputs.py). No API key needed.

## What you'll build

- A Pydantic schema for an invoice and its lines, where quantity is at least 1 and prices and totals can't be negative
- `parse()`, which turns one raw reply into an `Invoice`, or `None` when it's broken JSON or doesn't fit the schema
- `problems()`, which checks the maths in plain Python: no lines, or line items that don't add up to the total (within 1 rupee)
- `route()`, which sorts every reply into accepted or sent to a person for review

You edit [`verify.py`](verify.py). The tests in [`test_verify.py`](test_verify.py) check each reply ends up
in the right pile.

## Done means

- [ ] `python quest.py 14` is all green (4 checks)
- [ ] You can explain why a reply can pass the schema and still be wrong
- [ ] You can say why the maths check is plain Python and not another model call

## Run it

```bash
python quest.py 14   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Get real replies: send a few invoice texts to a model (Day 13's calling a model) and run them through your checker
- Pull the JSON out of chatty replies like `"Sure! Here is the invoice: {...}"` before parsing, so they're judged on what they say, not how they're wrapped
- Write the review pile to a CSV with the reason for each, so a person knows what to look at

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day14
git commit -m "Mini-project 14: invoice extraction checker"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
