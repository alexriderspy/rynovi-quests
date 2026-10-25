# Mini-project 54 · A golden set that grows

**Day 54 · about 30 minutes · golden datasets, deduplication, versioning**

## The brief

The HR assistant team found four new failures this week and wants them in the golden set. Two of them are
the same question typed differently, and one is already in the set. Last quarter someone also deleted an
old case, and the bug it covered came back. The lead's rule: *"every new failure becomes a test, nothing old
gets lost, and we always know which version a score came from."*

You're building the code that grows the set safely.

## What you'll build

- A `normalise()` that lowercases text, strips punctuation and squashes spaces, so near-identical questions match
- An `add_cases()` that appends new cases, skips duplicates (even within the new batch) and never touches old ones
- A `bump_version()` that moves the set from `v3` to `v4` when it changes, and leaves it alone when it doesn't

You edit [`grow.py`](grow.py). The tests in [`test_grow.py`](test_grow.py) add a batch of new HR
questions with duplicates mixed in.

## Done means

- [ ] `python quest.py 54` is all green (3 checks)
- [ ] You can explain why scores from `v3` and `v4` of the set shouldn't be compared directly
- [ ] You can say why old cases stay in the set even after their bug is fixed

## Run it

```bash
python quest.py 54   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Save the set as a JSONL file per version (`golden_v4.jsonl`) and write a small diff command between two versions
- Catch near-duplicates too, using embeddings (Day 25) and a similarity threshold you pick and justify
- Print a per-category count after each update, so you can see which areas the set covers well

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day54
git commit -m "Mini-project 54: growing golden set"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
