# TC-FR002-UT002: Verify item is removed from the cart if a user sets the quantity to 0 or negative

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_remove_item_when_quantity_zero_or_negative(client):
    """
    Test Case: TC-FR002-UT002
    Requirement: FR-002
    Scenario: FR-002-TS002
    Title: Verify item is removed from the cart if a user sets the quantity to 0 or negative
    Steps:
      - Navigate to catalogue
      - Add 'I Ching' to cart with quantity = 1
      - Go to cart page
      - Update quantity of 'I Ching' to 0
      - Re-add 'I Ching' to cart with quantity = 1
      - Update quantity of 'I Ching' to -1
    Expected Result:
      - When quantity = 0: Flash message confirms removal, 'I Ching' no longer in cart
      - When quantity = -1: Validation error shown, 'I Ching' not added to cart
    """

    # Reset cart before test
    cart.clear()

    # Add I Ching to cart
    client.post("/add-to-cart", data={"title": "I Ching", "quantity": 1}, follow_redirects=True)

    # Update quantity to 0
    response_zero = client.post("/update-cart", data={"title": "I Ching", "quantity": 0}, follow_redirects=True)
    html_zero = response_zero.data.decode()

    # Validate removal message
    assert "Removed" in html_zero
    assert "I Ching" in html_zero

    # Ensure cart is empty
    cart_response = client.get("/cart")
    assert "I Ching" not in cart_response.data.decode()

    # Re-add I Ching
    client.post("/add-to-cart", data={"title": "I Ching", "quantity": 1}, follow_redirects=True)

    # Update quantity to -1
    response_neg = client.post("/update-cart", data={"title": "I Ching", "quantity": -1}, follow_redirects=True)
    html_neg = response_neg.data.decode()

    # Validate error message (depending on your template wording)
    assert "Quantity must be positive" in html_neg or "Invalid quantity" in html_neg

    # Ensure cart is still empty after invalid update
    cart_response = client.get("/cart")
    assert "I Ching" not in cart_response.data.decode()
