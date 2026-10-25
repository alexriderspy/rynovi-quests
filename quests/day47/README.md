# Mini-project 47 · MCP client for a weather server

**Day 47 · about 35 minutes · MCP, async Python, tool schemas**

## The brief

A travel startup in Pune has a small MCP server that reports the weather in Indian cities. Their support
bot needs to use it, but nobody wants to hand-write a tool definition for every server they add later.
The lead says: *"if a server can describe its own tools, our code should just ask it."*

You're building that client: it starts the server, finds its tools, calls them, and hands them to a model.

## What you'll build

- A client that starts the server as its own process over stdio, initializes a session and lists the tool names
- A `call()` function that runs one tool with arguments and returns the text of its result
- A converter that turns the server's tools into the `name`, `description`, `input_schema` format the Claude API expects

You edit [`client.py`](client.py). The tests in [`test_client.py`](test_client.py) start the real
[`weather_server.py`](weather_server.py) and talk to it through your client.

## Done means

- [ ] `python quest.py 47` is all green (3 checks)
- [ ] You can explain why the client must call `session.initialize()` before anything else
- [ ] You can say where a tool's `input_schema` comes from, without looking at the server code

## Run it

```bash
pip install "mcp<2"   # the official MCP Python SDK
python quest.py 47    # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Close the loop: send `tools_for_model()` to a real model, run whatever tool it asks for through `call()`, and print the final answer (Day 40's agent loop)
- Point your client at the server you wrote on Day 46 and show that the same code works with no changes
- Connect to two servers at once and merge their tools into one list, prefixing names so they never clash

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day47
git commit -m "Mini-project 47: MCP client"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
