# TC-FR002-PERF001: Measure execution time for adding a book to the cart

import timeit
import pytest

from models import Cart


# Dummy Book class for testing
class DummyBook:
    def __init__(self, title="Book A", price=10.0):
        self.title = title
        self.price = price


def add_book_operation():
    """Helper function to simulate adding a book to the cart."""
    cart = Cart()
    book = DummyBook()
    cart.add_book(book, 1)


def test_add_book_to_cart_performance():
    """
    Test Case: TC-FR002-PERF001
    Requirement: FR-002
    Title: Measure execution time for adding a book to the cart using timeit
    Preconditions:
      - Cart class available
    Steps:
      1. Use timeit to measure execution time of add_book operation.
    Expected Result:
      - Execution time per operation is within acceptable threshold (e.g. < 1 ms).
    """

    # Run the add_book_operation 1000 times
    total_time = timeit.timeit("add_book_operation()", globals=globals(), number=1000)
    avg_time = total_time / 1000

    print(f"\nAverage execution time per add_book: {avg_time:.6f} seconds")

    # Example threshold: 1 millisecond per operation
    assert avg_time < 0.001, f"add_book too slow: {avg_time:.6f} seconds"
