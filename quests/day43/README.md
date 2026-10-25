# Mini-project 43 · Long-term memory for a career bot

**Day 43 · about 30 minutes · memory stores, relevance scoring, regex**

## The brief

A career-guidance chatbot for students forgets everything between sessions. Riya told it last month
she lives in Pune and prefers Python, and today it asks again. Worse, she has since moved to Bengaluru.
The product lead wants: *"remember what matters, bring up only what's relevant, and update it when life
changes."*

You're building that memory store.

## What you'll build

- `remember()`, `get()` and `forget()`: save facts per user, replace old values, delete on request
- `recall()`: only the facts relevant to the current question, best match first
- `extract()`: pull facts like name, city, employer and preference straight out of a message

You edit [`memory.py`](memory.py). The tests in [`test_memory.py`](test_memory.py) check saving,
recall and extraction.

## Done means

- [ ] `python quest.py 43` is all green (3 checks)
- [ ] You can explain why a fact that changed must replace the old one, not sit next to it
- [ ] You can say why recall leaves out facts with a score of 0

## Run it

```bash
python quest.py 43   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Save the store to a JSON or SQLite file so memory survives a restart
- Use embeddings and your Day 34 index for recall, so "Bengaluru" matches "Bangalore"
- Keep a dated history of each fact and add a "what do you know about me?" command

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day43
git commit -m "Mini-project 43: long-term memory"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
