from discount_strategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float):
        if threshold < 0:
            raise ValueError("Threshold must not be negative")
        if amount < 0:
            raise ValueError("Discount amount must not be negative")

        self.__threshold = threshold
        self.__amount = amount

    def apply(self, order_total: float) -> float | None:
        if order_total > self.__threshold:
            return max(0.0, order_total - self.__amount)
        return order_total
 
