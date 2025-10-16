# TC-FR003-PERF001: Measure execution time for processing checkout with many items

import timeit
import pytest
from models import Cart  # clean import with __init__.py in place


# Dummy Book class for testing
class DummyBook:
    def __init__(self, title="Book A", price=10.0):
        self.title = title
        self.price = price


def checkout_operation(n=5000):
    """
    Simulate checkout by:
    - Creating a cart
    - Adding n items
    - Calculating total price (representing checkout processing)
    """
    cart = Cart()
    book = DummyBook()
    for _ in range(n):
        cart.add_book(book, 1)
    # Checkout step: compute total
    _ = cart.get_total_price()


def test_checkout_performance_many_items():
    """
    Test Case: TC-FR003-PERF001
    Requirement: FR-003
    Title: Measure execution time for processing checkout with many items
    Preconditions:
      - Cart class available
    Steps:
      1. Fill cart with 5000 items.
      2. Measure execution time for checkout operation.
    Expected Result:
      - Average execution time per checkout is within acceptable threshold (e.g. < 0.5s).
    """

    total_time = timeit.timeit("checkout_operation()", globals=globals(), number=1)
    print(f"\nExecution time for checkout with 5000 items: {total_time:.6f} seconds")

    # Example threshold: half a second for 5000 items
    assert total_time < 0.5, f"Checkout too slow: {total_time:.6f} seconds"
