# TC-FR003-UT010: Verify user can proceed to checkout when cart contains items

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_proceed_to_checkout_with_items(client):
    """
    Test Case: TC-FR003-UT010
    Requirement: FR-003
    Scenario: FR-003-TS001 (User proceeds to checkout with items in cart)
    Title: Verify user can proceed to checkout when cart contains items
    Preconditions: Cart contains:
      - **_The Great Gatsby_** (Quantity: 1)
    Steps:
      - Add **_The Great Gatsby_** (q = 1) to cart
      - Call proceed_to_checkout() function
    Expected Result:
      - Checkout page loads successfully
      - Cart contents (**_The Great Gatsby_**, q = 1) are carried forward
    """

    # Reset cart before test
    cart.clear()

    # Add **_The Great Gatsby_** with quantity = 1
    client.post("/add-to-cart", data={"title": "The Great Gatsby", "quantity": 1}, follow_redirects=True)

    # Proceed to checkout
    response = client.get("/checkout", follow_redirects=True)
    html = response.data.decode()

    # Verify checkout page loads successfully
    assert response.status_code == 200
    assert "Checkout" in html or "Proceed to Checkout" in html

    # Verify cart contents carried forward
    assert "The Great Gatsby" in html
    assert "Quantity: 1" in html or "1 item" in html
