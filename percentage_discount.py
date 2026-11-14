from discount_strategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.__percentage = percentage
    def apply(self, order_total: float) -> float:
        return order_total * (100 - self.__percentage)/ 100