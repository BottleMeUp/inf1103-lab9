from order import Order
from physical_product import PhysicalProduct
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from supplier import Supplier

supplier = Supplier("S001", "ABC@gmail.com", "ABC Supplier")

product1 = PhysicalProduct(
    "P001", "Laptop", 100.00, 10, 2.5, supplier
)

product2 = PhysicalProduct(
    "P002", "Mouse", 50.00, 10, 0.2, supplier
)

order = Order("O001", BulkDiscount(200,20))
order.add_order_line(product1, 2)
order.add_order_line(product2, 1)

print("Actual total:", order.calculate_total())

print("Testing BulkDiscount")
order.set_discount(PercentageDiscount(10))

print("\nTesting PercentageDiscount")
print("Actual total:", order.calculate_total())