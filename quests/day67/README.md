# Mini-project 67 · Permission-aware search with audit log

**Day 67 · about 30 minutes · roles, retrieval filtering, audit trails**

## The brief

A mid-sized IT services company wants an internal assistant that answers questions from its policy
documents. Some of those documents are salary bands and board notes. Their security lead signs off on one
condition: *"the assistant only ever sees what the person asking is allowed to see, and I can check later
who was shown what."*

You're building the search layer that keeps that promise.

## What you'll build

- A `can_read()` check that compares a user's roles with a document's roles
- A `search()` that drops every document the user can't read first, and only then ranks the rest by
  matching words
- An `AuditLog` that records who asked, what they asked and which document ids they got (never the text),
  and can answer "who saw this document?"

You edit [`access.py`](access.py). The tests in [`test_access.py`](test_access.py) search as different
employees and check the log.

## Done means

- [ ] `python quest.py 67` is all green (3 checks)
- [ ] You can explain why filtering after ranking can still leak a document
- [ ] You can say why the audit log stores ids and not the document text

## Run it

```bash
python quest.py 67   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Swap the word-count scoring for embeddings in a vector database (Day 34) with a metadata filter on roles
- Write the audit log to SQLite with a timestamp, and add a query for "everything this user saw this week"
- Put the search behind a FastAPI endpoint where the user comes from a login token (Day 66), not a parameter

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day67
git commit -m "Mini-project 67: permission-aware search"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
