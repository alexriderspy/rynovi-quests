# Mini-project 12 · Text stats module, built by an agent

**Day 12 · about 45 minutes · coding agents, planning, code review**

## The brief

Your team has started using coding agents, and the results are mixed. One teammate let an agent run
loose and it "fixed" failing tests by editing the tests. Now your lead has a rule for everyone: *"the
agent writes a plan first, you read every diff, and you commit in small steps. And nobody touches the
tests."*

You're showing the team what that looks like on a small module, [`textstats.py`](textstats.py): word
counts, top words and reading time. You don't write the code yourself. You stay in charge of the agent
that does.

## What you'll build

- A plan first: ask your agent for one and save it as `PLAN.md` in this folder, with at least 3 bullet points
- The three functions in `textstats.py`, written by the agent until [`test_textstats.py`](test_textstats.py) passes
- A clean history: the tests left exactly as they were, and the work on `textstats.py` committed in at least two small, reviewed steps

The agent edits [`textstats.py`](textstats.py), and you create `PLAN.md` and the commits.
[`test_process.py`](test_process.py) checks how you worked: the plan, the untouched tests and your git log.

## Done means

- [ ] `python quest.py 12` is all green (3 checks)
- [ ] You read every diff before committing it, and could explain each change to a reviewer
- [ ] You can say why an agent editing the tests is a red flag, even when everything goes green

## Run it

Any coding agent works (Claude Code, Cursor, Copilot...). No paid agent? Run Claude Code free on your
laptop with Ollama: [local-coding-agent](https://github.com/alexriderspy/local-coding-agent).

```bash
python quest.py 12   # checks the plan, the tests and your commits
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Add a short "What the agent got wrong" section to `PLAN.md`: what you caught in review and how you fixed it
- Ask the agent for a new function (like `longest_sentence()`), but this time you write the test first and it writes the code
- Try the same task with two different agents or models and compare the plans and the number of fixes you needed

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub. Your small
commits are already made; this adds anything left (like `PLAN.md`) and pushes:

```bash
git add quests/day12
git commit -m "Mini-project 12: agent-built text stats"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
