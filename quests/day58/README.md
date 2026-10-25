# Mini-project 58 · Eval regression gate for CI

**Day 58 · about 30 minutes · evals in CI, exit codes, baselines**

## The brief

A team runs a RAG assistant for an insurance company's support desk. Every pull request already runs the
evals, but nobody reads the numbers, and last month a prompt change quietly dropped faithfulness by five
points. Their lead wants a hard stop: *"if any score goes down, the build goes red, and it tells me which
one."*

You're building that gate.

## What you'll build

- A `drops()` function that compares this run's scores with the last release and lists every metric that
  fell by more than a small tolerance, including metrics that went missing
- A command-line script that prints each drop and exits with `1`, so CI fails the build, or prints
  `no regressions` and exits with `0`
- A `next_baseline()` step that moves the baseline forward after a clean merge, and keeps the old one if
  anything dropped

You edit [`gate.py`](gate.py). The tests in [`test_gate.py`](test_gate.py) check the drop messages, the
exit codes and how the baseline moves.

## Done means

- [ ] `python quest.py 58` is all green (3 checks)
- [ ] You can explain why a non-zero exit code is all CI needs to fail a build
- [ ] You can say why a metric that disappears from the results should count as a drop

## Run it

```bash
python quest.py 58                                        # checks your work and points at the next TODO
python quests/day58/gate.py baseline.json current.json    # run the gate on two JSON score files of your own
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Add a GitHub Actions workflow that runs your evals and then the gate on every pull request
- Give each metric its own tolerance (read from a small config file), since some scores are noisier than others
- Post the drops as a Markdown table in the pull request summary instead of plain lines

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day58
git commit -m "Mini-project 58: eval regression gate"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
