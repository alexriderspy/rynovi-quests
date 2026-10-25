# Mini-project 69 · Incremental index sync

**Day 69 · about 30 minutes · content hashing, sync planning, embeddings**

## The brief

A legal-tech startup re-embeds all 40,000 of its documents every night, even though only a few dozen
change. The job takes hours and the embedding bill is the biggest line on their cloud invoice. Their CTO
asks: *"can we only touch what actually changed?"*

You're building the sync that does exactly that.

## What you'll build

- A `content_hash()` that fingerprints each document's text with SHA-256
- A `plan_sync()` that compares the source with the index and lists what to add, update and delete, plus
  how many need nothing
- An `apply_sync()` that carries out the plan, calls the embedding function only for new and changed
  documents, and reports how many embeddings it made

You edit [`sync.py`](sync.py). The tests in [`test_sync.py`](test_sync.py) check the plan and count every
call to the embedding function.

## Done means

- [ ] `python quest.py 69` is all green (3 checks)
- [ ] You can explain why a hash is enough to know a document changed, without storing its old text
- [ ] You can say why running the sync twice in a row should embed nothing the second time

## Run it

```bash
python quest.py 69   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Hash and re-embed per chunk instead of per document, so a one-line edit re-embeds one chunk (Day 33)
- Run the sync against a real vector database (Day 34) with a real embedding model, and time it against a full rebuild
- Print a sync report with counts and the cost saved, using a price per million tokens

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day69
git commit -m "Mini-project 69: incremental index sync"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
