# Mini-project 34 · Vector index for handbook search

**Day 34 · about 30 minutes · NumPy, cosine similarity, metadata filters**

## The brief

A 300-person company wants its staff to search the HR and IT handbooks by meaning, not just by
keyword. Someone has already suggested paying for a hosted vector database. Your lead wants to understand
the idea first: *"before we buy one, show me what a vector database actually does, in fifty lines."*

You're building that index, in plain NumPy.

## What you'll build

- A `cosine()` function: 1 means the same direction, 0 means unrelated
- A `VectorIndex` that stores each chunk as a unit vector plus metadata, and returns the top k matches
- Metadata filters like `where={"dept": "hr"}`, applied before ranking
- `delete()`, so a removed document never shows up in search again

You edit [`index.py`](index.py). The tests in [`test_index.py`](test_index.py) load five small
handbook documents and search them.

## Done means

- [ ] `python quest.py 34` is all green (4 checks)
- [ ] You can explain why storing unit vectors lets search use a plain dot product
- [ ] You can say why the filter has to run before ranking, not after

## Run it

```bash
python quest.py 34   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Embed the Day 33 handbook chunks with a real embedding model (Day 25's idea) and search them with your index
- Time your search on 100,000 random vectors, then speed it up by stacking them into one matrix
- Save and load the index with `np.save` so it survives a restart

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day34
git commit -m "Mini-project 34: vector index"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
