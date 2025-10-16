# TC-FR004-IT020: Verify system rejects invalid card number at checkout

import pytest
from app import app

def test_checkout_invalid_card_number(client=None):
    """
    Test Case: TC-FR004-IT020
    Requirement: FR-004
    Title: Verify system rejects invalid card number
    Preconditions:
      - Cart contains "1984" (£8.99, Quantity: 1)
      - Checkout form completed with valid shipping info
    Steps:
      1. Navigate to payment form.
      2. Enter Card Number = "1234567890123456" (invalid).
      3. Enter Expiry = "11/27".
      4. Enter CVV = "456".
      5. Submit form.
    Expected Result:
      - System displays "Invalid card number".
      - Payment is not processed.
    """

    # Use Flask test client
    test_client = client or app.test_client()

    # Simulate posting checkout form with invalid card number
    response = test_client.post(
        "/checkout",
        data={
            "name": "Test User",
            "email": "test@example.com",
            "address": "123 Test Street",
            "city": "London",
            "zip_code": "E1 6AN",
            "payment_method": "credit_card",
            "card_number": "1234567890123456",  # invalid
            "expiry_date": "11/27",
            "cvv": "456"
        },
        follow_redirects=True
    )

    # Verify the response contains the error message
    assert response.status_code == 200
    assert b"Invalid card number" in response.data
