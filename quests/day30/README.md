# Mini-project 30 · LoRA from scratch

**Day 30 · about 45 minutes · NumPy, fine-tuning, parameter maths**

## The brief

Your team wants to fine-tune a 1B-parameter model on a single laptop GPU. Full fine-tuning won't fit in
memory, so your lead says *"just use LoRA"*, and then asks you to explain to the rest of the team how much
it actually saves and why it doesn't change the model's behaviour before training starts.

Instead of a slide, you build a LoRA layer yourself, in plain NumPy, and let the numbers make the case.

## What you'll build

- A parameter counter: how many numbers LoRA trains for one layer, against full fine-tuning
- A `LoRALinear` layer that wraps a frozen weight matrix and starts as an exact no-op
- A `merge()` step that folds the trained update back into one matrix, so serving costs nothing extra
- A budget calculator for LoRA on the attention projections of a whole 1B model

You edit [`lora.py`](lora.py). The tests in [`test_lora.py`](test_lora.py) check the maths, the no-op
start and the merge.

## Done means

- [ ] `python quest.py 30` is all green (4 checks)
- [ ] You can say, for a 1B model, roughly what fraction of the parameters LoRA trains at rank 8
- [ ] You can explain why `B` starts at zero

## Run it

```bash
python quest.py 30   # checks your work and points at the next TODO
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Plot trainable parameters against rank (r = 1 to 64) for a 1B and a 7B model, and add the chart to this README
- Train your layer on a toy regression task with gradient descent and show the loss going down
- Compare your numbers with what `peft` reports for a real model (`model.print_trainable_parameters()`)

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day30
git commit -m "Mini-project 30: LoRA from scratch"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
