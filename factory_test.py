"""
Simple tests for Lab 9, Section 3 (ProductFactory).
Run with:  python factory_test.py
"""
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory

# Stand-in supplier: the factory only passes it through to the product.
# Replace with a real Supplier(...) if your Product checks its type.
supplier = object()

print("--- 3.2 ProductFactory.create ---")

physical = ProductFactory.create("physical", "P001", "Desk Lamp", 25.0, 10,
                                 supplier, weight=2.5)
print("'physical' creates a PhysicalProduct", isinstance(physical, PhysicalProduct))

digital = ProductFactory.create("digital", "D001", "Photo Editor", 49.9, 100,
                                supplier, download_size=350.0)
print("'digital' creates a DigitalProduct", isinstance(digital, DigitalProduct))

print("\n--- 3.3 Returned type is Product ---")
print("physical result is a Product", isinstance(physical, Product))
print("digital result is a Product", isinstance(digital, Product))

print("\n--- Values passed in are stored ---")
print("product ID is P001", physical.get_product_id() == "P001")
print("name is Desk Lamp", physical.get_name() == "Desk Lamp")
print("price is 25.0", physical.get_price() == 25.0)
print("stock is 10", physical.get_stock() == 10)

print("\n--- Unknown type ---")
try:
    ProductFactory.create("service", "S001", "Installation", 30.0, 5, supplier)
    print("'service' raises ValueError", False)
except ValueError as error:
    print("'service' raises ValueError", True)
    print("error message mentions 'service'", "service" in str(error))
    print(f"      (message was: {error})")

