from discount_strategy import DiscountStrategy

class NoDiscount(DiscountStrategy):
    def apply(self, order_total: float) -> float:
        print("No Discount Applied")
        return order_total

