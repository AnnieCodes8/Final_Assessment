# TC-FR003-UT017: Verify user can apply the discount code WELCOME20 successfully

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_apply_discount_welcome20(client):
    """
    Test Case: TC-FR003-UT017
    Requirement: FR-003
    Scenario: FR-003-TS003 (User applies discount code)
    Title: Verify user can apply the discount code WELCOME20 successfully
    Preconditions:
      - Cart contains "1984" (£8.99, Quantity: 1)
    Steps:
      - Add "1984" (q = 1) to cart
      - Enter discount code "WELCOME20"
      - Submit checkout form with valid shipping and payment info
    Expected Result:
      - Cart/order total is reduced from £8.99 to £7.19 (20% off)
      - Discounted total is displayed on the confirmation page
    """

    # Reset cart and add item
    cart.clear()
    client.post("/add-to-cart", data={"title": "1984", "quantity": 1}, follow_redirects=True)

    # Submit checkout form with discount code WELCOME20
    response = client.post(
        "/process-checkout",
        data={
            # Shipping info
            "name": "Alice Doe",
            "address": "22 Baker Street",
            "city": "London",
            "zip_code": "NW1 6XE",
            "email": "alice@example.com",
            # Payment info
            "payment_method": "credit_card",
            "card_number": "4111111111111234",
            "expiry_date": "12/30",
            "cvv": "123",
            # Discount code
            "discount_code": "WELCOME20"
        },
        follow_redirects=True
    )
    html = response.data.decode()

    # Verify response is OK
    assert response.status_code == 200
    # Verify discounted total is presented to the user
    assert "7.19" in html or "£7.19" in html
