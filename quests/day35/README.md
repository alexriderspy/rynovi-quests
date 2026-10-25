# Mini-project 35 · Hybrid search for a support bot

**Day 35 · about 30 minutes · BM25, rank fusion, hit rate**

## The brief

A payments app's support bot finds help articles with embedding search. It handles "how do I get my
money back" well, but fails on exact things like the error code "XJ-204". The old keyword search is the
opposite. The support lead asks: *"can't we just use both?"*

You're building the fusion step, and the number that proves it works.

## What you'll build

- Reciprocal rank fusion (`rrf`): merge two rankings into one, so documents both searches like rise to the top
- `hit_at_k`: the share of queries where the right document lands in the top k
- A `report()` that puts keyword, embedding and hybrid hit rates side by side, so the win is plain to see

You edit [`fusion.py`](fusion.py). The ten queries and both rankings are in [`rankings.py`](rankings.py)
(don't edit it). The tests in [`test_fusion.py`](test_fusion.py) check the fusion and the hit rates.

## Done means

- [ ] `python quest.py 35` is all green (3 checks)
- [ ] You can say which kind of query each search wins on, using two examples from `rankings.py`
- [ ] You can explain what the `k = 60` in RRF does

## Run it

```bash
python quest.py 35   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Try RRF with k from 1 to 100 and chart how hit rate @1 and @3 change
- Add MRR (mean reciprocal rank) to the report, and explain when it tells you more than hit rate
- Run real BM25 (the `rank_bm25` package) and an embedding model over the Day 33 handbook and fuse those

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day35
git commit -m "Mini-project 35: hybrid search"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
