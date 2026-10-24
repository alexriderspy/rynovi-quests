"""A planted bug. No peeking until you've caught it! Run python quest.py 5."""
class Cart:
    def __init__(self) -> None:
        self.items: list[tuple[str, float, int]] = []
        self.discount = 0.0

    def add(self, name: str, price: float, qty: int = 1) -> None:
        if qty < 1:
            raise ValueError("qty must be at least 1")
        self.items.append((name, price, qty))

    def subtotal(self) -> float:
        return sum(price for _, price, qty in self.items)

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
