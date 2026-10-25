# Mini-project 70 · CDC replay into a table

**Day 70 · about 30 minutes · change data capture, idempotency, resuming**

## The brief

A food delivery startup copies its customers table into the analytics warehouse every hour, in full. The
table has grown, the copy now takes 50 minutes, and the data team wants to switch to the database's change
stream. Their data lead has one worry: *"the stream repeats events after a retry and sometimes sends them
out of order. The copy can't get corrupted."*

You're building the replay that makes the stream safe to use.

## What you'll build

- An `apply()` that handles one event: insert puts a row in, update merges new fields into the existing
  row, delete removes it
- A `replay()` that sorts events by their sequence number and skips anything already applied, so repeated
  events change nothing
- Resume support: start from a saved table and last sequence number after a crash, without changing the
  table you were given

You edit [`cdc.py`](cdc.py). The tests in [`test_cdc.py`](test_cdc.py) replay a stream with repeats and
out-of-order events, then replay it again from the middle.

## Done means

- [ ] `python quest.py 70` is all green (3 checks)
- [ ] You can explain what makes a replay idempotent, and why that matters for streams
- [ ] You can say why the last applied sequence number is all you need to resume

## Run it

```bash
python quest.py 70   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Apply the events to a real SQLite table (Day 8) with `INSERT ... ON CONFLICT` and store the last sequence number in it
- Write a checkpoint to disk every 100 events and show a crash and resume in a short script
- Generate 10,000 random events and time your replay against a full-table copy

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day70
git commit -m "Mini-project 70: CDC replay"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
