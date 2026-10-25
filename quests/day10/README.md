# Mini-project 10 · Invoice reader for PDFs

**Day 10 · about 35 minutes · pdfplumber, regex, tables**

## The brief

A finance team gets vendor invoices as PDFs and types the totals and line items into a sheet by hand.
They want a script to do the first pass. There's a catch: some invoices are proper digital PDFs, some
have the items in a table, and some are just a photo of a page with no text inside at all. The finance
lead says: *"get me the total and the items, and if it's a scan, tell me, so I know it needs a different
tool."*

You're building that first-pass reader, using three sample invoices in [`invoices/`](invoices/).

## What you'll build

- `extract_text()`, which pulls the text out of every page of a PDF
- `find_total()`, which finds the real total with a regex, not the subtotal sitting just above it
- `line_items()`, which reads the table on the first page into rows of item, quantity and amount
- `is_scan()`, which spots a PDF with no text layer, so it can go to OCR or a vision model instead

You edit [`detective.py`](detective.py). The tests in [`test_detective.py`](test_detective.py) run it on the
three invoices and check that the line items add up to the total.

## Done means

- [ ] `python quest.py 10` is all green (4 checks)
- [ ] You can explain why `extract_text()` gives nothing for `scan.pdf` even though you can read it on screen
- [ ] You can say why your total regex doesn't match the subtotal line

## Run it

`pdfplumber` is already in `requirements.txt`. If you skipped that step, `pip install pdfplumber` first.

```bash
python quest.py 10   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Run it over a folder of PDFs and write one CSV row per invoice: file, total, number of items, scan or not
- Add OCR for scans with `pytesseract`, and see if `find_total()` still works on the OCR text
- Pull out the invoice number and date too, and add your own test invoice to the folder

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day10
git commit -m "Mini-project 10: PDF invoice reader"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
