# Mini-project 49 · Approval gate for refunds

**Day 49 · about 30 minutes · human-in-the-loop, checkpoints, JSON state**

## The brief

An online store's support agent can look up orders on its own. But when it wants to refund money or email
a customer, the support lead wants a person to check first: *"it can do the lookups, but a human signs off
on anything that touches money or a customer's inbox."* The person might reply in five minutes or five hours,
so the run has to pause, wait, and pick up exactly where it stopped.

You're building that approval gate.

## What you'll build

- A `needs_approval()` rule: risky tools (email, booking, refunds) and any call with an amount over 5000 need a person
- A `run()` that works through tool calls and pauses at the first risky one, saving its state as a JSON checkpoint
- A `decide()` that records a person's choice (approve, edit the input, or reject), so `run()` can resume from the checkpoint

You edit [`approvals.py`](approvals.py). The tests in [`test_approvals.py`](test_approvals.py) pause a
refund flow, approve the refund, edit the customer email and resume to the end.

## Done means

- [ ] `python quest.py 49` is all green (3 checks)
- [ ] You can explain why the checkpoint is a JSON string and not a Python object kept in memory
- [ ] You can say what the run returns for a rejected call, and why it keeps going

## Run it

```bash
python quest.py 49   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Save checkpoints in SQLite so a paused run survives a restart, and resume it from a second script
- Put a small FastAPI page in front of it that lists paused runs with Approve, Edit and Reject buttons
- Rebuild the same flow with LangGraph's checkpoints and interrupts (Day 44) and compare the two

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day49
git commit -m "Mini-project 49: approval gate"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
