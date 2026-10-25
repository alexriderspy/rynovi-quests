# Mini-project 41 · Fixing tools for an order agent

**Day 41 · about 35 minutes · JSON schema, argument validation, tool errors**

## The brief

An e-commerce support agent keeps calling its tools wrong: it invents arguments, passes numbers
where text is expected, and when an order id is wrong the whole run crashes. The model isn't the problem,
the tools are. Your lead puts it simply: *"the tool definition is the only manual the model gets. Write
a better one."*

You're fixing the tools, so the model can use them and recover when it gets them wrong.

## What you'll build

- A clear `search_policies` tool definition, with a useful description, typed inputs and an enum
- `validate_args()`: catch missing, unknown, wrongly typed and out-of-enum arguments before the tool runs
- `call_get_order()`: never raise, and return errors with a hint that tells the model what to do next

You edit [`tools.py`](tools.py). The tests in [`test_tools.py`](test_tools.py) check the definition,
the validation and the error messages.

## Done means

- [ ] `python quest.py 41` is all green (3 checks)
- [ ] You can explain why `True` must not count as an integer here
- [ ] You can say what makes an error message something a model can act on

## Run it

```bash
python quest.py 41   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Plug `call_get_order` into your Day 40 loop and script a model that fixes its arguments after an error
- Extend `validate_args` to check the items inside arrays and nested objects
- Generate the input schema from a Pydantic model and compare it with the one you wrote by hand

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day41
git commit -m "Mini-project 41: tool doctor"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
