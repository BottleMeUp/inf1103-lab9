from discount_strategy import DiscountStrategy

class NoDiscount(DiscountStrategy):
    def apply(self, order_total):
        print("No Discount Applied")
        return order_total

