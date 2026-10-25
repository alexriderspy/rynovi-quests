# Mini-project 36 · Citation checker for an HR assistant

**Day 36 · about 30 minutes · regex, citations, refusing**

## The brief

An HR team is piloting a RAG assistant that answers policy questions for employees. In the first week
it cited a source that didn't exist, and once answered a question about the CEO's salary from a
learning-budget document. The HR head is clear: *"if it can't show where the answer came from, it
shouldn't answer."*

You're building the check that runs before any answer reaches an employee.

## What you'll build

- `cited_ids()`: pull the `[1]`, `[2]` style citations out of an answer, in order, without repeats
- `citation_problems()`: flag answers that cite nothing, or cite a source that wasn't retrieved
- `should_refuse()`: refuse when retrieval came back empty or the best score is below a threshold
- `final_answer()`: what the employee actually sees, the answer or a polite refusal

You edit [`sources.py`](sources.py). The six real-looking answers are in [`cases.py`](cases.py)
(don't edit it). The tests in [`test_sources.py`](test_sources.py) check each case.

## Done means

- [ ] `python quest.py 36` is all green (4 checks)
- [ ] You can explain why the CEO salary answer is refused even though its citation looks valid
- [ ] You can say why a correct answer with no citations still gets refused

## Run it

```bash
python quest.py 36   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Check that each cited source actually supports its sentence (start with simple word overlap)
- Add query rewriting: before refusing, rewrite the question once and retry retrieval
- Tune the threshold on more cases and show how many good answers each value throws away

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day36
git commit -m "Mini-project 36: citation checker"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
