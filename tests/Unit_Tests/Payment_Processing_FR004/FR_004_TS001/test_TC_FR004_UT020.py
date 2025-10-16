# TC-FR004-UT020: Verify successful PayPal payment with valid card number

import pytest
from models import PaymentGateway

def test_process_payment_success_paypal():
    """
    Test Case: TC-FR004-UT020
    Requirement: FR-004
    Title: Verify successful PayPal payment with valid card number
    Preconditions:
      - Cart contains "I Ching" (£18.99, Quantity: 1)
      - Shipping details completed
    Steps:
      1. Prepare payment_info with:
         - Card Number = 5555444433332222 (valid, not ending in 1111)
         - Payment Method = paypal
         - Amount = £18.99
      2. Call PaymentGateway.process_payment(payment_info)
    Expected Result:
      - Response returns success=True
      - Message = "Payment processed successfully"
      - transaction_id is not None
    """

    payment_info = {
        "card_number": "5555444433332222",
        "payment_method": "paypal",
        "amount": 18.99
    }

    result = PaymentGateway.process_payment(payment_info)

    # Verify response structure and values
    assert result["success"] is True
    assert result["message"] == "Payment processed successfully"
    assert result.get("transaction_id") is not None
    assert isinstance(result["transaction_id"], str)
    assert result["transaction_id"].strip() != ""
