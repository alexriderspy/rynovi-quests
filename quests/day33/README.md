# Mini-project 33 · Chunkers for a handbook assistant

**Day 33 · about 35 minutes · chunking, keyword search, hit rate**

## The brief

An HR team wants an assistant that answers questions from the company handbook: leave, work from home,
expenses. The first version keeps missing answers that are clearly in the document, because it cut the
handbook into chunks of 200 characters, often in the middle of a sentence. The engineer on it asks:
*"before we touch the model, can we prove a better way of cutting finds more answers?"*

You're building two chunkers and the measurement that settles it. The handbook, the questions and a
simple keyword score are in [`corpus.py`](corpus.py).

## What you'll build

- `fixed_chunks()`, which cuts text into pieces of a fixed size, with optional overlap
- `recursive_chunks()`, which splits on paragraphs first, then sentences, and never goes over the size limit
- `search()`, which returns the top-k chunks for a question using the keyword score
- `hit_rate()`, which measures how often the answer is inside the top 3 chunks, for both chunkers

You edit [`chop.py`](chop.py). The tests in [`test_chop.py`](test_chop.py) check each splitter, then
expect the recursive one to find at least 90% of the answers and beat the fixed one.

## Done means

- [ ] `python quest.py 33` is all green (4 checks)
- [ ] You can say the hit rate for both chunkers, and why the recursive one wins on this handbook
- [ ] You can explain what overlap buys you in fixed-size chunks, and what it costs

## Run it

```bash
python quest.py 33   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Try sizes from 100 to 800 characters for both chunkers and add a small hit-rate table to this README
- Add metadata to each chunk (the section heading it came from) and show it next to each search result
- Swap the keyword score for embeddings in a vector database (Day 34) and compare hit rates

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day33
git commit -m "Mini-project 33: chunkers and hit rate"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
