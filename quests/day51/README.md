# Mini-project 51 · Least-privilege tools for agents

**Day 51 · about 35 minutes · permissions, sandboxing, prompt injection**

## The brief

A company runs two agents: one answers support tickets, the other handles billing. During a review, the
security engineer asks three questions: *"can the support bot issue a refund? Can it read files outside its
folder? And does any agent read untrusted content, see private data and send things out, all at once?"*
Nobody can answer with confidence.

You're building the checks that answer all three.

## What you'll build

- An `allowed()` allow-list that says which role may use which tool, and denies unknown roles by default
- A `safe_path()` sandbox that keeps file access inside one folder and blocks `../` tricks and absolute paths
- A `lethal_trifecta()` check that flags an agent with private data, untrusted content and a way to send data out

You edit [`privilege.py`](privilege.py). The tests in [`test_privilege.py`](test_privilege.py) try
escape paths like `notes/../../x` and `/etc/passwd`, and check a risky tool mix.

## Done means

- [ ] `python quest.py 51` is all green (3 checks)
- [ ] You can explain why "deny by default" is safer than listing what's forbidden
- [ ] You can describe how a prompt injection could steal data from an agent with all three flags

## Run it

```bash
python quest.py 51   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Plug `allowed()` into a tool-calling loop so a blocked tool returns a clear error to the model instead of running
- Add a symlink test: create a link inside the folder that points outside, and make sure `safe_path()` still blocks it
- Write a short audit script that runs `lethal_trifecta()` over every agent config in a project and prints a table

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day51
git commit -m "Mini-project 51: least privilege"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
