# TC-FR003-UT016: Verify discount code SAVE10 is applied successfully even with case errors

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize("code_variant", ["save10", "sAve10"])
def test_apply_discount_save10_case_insensitive(client, code_variant):
    """
    Test Case: TC-FR003-UT016
    Requirement: FR-003
    Scenario: FR-003-TS003 (User applies discount code)
    Title: Verify discount code SAVE10 is applied successfully even with case errors
    Preconditions:
      - Cart contains "The Great Gatsby" (£10.99, Quantity: 1)
    Steps:
      - Add "The Great Gatsby" (q = 1) to cart
      - Enter discount code with case variation (e.g., "save10", "sAve10")
      - Submit checkout form with valid shipping and payment info
    Expected Result:
      - Cart/order total is reduced from £10.99 to £9.89
      - Discounted total is displayed on the confirmation page
    """

    # Reset cart and add item
    cart.clear()
    client.post("/add-to-cart", data={"title": "The Great Gatsby", "quantity": 1}, follow_redirects=True)

    # Submit checkout form with discount code variant
    response = client.post(
        "/process-checkout",
        data={
            # Shipping info
            "name": "Oli Smith",
            "address": "10 High Street",
            "city": "London",
            "zip_code": "SW1A 1AA",
            "email": "ol8@example.com",
            # Payment info
            "payment_method": "credit_card",
            "card_number": "4111111111111234",
            "expiry_date": "12/30",
            "cvv": "123",
            # Discount code variant
            "discount_code": code_variant
        },
        follow_redirects=True
    )
    html = response.data.decode()

    # Verify response is OK
    assert response.status_code == 200
    # Verify discounted total is presented to the user
    assert "9.89" in html or "£9.89" in html
