# TC-FR003-UT015: Verify discount code SAVE10 reduces total by 10%

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_apply_discount_save10_total_only(client):
    """
    Test Case: TC-FR003-UT015
    Requirement: FR-003
    Scenario: FR-003-TS003 (User applies discount code)
    Title: Verify discount code SAVE10 reduces total by 10%
    Preconditions:
      - Cart contains "The Great Gatsby" (£10.99, Quantity: 1)
    Steps:
      - Add "The Great Gatsby" (q = 1) to cart
      - Submit checkout form with discount code "SAVE10"
    Expected Result:
      - Cart/order total is reduced from £10.99 to £9.89
    """

    # Reset cart and add item
    cart.clear()
    client.post("/add-to-cart", data={"title": "The Great Gatsby", "quantity": 1}, follow_redirects=True)

    # Submit checkout form with discount code SAVE10
    client.post(
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
            # Discount code
            "discount_code": "SAVE10"
        },
        follow_redirects=True
    )

    # After checkout, the cart total should reflect the discount
    discounted_total = round(cart.get_total_price(), 2)
    assert discounted_total == 9.89
