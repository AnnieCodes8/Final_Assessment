# TC-FR002-UT002: Verify empty cart displays appropriate message

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_empty_cart_displays_message(client):
    """
    Test Case: TC-FR002-UT002
    Requirement: FR-002
    Scenario: Verify empty cart displays appropriate message
    Preconditions: User has not added any items to the cart
    Steps:
      - Call view_cart() function with empty cart state
    Expected Result:
      - Function returns "Your cart is empty"
      - No items or totals are shown
    """

    # Reset cart to ensure it's empty
    cart.clear()

    # Call the cart page
    response = client.get("/cart")
    html = response.data.decode()

    # Validate empty cart message
    assert "Your cart is empty" in html

    # Ensure no book titles or totals are displayed
    assert "Total Items" not in html
    assert "Total Price" not in html
