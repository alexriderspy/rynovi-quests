# Mini-project 60 · Streaming chat endpoint with FastAPI

**Day 60 · about 30 minutes · FastAPI, server-sent events, timeouts**

## The brief

An edtech startup has a doubt-solving assistant for students. Answers take up to 20 seconds, and the app
shows a spinner the whole time, so students close it before the reply arrives. Their product manager puts
it simply: *"show the words as they come, like ChatGPT does, and never let one request hang forever."*

You're building that endpoint.

## What you'll build

- `GET /health` that answers `{"status": "ok"}`, so a load balancer knows the service is alive
- `GET /stream?q=...` that sends the model's reply word by word as server-sent events, and ends with
  `data: [DONE]`
- A 2-second time limit on each request: once it passes, the stream sends `data: [TIMEOUT]` and stops

You edit [`app.py`](app.py). The tests in [`test_app.py`](test_app.py) call the health check, read the
stream event by event, and time a slow request.

## Done means

- [ ] `python quest.py 60` is all green (3 checks)
- [ ] You've watched the words arrive one by one with `curl -N`
- [ ] You can explain what the blank line after each `data:` line is for

## Run it

```bash
python quest.py 60                          # checks your work and points at the next TODO
fastapi dev quests/day60/app.py             # run it for real
curl -N "localhost:8000/stream?q=hello"     # in a second terminal: watch the tokens stream in
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Build a tiny HTML page that reads the stream with `EventSource` and types the answer onto the screen
- Swap `fake_llm()` for a real model's streaming API and keep the same timeout and `[DONE]` contract
- Log how long each request took to its first token and to the end, and expose the numbers on `/health`

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day60
git commit -m "Mini-project 60: streaming endpoint"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
