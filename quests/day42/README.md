# Mini-project 42 · State and history for support chat

**Day 42 · about 30 minutes · dataclasses, token budgets, context trimming**

## The brief

A support agent handles long chats well at first. Twenty messages in, the context window fills up,
old messages get cut, and the agent forgets the order id the customer gave at the start. The customer has
to repeat it, and is not happy. Your lead says: *"ids don't belong in chat history. Keep them in state."*

You're building the state object and the trimming that keeps both in shape.

## What you'll build

- `update_state()`: copy ids and approval from tool results into a `SupportState`, without wiping what's already there
- `trim_history()`: keep the system message and the most recent messages that fit a token budget
- `build_context()`: put the state at the top, so the order id survives even when its message is trimmed

You edit [`state.py`](state.py). The tests in [`test_state.py`](test_state.py) use a short support chat
about a missing order.

## Done means

- [ ] `python quest.py 42` is all green (3 checks)
- [ ] You can explain the difference between state and history in one sentence each
- [ ] You can say why trimming keeps whole messages, from the newest backwards

## Run it

```bash
python quest.py 42   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Count real tokens with a tokenizer (like `tiktoken`) instead of words, and compare the results
- Instead of dropping old messages, fold them into a one-line summary note in state
- Simulate a 50-message chat and show the context staying under budget at every step

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day42
git commit -m "Mini-project 42: state vs memory"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
