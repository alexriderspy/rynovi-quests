# Mini-project 68 · Paginated document connector

**Day 68 · about 35 minutes · pagination, rate limits, permissions**

## The brief

A consulting firm wants its assistant to answer from the documents in its shared drive. The drive's API
returns two files at a time and starts refusing calls if you go too fast. Their IT admin has seen
connectors take the API down before: *"get every file, don't hammer us, and don't index anything without
its permissions."*

You're building that connector.

## What you'll build

- A `fetch_all()` that follows the page token from page to page until there are no more, and returns every
  file in order
- Rate-limit handling: when the API says slow down, wait and retry the same page, so no page is ever
  skipped
- A `to_index()` step that drops trashed files and keeps only the id, title and sorted list of who may
  see each one

You edit [`connector.py`](connector.py). It talks to a pretend drive in [`fake_api.py`](fake_api.py)
(don't edit that one). The tests in [`test_connector.py`](test_connector.py) check that you got every
file, how many calls you made, and what goes into the index.

## Done means

- [ ] `python quest.py 68` is all green (3 checks)
- [ ] You can explain why a rate-limited call must retry the same page, not move on
- [ ] You can say what goes wrong if a document is indexed without its permissions

## Run it

```bash
python quest.py 68   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Add exponential backoff with a maximum number of retries, and log each wait (Day 4)
- Save the last page token to disk so a crashed sync picks up where it stopped
- Point the same connector at a real API you have access to, such as the GitHub issues API, which also pages and rate-limits

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day68
git commit -m "Mini-project 68: document connector"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
