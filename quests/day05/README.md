# Mini-project 5 · Test suite for a shopping cart

**Day 5 · about 35 minutes · pytest, fixtures, edge cases**

## The brief

A small online store keeps shipping cart bugs to customers. Last month people got charged shipping on
orders that should have been free, and before that a coupon could be used twice. The code itself is
short; the problem is there are no tests. The tech lead's message: *"I don't need more code. I need tests
that would have caught these before they went live."*

You're writing that test suite. The rules are at the top of [`cart.py`](cart.py), and we've planted 3
bugs in 3 copies of the cart for your tests to find.

## What you'll build

- Tests that pass on the real cart, so they don't raise false alarms
- A test that catches a cart that forgets about quantities
- A test right at the free-shipping line, where `500` exactly should ship free
- A test that catches a coupon being used twice

You edit [`test_my_cart.py`](test_my_cart.py), not the cart. Your tests use the `Cart` fixture from
[`conftest.py`](conftest.py), and `python quest.py 5` swaps in each buggy cart to see if your tests notice.

## Done means

- [ ] `python quest.py 5` is all green (4 checks: your tests pass on the real cart, and catch all 3 bugs)
- [ ] You found the bugs from the rules in `cart.py`, without opening the buggy copies
- [ ] You can explain why testing right at a boundary (like `500`) catches bugs that "a big order" wouldn't

## Run it

```bash
python quest.py 5   # runs your tests on the real cart and on each buggy one
```

## Make it yours (optional)

Pick one to turn this into something you'd show in an interview:

- Use `@pytest.mark.parametrize` to test many carts in one test, including totals just under and over 500
- Add tests for the rest of the spec: `qty=0`, an unknown coupon code, and rounding in `total()`
- Run `pytest --cov` (with `pytest-cov`) on the real cart and get to 100% line coverage

## Put it on your GitHub

You're working in your own fork of this repo, so this mini-project lives on your GitHub:

```bash
git add quests/day05
git commit -m "Mini-project 5: shopping cart tests"
git push
```

Then add one line about it to your fork's top README under **My mini-projects**.
