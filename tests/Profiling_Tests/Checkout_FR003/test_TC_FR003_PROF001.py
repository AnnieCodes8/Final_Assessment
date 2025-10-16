# TC-FR003-PROF001: Profile checkout function for bottlenecks

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


def simulate_checkout(n=100000):
    """
    Simulate a checkout process:
    - Create a cart
    - Add n items
    - Calculate total price (checkout step)
    """
    cart = Cart()
    book = DummyBook()
    for _ in range(n):
        cart.add_book(book, 1)
    return cart.get_total_price()


def test_profile_checkout():
    """
    Test Case: TC-FR003-PROF001
    Requirement: FR-003
    Title: Profile checkout function for bottlenecks
    Preconditions:
      - Cart class available
    Steps:
      1. Simulate checkout with many items.
      2. Profile checkout (get_total_price) using cProfile.
      3. Save profiling results to test_results folder.
    Expected Result:
      - Profile output shows where time is spent.
      - No unexpected bottlenecks in checkout processing.
    """

    pr = cProfile.Profile()
    pr.enable()
    # Run multiple times to amplify workload
    for _ in range(5):
        _ = simulate_checkout(20000)
    pr.disable()

    # Capture stats into a string
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.print_stats(15)  # show top 15 functions

    output = s.getvalue()
    print("\n--- cProfile Results for Checkout (get_total_price) ---")
    print(output)

    # Save results to test_results folder
    results_dir = os.path.join("test_results", "Profiling_Tests", "Checkout_FR003")
    os.makedirs(results_dir, exist_ok=True)
    results_file = os.path.join(results_dir, "FR003_PROF001_results.txt")

    with open(results_file, "w") as f:
        f.write(output)

    # Basic assertion: ensure profiling captured calls
    assert ps.total_calls > 0
