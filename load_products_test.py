"""
Simple tests for Lab 9, Section 5.2 (load_products).
Needs products.csv in the same folder as this file.
Run with:  python load_products_test.py
"""
import contextlib
import io
import os

# Change 'helpers' to the file where load_products() lives.
from helpers import load_products

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "products.csv")


class FakeInventory:
    """Just collects products, so the test doesn't depend on your Inventory class."""
    def __init__(self):
        self.products = []

    def add_product(self, product) -> None:
        self.products.append(product)


def run_load(path: str):
    """Call load_products and return (inventory, everything it printed)."""
    inventory = FakeInventory()
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        load_products(path, inventory, object())  # object() stands in for a Supplier
    return inventory, buffer.getvalue()


# ---------------- products.csv exists ----------------
print("Test 1: products.csv exists")
inventory, output = run_load(CSV_PATH)
ids = [p.get_product_id() for p in inventory.products]

assert len(inventory.products) == 3, f"expected 3 products, got {len(inventory.products)}"
assert ids == ["P001", "D001", "P003"], f"wrong products loaded: {ids}"
assert "service" in output, "service row was not reported"
assert "abc" in output, "abc price row was not reported"
assert "3 products loaded." in output, "missing '3 products loaded.'"
assert "Load attempt finished." in output, "missing 'Load attempt finished.'"
assert output.find("3 products loaded.") < output.find("Load attempt finished."), \
    "count should print before the finished message"
print("  passed")
print("  output was:")
print("  " + output.strip().replace("\n", "\n  "))

# ---------------- file missing ----------------
print("\nTest 2: file does not exist")
missing = os.path.join(os.path.dirname(CSV_PATH), "no_such_file.csv")
inventory, output = run_load(missing)

assert "not found" in output.lower(), "missing 'not found' message"
assert len(inventory.products) == 0, "nothing should be loaded"
assert "Load attempt finished." in output, "finally block did not run"
assert "products loaded" not in output, "else block should not run"
print("  passed")
print("  output was:")
print("  " + output.strip().replace("\n", "\n  "))

print("\nAll tests passed.")