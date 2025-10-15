# TC-FR002-UT004: Verify system prevents non-integer quantity updates

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_prevent_non_integer_quantity_update(client):
    """
    Test Case: TC-FR002-UT004
    Requirement: FR-002
    Title: Verify system prevents non-integer quantity updates
    Preconditions: Cart contains **_Moby Dick_** (Quantity: 1)
    Steps:
      - Add **_Moby Dick_** (q = 1) to cart
      - Attempt to update **_Moby Dick_** to q = '@'
      - Call update_cart() function
    Expected Result:
      - System displays validation error
      - **_Moby Dick_** remains in cart with Quantity = 1
    """

    # Reset cart before test
    cart.clear()

    # Add **_Moby Dick_** with quantity = 1
    client.post("/add-to-cart", data={"title": "Moby Dick", "quantity": 1}, follow_redirects=True)

    # Attempt to update **_Moby Dick_** with a non-integer quantity
    response = client.post("/update-cart", data={"title": "Moby Dick", "quantity": "@"}, follow_redirects=True)
    html = response.data.decode()

    # Validate error message (depending on template wording)
    assert "Invalid quantity" in html or "must be a number" in html

    # Ensure **_Moby Dick_** is still in the cart with quantity = 1
    cart_response = client.get("/cart")
    cart_html = cart_response.data.decode()
    assert "Moby Dick" in cart_html
    assert "Quantity: 1" in cart_html or ">1<" in cart_html
