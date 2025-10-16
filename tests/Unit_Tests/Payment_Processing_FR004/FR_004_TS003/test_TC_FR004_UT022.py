# TC-FR004-UT022: Verify transaction ID is generated and correctly formatted for successful payment

import re
import pytest
from models import PaymentGateway   # adjust if your module path differs

def test_process_payment_generates_transaction_id():
    """
    Test Case: TC-FR004-UT022
    Requirement: FR-004
    Title: Verify transaction ID is generated and correctly formatted for successful payment
    Preconditions:
      - Cart contains "1984" (£8.99, Quantity: 1)
      - Shipping details completed
    Steps:
      1. Prepare payment_info with:
         - Card Number = 5555444433332222 (valid, not ending in 1111)
         - Payment Method = paypal
         - Amount = £8.99
      2. Call PaymentGateway.process_payment(payment_info)
    Expected Result:
      - Response returns success=True
      - Message = "Payment processed successfully"
      - transaction_id is non-null, starts with "TXN", and is followed by 6 digits
    """

    payment_info = {
        "card_number": "5555444433332222",
        "payment_method": "paypal",
        "amount": 8.99
    }

    result = PaymentGateway.process_payment(payment_info)

    # Verify success and message
    assert result["success"] is True
    assert result["message"] == "Payment processed successfully"

    # Verify transaction_id format
    transaction_id = result.get("transaction_id")
    assert transaction_id is not None
    assert isinstance(transaction_id, str)
    assert re.fullmatch(r"TXN\d{6}", transaction_id), (
        f"Transaction ID '{transaction_id}' does not match expected format TXN######"
    )
