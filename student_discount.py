from discount_strategy import DiscountStrategy

class StudentDiscount(DiscountStrategy):
    def apply(self, order_total:float) -> float:
        return order_total * 0.95