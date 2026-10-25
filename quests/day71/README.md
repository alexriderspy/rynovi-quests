# Mini-project 71 · PII scanner for project files

**Day 71 · about 30 minutes · regex, PII detection, DPDP Act**

## The brief

A lending startup is getting ready for a data-protection review under India's DPDP Act. Their app database
is locked down, but nobody has checked the logs, traces and eval files their AI team keeps in the repo.
The compliance lead asks: *"tell me every file that has personal data in it, then clean those files up."*

You're building the scanner that answers that, and the clean-up.

## What you'll build

- A `find_pii()` that spots Aadhaar numbers, PAN numbers, phone numbers and email addresses in a piece of
  text
- A `scan()` that walks a project folder and reports which files hold which kinds of personal data
- A `clean()` that rewrites only the files with personal data, replacing each match with a label like
  `[EMAIL]`, so a fresh scan finds nothing

You edit [`scan.py`](scan.py). It runs on the sample project in [`workspace/`](workspace/). The tests in
[`test_scan.py`](test_scan.py) scan that folder and clean a copy of it, so the original stays as it is.

## Done means

- [ ] `python quest.py 71` is all green (3 checks)
- [ ] You can explain why Aadhaar must be replaced before phone numbers
- [ ] You can name two places in an AI project where personal data ends up without anyone noticing

## Run it

```bash
python quest.py 71   # checks your work and points at the next TODO
```

The checks run your `clean()` on a copy of `workspace/`. If you try it yourself, use a copy too: running it on the real folder rewrites the sample files, and the scan check then fails. `git checkout quests/day71/workspace` puts them back.

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Turn the scanner into a pre-commit hook that blocks a commit when it finds personal data
- Add a check for valid Aadhaar numbers (they use the Verhoeff checksum) to cut false positives
- Print an HTML report with each file, the kinds found and the line numbers, for the compliance team

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day71
git commit -m "Mini-project 71: PII scanner"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
