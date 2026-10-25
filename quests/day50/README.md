# Mini-project 50 · Guardrails for a support bot

**Day 50 · about 30 minutes · regex, PII redaction, cost limits**

## The brief

A fintech support team in Bengaluru is putting an AI assistant in front of customers. Customers paste
Aadhaar numbers, PAN cards and phone numbers into chat, and none of that should end up in prompts or logs.
Last month a test agent also got stuck in a loop and ran up a bill. The compliance lead's ask: *"no
personal data in the logs, a hard stop on runaway runs, and nothing that sounds like a promise goes out."*

You're building those guardrails, in plain code around the model.

## What you'll build

- A `redact()` that swaps Aadhaar numbers, PAN numbers, Indian mobile numbers and emails for placeholders like `[PAN]`
- A `Budget` that counts steps and rupees and stops the run with a clear "steps" or "cost" error once a limit is crossed
- A `check_draft()` that flags a reply before it's sent if it has personal data or promises like "guarantee"

You edit [`rails.py`](rails.py). The tests in [`test_rails.py`](test_rails.py) check real-looking
Indian IDs, a runaway run and two draft replies.

## Done means

- [ ] `python quest.py 50` is all green (3 checks)
- [ ] You can explain why Aadhaar has to be redacted before phone numbers
- [ ] You can say why these rails are plain code and not another model call

## Run it

```bash
python quest.py 50   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Add rules for UPI IDs and bank IFSC codes, with tests for numbers that look close but shouldn't match
- Wrap a real model call so every prompt is redacted on the way in and every reply is checked on the way out
- Write a small logging filter that runs `redact()` on every log line, and show a before and after

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day50
git commit -m "Mini-project 50: guardrails"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
