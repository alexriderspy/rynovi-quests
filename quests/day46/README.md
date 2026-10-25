# Mini-project 46 · MCP server for support tickets

**Day 46 · about 35 minutes · MCP, FastMCP, tools and resources**

## The brief

A support team uses AI assistants in different apps, and each one needs its own custom code to reach the
ticket system. The platform lead wants one integration that any MCP client can use: *"write it once, as an
MCP server, and let every assistant plug in."*

You're building that server, with the official Python SDK.

## What you'll build

- A read tool, `open_tickets`, that lists a customer's open tickets
- A write tool, `create_ticket`, whose priority is limited to `low` or `high`
- A resource, `tickets://{ticket_id}`, that returns one ticket as JSON

You edit [`server.py`](server.py). The tests in [`test_server.py`](test_server.py) connect a real MCP client
to your server and call it.

## Done means

- [ ] `python quest.py 46` is all green (3 checks)
- [ ] You've opened your server in the MCP Inspector and called each tool by hand
- [ ] You can explain when something should be a tool and when it should be a resource

## Run it

```bash
pip install "mcp<2"            # already in requirements.txt
python quest.py 46             # checks your work and points at the next TODO
mcp dev quests/day46/server.py # try it by hand in the MCP Inspector
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Connect your server to an MCP client you use, like Claude Desktop or Claude Code, and add a screenshot here
- Add a `close_ticket` tool that refuses to close a ticket that's already closed, with a clear error
- Store tickets in SQLite instead of a dict, so new tickets survive a restart

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day46
git commit -m "Mini-project 46: MCP server"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
