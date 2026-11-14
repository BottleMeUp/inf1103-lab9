from order import Order
from physical_product import PhysicalProduct
from student_discount import StudentDiscount
from supplier import Supplier

supplier = Supplier("S001", "ABC@gmail.com", "ABC Supplier")

product1 = PhysicalProduct(
    "P001", "Laptop", 100.00, 10, 2.5, supplier
)

product2 = PhysicalProduct(
    "P002", "Mouse", 50.00, 10, 0.2, supplier
)

order = Order("O001", StudentDiscount())
order.add_order_line(product1, 2)
order.add_order_line(product2, 1)
print("Testing BulkDiscount")
print("Actual total:", order.calculate_total())