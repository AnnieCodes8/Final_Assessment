# TC-FR002-UT006: Verify user can remove an item from the cart

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_remove_item_from_cart(client):
    """
    Test Case: TC-FR002-UT006
    Requirement: FR-002
    Title: Verify user can remove an item from the cart
    Preconditions: Cart contains **_The Great Gatsby_** (Quantity: 1)
    Steps:
      - Add **_The Great Gatsby_** (q = 1) to cart
      - Call remove_from_cart(**_The Great Gatsby_**)
    Expected Result:
      - **_The Great Gatsby_** is removed from the cart
      - Cart is empty
    """

    # Reset cart before test
    cart.clear()

    # Add **_The Great Gatsby_** with quantity = 1
    client.post("/add-to-cart", data={"title": "The Great Gatsby", "quantity": 1}, follow_redirects=True)

    # Remove **_The Great Gatsby_** from the cart
    client.post("/remove-from-cart", data={"title": "The Great Gatsby"}, follow_redirects=True)

    # Verify cart is empty
    cart_response = client.get("/cart")
    cart_html = cart_response.data.decode()
    assert "The Great Gatsby" not in cart_html
    assert "Your cart is empty" in cart_html or "0 items" in cart_html
