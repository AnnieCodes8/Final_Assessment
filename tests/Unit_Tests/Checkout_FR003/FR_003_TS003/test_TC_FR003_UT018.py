# TC-FR003-UT018: Verify system rejects an invalid discount code

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_reject_invalid_discount_code(client):
    """
    Test Case: TC-FR003-UT018
    Requirement: FR-003
    Scenario: FR-003-TS003 (User applies discount code)
    Title: Verify system rejects an invalid discount code
    Preconditions:
      - Cart contains "I Ching" (£18.99, Quantity: 1)
    Steps:
      - Add "I Ching" (q = 1) to cart
      - Enter discount code "INVALIDCODE"
      - Submit checkout form with valid shipping and payment info
    Expected Result:
      - System displays "Invalid code"
      - Cart/order total remains £18.99
    """

    # Reset cart and add item
    cart.clear()
    client.post("/add-to-cart", data={"title": "I Ching", "quantity": 1}, follow_redirects=True)

    # Submit checkout form with invalid discount code
    response = client.post(
        "/process-checkout",
        data={
            # Shipping info
            "name": "John Doe",
            "address": "50 Oxford Street",
            "city": "London",
            "zip_code": "W1D 1BS",
            "email": "john@example.com",
            # Payment info
            "payment_method": "credit_card",
            "card_number": "4111111111111234",
            "expiry_date": "12/30",
            "cvv": "123",
            # Invalid discount code
            "discount_code": "INVALIDCODE"
        },
        follow_redirects=True
    )
    html = response.data.decode()

    # Verify response is OK
    assert response.status_code == 200
    # Verify invalid code message is shown
    assert "Invalid" in html or "invalid" in html
    # Verify total remains unchanged (£18.99)
    assert "18.99" in html or "£18.99" in html
