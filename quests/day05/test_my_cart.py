"""Day 5 · Bug hunt

We planted 3 bugs in 3 copies of the cart. Write tests here, using the `Cart` fixture,
that pass on the real cart (cart.py) but fail on each buggy copy.

Read the rules at the top of cart.py, then test them, including the edges.
Run `python quest.py 5` to see which bugs you've caught.
"""
import pytest  # noqa: F401


def test_add_one_item(Cart):
    cart = Cart()
    cart.add("notebook", 120)
    assert cart.subtotal() == 120


# TODO 5.1 · Write a test that would catch a cart that forgets quantities.
# TODO 5.2 · Write a test right at the free-shipping line.
# TODO 5.3 · Write a test for using the coupon twice.
