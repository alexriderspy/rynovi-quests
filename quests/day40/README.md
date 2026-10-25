# Mini-project 40 · Agent loop from scratch

**Day 40 · about 30 minutes · tool calling, the agent loop, step limits**

## The brief

A startup's first support agent works in demos, then crashes when a tool throws an error, and once
ran up a big API bill by calling tools in circles. Before anyone picks a framework, the tech lead says:
*"I want to see the loop itself. No libraries, just the loop."*

You're building that loop, against a scripted model, so no API key is needed.

## What you'll build

- `run_tool()`: run one tool call and turn the result, or any error, into a tool result the model can read
- `run_agent()`: call the model, run the tools it asks for, send the results back, and stop when it answers
- A step limit, so an agent that never answers stops instead of looping forever

You edit [`loop.py`](loop.py). The pretend model is in [`fake_model.py`](fake_model.py) (don't edit it).
The tests in [`test_loop.py`](test_loop.py) check every message your loop sends back.

## Done means

- [ ] `python quest.py 40` is all green (3 checks)
- [ ] You can draw the message list for one tool call, from the user's question to the final answer
- [ ] You can explain why a tool error goes back to the model instead of crashing the program

## Run it

```bash
python quest.py 40   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Write a small adapter so `run_agent` works with a real model API's tool calling
- Support a reply with several tool calls at once, and send all the results back together
- Log each step (tool name, input, time taken) and print a short trace at the end

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day40
git commit -m "Mini-project 40: agent loop"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
