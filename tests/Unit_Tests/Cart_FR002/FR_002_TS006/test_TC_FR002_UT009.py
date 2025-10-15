# TC-FR002-UT009: Verify cart summary updates correctly after item removal

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_cart_summary_updates_after_item_removal(client):
    """
    Test Case: TC-FR002-UT009
    Requirement: FR-002
    Scenario: FR-002-TS006 (Dynamic pricing updates totals in real time)
    Title: Verify cart summary updates correctly after item removal
    Preconditions: Cart contains multiple items:
      - **_I Ching_** (Price: £18.99, Quantity: 1)
      - **_1984_** (Price: £8.99, Quantity: 2)
    Steps:
      - Add **_I Ching_** (q = 1) to cart
      - Add **_1984_** (q = 2) to cart
      - Remove **_I Ching_**
      - Call view_cart_summary()
    Expected Result:
      - Cart summary shows 1 line item (**_1984_** only)
      - Total quantity = 2
      - Total price = £17.98
    """

    # Reset cart before test
    cart.clear()

    # Add **_I Ching_** with quantity = 1
    client.post("/add-to-cart", data={"title": "I Ching", "quantity": 1}, follow_redirects=True)

    # Add **_1984_** with quantity = 2
    client.post("/add-to-cart", data={"title": "1984", "quantity": 2}, follow_redirects=True)

    # Remove **_I Ching_**
    client.post("/remove-from-cart", data={"title": "I Ching"}, follow_redirects=True)

    # View cart summary
    response = client.get("/cart")
    html = response.data.decode()

    # Verify **_I Ching_** is gone
    assert "I Ching" not in html

    # Verify **_1984_** remains
    assert "1984" in html

    # Verify totals: quantity = 2, price = £17.98
    assert "Total Items: 2" in html or "Quantity: 2" in html
    assert "17.98" in html  # formatted total price
