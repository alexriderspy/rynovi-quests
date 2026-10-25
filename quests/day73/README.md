# Mini-project 73 · Output filter against data leaks

**Day 73 · about 30 minutes · prompt injection, Markdown parsing, secret detection**

## The brief

An HR software company's chat assistant renders model replies as Markdown. During a security review, a
tester hid an instruction in a document that made the model write an image link with salary data in the
URL. The chat window loaded the image, and the data reached the tester's server without anyone clicking
anything. Their security lead's fix: *"check every reply before it renders."*

You're building that check.

## What you'll build

- A `find_urls()` that pulls every image and link out of a Markdown reply, in order
- A `problems()` check that flags images and links to domains outside an allow-list, and any API key that
  slipped into the reply
- A `sanitise()` step that removes bad images, turns bad links into plain text and hides secrets, while
  leaving allowed images and links as they were

You edit [`leaks.py`](leaks.py). The tests in [`test_leaks.py`](test_leaks.py) run a real-looking attack
reply through each step.

## Done means

- [ ] `python quest.py 73` is all green (3 checks)
- [ ] You can explain why an image is more dangerous than a link here
- [ ] You can say why an allow-list of domains is safer than a block-list

## Run it

```bash
python quest.py 73   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Add raw HTML `<img>` tags and autolinks like `<https://...>` to what you catch
- Wire `sanitise()` into the streaming endpoint from Day 60 so no unsafe reply ever reaches the browser
- Collect ten attack replies, including ones from Day 72's prompt injections, and keep them as a test set

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day73
git commit -m "Mini-project 73: output leak filter"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
