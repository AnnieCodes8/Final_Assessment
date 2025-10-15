# TC-FR003-UT014: Verify system prevents submission when a required field is left empty (Email)

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_required_email_field_empty_blocks_checkout(client):
    """
    Test Case: TC-FR003-UT014
    Requirement: FR-003
    Scenario: FR-003-TS002 (User enters shipping information)
    Title: Verify system prevents submission when a required field is left empty
    Preconditions:
      - Checkout page is loaded with items in cart
    Steps:
      - Enter valid Name, Address, City, Zip, Phone
      - Leave Email field empty
      - Submit form
    Expected Result:
      - System displays validation error "Email is required"
      - Form not submitted
      - User remains on checkout page
    """

    # Reset cart and add an item so checkout is available
    cart.clear()
    client.post("/add-to-cart", data={"title": "The Great Gatsby", "quantity": 1}, follow_redirects=True)

    # Submit checkout form with empty email
    response = client.post(
        "/process-checkout",
        data={
            "name": "Alice Doe",
            "address": "22 Baker Street",
            "city": "London",
            "zip_code": "NW1 6XE",
            "phone": "07123456789",
            "email": "",  # required field left empty
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
    assert "Email is required" in html
    # User should remain on checkout page, not advance to confirmation
    assert "Checkout" in html
    assert "Order Confirmed" not in html
