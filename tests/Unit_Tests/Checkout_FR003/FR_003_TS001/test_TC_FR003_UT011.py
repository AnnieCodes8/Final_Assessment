# TC-FR003-UT011: Verify system prevents proceeding to checkout with empty cart

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_prevent_checkout_with_empty_cart(client):
    """
    Test Case: TC-FR003-UT011
    Requirement: FR-003
    Scenario: FR-003-TS001 (User proceeds to checkout with items in cart)
    Title: Verify system prevents proceeding to checkout with empty cart
    Preconditions: Cart is empty
    Steps:
      - Call proceed_to_checkout() function (navigate to /checkout)
    Expected Result:
      - System displays error message: "Cart is empty"
      - Checkout page is not loaded
      - User remains on cart page or is redirected appropriately
    """

    # Ensure cart is empty before test
    cart.clear()

    # Attempt to proceed to checkout
    response = client.get("/checkout", follow_redirects=True)
    html = response.data.decode()

    # Verify system prevents checkout
    assert response.status_code == 200
    assert "Cart is empty" in html
    assert "Checkout" not in html or "Proceed to Checkout" not in html
