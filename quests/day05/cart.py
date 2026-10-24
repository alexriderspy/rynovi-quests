"""Day 5 · The shopping cart under test. Don't edit this file: write tests for it.

The rules (this is the spec your tests should check):
  - add(name, price, qty=1): qty must be at least 1, otherwise ValueError.
  - subtotal(): the sum of price × qty for every item.
  - apply_coupon("SAVE10"): 10% off the subtotal. It works once; a second call raises ValueError.
    Any other code raises ValueError.
  - shipping(): free (0) when the discounted subtotal is 500 or more, otherwise 40.
  - total(): discounted subtotal + shipping, rounded to 2 decimals.
"""


class Cart:
    def __init__(self) -> None:
        self.items: list[tuple[str, float, int]] = []
        self.discount = 0.0

    def add(self, name: str, price: float, qty: int = 1) -> None:
        if qty < 1:
            raise ValueError("qty must be at least 1")
        self.items.append((name, price, qty))

    def subtotal(self) -> float:
        return sum(price * qty for _, price, qty in self.items)

    def apply_coupon(self, code: str) -> None:
        if code != "SAVE10":
            raise ValueError("unknown coupon")
        if self.discount:
            raise ValueError("coupon already applied")
        self.discount = 0.10

    def discounted(self) -> float:
        return self.subtotal() * (1 - self.discount)

    def shipping(self) -> float:
        return 0 if self.discounted() >= 500 else 40

    def total(self) -> float:
        return round(self.discounted() + self.shipping(), 2)
