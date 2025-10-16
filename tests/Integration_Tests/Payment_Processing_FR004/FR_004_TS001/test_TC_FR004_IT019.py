# TC-FR004-IT019: Verify successful credit card payment with valid card number

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_process_checkout_valid_payment_success(client):
    """
    Test Case: TC-FR004-IT019
    Requirement: FR-004
    Scenario: FR-004-TS001 (User submits valid payment)
    Title: Verify successful credit card payment with valid card number
    Preconditions:
      - Cart contains "The Great Gatsby" (£10.99, Quantity: 1)
      - Shipping details completed
    Steps:
      1. Add "The Great Gatsby" (q = 1) to cart
      2. Submit checkout form with:
         - Card Number = 4111111111111234 (valid, not ending in 1111)
         - Payment Method = credit_card
         - Amount = £10.99
    Expected Result:
      - Response status = 200
      - Confirmation page rendered
      - Payment processed successfully (transaction_id present in order)
    """

    # Reset cart and add item
    cart.clear()
    client.post(
        "/add-to-cart",
        data={"title": "The Great Gatsby", "quantity": 1},
        follow_redirects=True
    )

    # Submit checkout form with valid payment info
    response = client.post(
        "/process-checkout",
        data={
            # Shipping info
            "name": "Jane Doe",
            "address": "123 Main Street",
            "city": "London",
            "zip_code": "SW1A 1AA",
            "email": "jane@example.com",
            # Payment info
            "payment_method": "credit_card",
            "card_number": "4111111111111234",  # valid test card
            "expiry_date": "12/30",
            "cvv": "123"
        },
        follow_redirects=True
    )
    html = response.data.decode()

    # Verify response is OK
    assert response.status_code == 200
    # Verify confirmation page rendered
    assert "Order Confirmed" in html or "Thank you for your purchase" in html
    # Verify transaction reference is present
    assert "transaction" in html.lower()
