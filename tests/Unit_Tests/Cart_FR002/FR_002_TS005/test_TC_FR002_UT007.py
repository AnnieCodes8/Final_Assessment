# TC-FR002-UT007: Verify user can clear all items from the cart

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_clear_all_items_from_cart(client):
    """
    Test Case: TC-FR002-UT007
    Requirement: FR-002
    Title: Verify user can clear all items from the cart
    Preconditions: Cart contains multiple items:
      - **_I Ching_** (Quantity: 1)
      - **_Moby Dick_** (Quantity: 2)
    Steps:
      - Add **_I Ching_** (q = 1) to cart
      - Add **_Moby Dick_** (q = 2) to cart
      - Call clear_cart() function
    Expected Result:
      - All items are removed from the cart
      - Cart is empty (no books remain)
    """

    # Reset cart before test
    cart.clear()

    # Add **_I Ching_** with quantity = 1
    client.post("/add-to-cart", data={"title": "I Ching", "quantity": 1}, follow_redirects=True)

    # Add **_Moby Dick_** with quantity = 2
    client.post("/add-to-cart", data={"title": "Moby Dick", "quantity": 2}, follow_redirects=True)

    # Clear the cart
    client.post("/clear-cart", follow_redirects=True)

    # Verify cart is empty
    cart_response = client.get("/cart")
    cart_html = cart_response.data.decode()
    assert "I Ching" not in cart_html
    assert "Moby Dick" not in cart_html
    assert "Your cart is empty" in cart_html or "0 items" in cart_html
