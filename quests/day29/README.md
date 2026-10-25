# Mini-project 29 · Chat templates by hand

**Day 29 · about 30 minutes · chat templates, special tokens, conversation checks**

## The brief

Your team fine-tuned a small model to label support issues, and in testing it acts strangely: it rambles,
ignores the system prompt, or keeps writing the user's next message. After a day of digging, the cause is
a training script that glued messages together in the wrong format. Your lead wants it fixed for good:
*"write the formatter yourself, so we know exactly what string the model sees."*

You're building that formatter for the two formats your team uses, ChatML and Llama 3, plus a check that
rejects broken conversations before they reach training.

## What you'll build

- `chatml()`, which turns a list of messages into the exact ChatML string with `<|im_start|>` and `<|im_end|>`
- The generation prompt: an option that ends the string with the assistant's header, so the model knows it's its turn
- `llama3()`, which builds the same conversation in the Llama 3 format with `<|begin_of_text|>` and header tokens
- `check_conversation()`, which raises an error for unknown roles, a system message that isn't first, or turns out of order

You edit [`templates.py`](templates.py). The tests in [`test_templates.py`](test_templates.py) compare your
output with the exact strings, character by character.

## Done means

- [ ] `python quest.py 29` is all green (4 checks)
- [ ] You can explain what goes wrong if you forget the generation prompt at inference time
- [ ] You can say why the same messages need a different string for a different model

## Run it

```bash
python quest.py 29   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Compare your `chatml()` with `tokenizer.apply_chat_template()` from `transformers` for a small Qwen model, and show they match
- Add a third format, such as Gemma's, from its model card, with its own test
- Tokenize both formats (Day 28's tokenizers) and count how many tokens the template itself adds per message

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day29
git commit -m "Mini-project 29: chat templates by hand"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
