# Mini-project 44 · LangGraph router with checkpoints

**Day 44 · about 40 minutes · LangGraph, conditional edges, checkpoints**

## The brief

Your team's assistant has grown into a tangle of if-statements, and when a long run fails halfway
it starts again from zero. Your lead wants to move it to LangGraph: *"one graph we can read, a clear
branch for each kind of question, and runs we can pause and pick up later."*

You're building a small version of that graph to prove the idea.

## What you'll build

- Three nodes: `classify` picks a route, `math` adds up the numbers, `chat` handles everything else
- A `StateGraph` with a conditional edge that sends each question down the right branch
- A run that pauses before the `math` node and resumes from its checkpoint

You edit [`graph.py`](graph.py). The tests in [`test_graph.py`](test_graph.py) run your graph, including
a paused run with `InMemorySaver`.

## Done means

- [ ] `python quest.py 44` is all green (3 checks)
- [ ] You can explain what the `steps` reducer (`operator.add`) does when two nodes both return `steps`
- [ ] You can say what `thread_id` is for when resuming a run

## Run it

```bash
pip install langgraph   # already in requirements.txt
python quest.py 44      # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Print your graph with `build_graph().get_graph().draw_mermaid()` and add the diagram to this README
- Add an approval step that pauses before an answer goes out (a preview of Day 49, Human-in-the-loop approvals)
- Swap `InMemorySaver` for a SQLite checkpointer (`pip install langgraph-checkpoint-sqlite`) so a paused run survives a restart

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day44
git commit -m "Mini-project 44: LangGraph router"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
