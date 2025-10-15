# TC-FR003-UT013: Verify user cannot continue checkout after entering an invalid email address

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_invalid_email_blocks_checkout(client):
    """
    Test Case: TC-FR003-UT013
    Requirement: FR-003
    Scenario: FR-003-TS002 (User enters shipping information)
    Title: Verify user cannot continue checkout after entering an invalid email address
    Preconditions:
      - Checkout page is loaded with items in cart
    Steps:
      - Enter valid Name, Address, City, Zip, Phone
      - Enter invalid Email = "alice[at]example"
      - Submit form
    Expected Result:
      - System displays validation error "Invalid email address"
      - Form not submitted
      - User remains on checkout page
    """

    # Reset cart and add an item so checkout is available
    cart.clear()
    client.post("/add-to-cart", data={"title": "The Great Gatsby", "quantity": 1}, follow_redirects=True)

    # Submit checkout form with invalid email
    response = client.post(
        "/process-checkout",
        data={
            "name": "Alice Doe",
            "address": "22 Baker Street",
            "city": "London",
            "zip_code": "NW1 6XE",
            "phone": "07123456789",
            "email": "alice[at]example",  # invalid format
            # Payment fields (still required by process_checkout)
            "card_number": "4111111111111234",
            "cvv": "123",
            "expiry_date": "12/30",
            "payment_method": "credit_card"
        },
        follow_redirects=True
    )
    html = response.data.decode()

    # Verify system blocks checkout
    assert response.status_code == 200
    assert "Invalid email address" in html
    # User should remain on checkout page, not advance to payment/confirmation
    assert "Checkout" in html
    assert "Payment" not in html or "Order Confirmation" not in html
