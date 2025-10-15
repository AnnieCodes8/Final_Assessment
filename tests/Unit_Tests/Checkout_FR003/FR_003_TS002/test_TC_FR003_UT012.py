# TC-FR003-UT012: Verify user can enter all required shipping fields in an acceptable format successfully

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_valid_shipping_information_submission(client):
    """
    Test Case: TC-FR003-UT012
    Requirement: FR-003
    Scenario: FR-003-TS002 (User enters valid shipping information)
    Title: Verify user can enter all required shipping fields in an acceptable format successfully
    Preconditions:
      - Checkout page is loaded with items in cart
    Steps:
      - Navigate to checkout form
      - Enter Name = "Oli Smith"
      - Enter Address = "10 High Street, London"
      - Enter City = "London"
      - Enter Zip Code = "SW1A 1AA"
      - Enter Email = "ol8@example.com"
      - Submit form
    Expected Result:
      - Form submission succeeds
      - Data stored in session
      - User proceeds to payment step
    """

    # Reset cart and add an item so checkout is available
    cart.clear()
    client.post("/add-to-cart", data={"title": "The Great Gatsby", "quantity": 1}, follow_redirects=True)

    # Submit valid shipping information to /process-checkout
    response = client.post(
        "/process-checkout",
        data={
            "name": "Oli Smith",
            "address": "10 High Street, London",
            "city": "London",
            "zip_code": "SW1A 1AA",
            "email": "ol8@example.com"
        },
        follow_redirects=True
    )
    html = response.data.decode()

    # Verify form submission succeeded and user is on payment step
    assert response.status_code == 200
    assert "Payment" in html or "Enter Payment Details" in html
    # Optional: check that shipping info is echoed back or stored
    assert "Oli Smith" in html or "Shipping Information" in html
