# TC-FR002-PROF001: Profile cart summary function for bottlenecks

import cProfile
import pstats
import io
import os
import pytest
from models import Cart


# Dummy Book class for testing
class DummyBook:
    def __init__(self, title="Book A", price=10.0):
        self.title = title
        self.price = price


def build_large_cart(n=100000):
    """Helper: create a cart with n items for profiling."""
    cart = Cart()
    book = DummyBook()
    for _ in range(n):
        cart.add_book(book, 1)
    return cart


def test_profile_cart_summary():
    """
    Test Case: TC-FR002-PROF001
    Requirement: FR-002
    Title: Profile cart summary function for bottlenecks
    Preconditions:
      - Cart class available
    Steps:
      1. Create a cart with many items (100k).
      2. Profile get_total_price() using cProfile.
      3. Save profiling results to test_results folder.
    Expected Result:
      - Profile output shows where time is spent.
      - No unexpected bottlenecks in get_total_price().
    """

    cart = build_large_cart(100000)

    pr = cProfile.Profile()
    pr.enable()
    # Run multiple times to amplify workload
    for _ in range(5):
        _ = cart.get_total_price()
    pr.disable()

    # Capture stats into a string
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.print_stats(15)  # show top 15 functions

    output = s.getvalue()
    print("\n--- cProfile Results for get_total_price() ---")
    print(output)

    # Save results to test_results folder
    results_dir = os.path.join("test_results", "Profiling_Tests", "Cart_FR002")
    os.makedirs(results_dir, exist_ok=True)
    results_file = os.path.join(results_dir, "FR002_PROF001_results.txt")

    with open(results_file, "w") as f:
        f.write(output)

    # Basic assertion: ensure profiling captured calls
    assert ps.total_calls > 0
