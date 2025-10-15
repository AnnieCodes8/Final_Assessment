# TC-FR002-UT005: Verify system prevents updates with non-existent book titles

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_prevent_update_with_nonexistent_book_title(client):
    """
    Test Case: TC-FR002-UT005
    Requirement: FR-002
    Title: Verify system prevents updates with non-existent book titles
    Preconditions: Cart contains **_1984_** (Quantity: 2)
    Steps:
      - Add **_1984_** (q = 2) to cart
      - Attempt to update "Nonexistent Book" to q = 10
      - Call update_cart() function
    Expected Result:
      - System displays error message (e.g. "Book not found" or "Invalid title")
      - **_1984_** remains in cart with Quantity = 2
    """

    # Reset cart before test
    cart.clear()

    # Add **_1984_** with quantity = 2
    client.post("/add-to-cart", data={"title": "1984", "quantity": 2}, follow_redirects=True)

    # Attempt to update a non-existent book
    response = client.post("/update-cart", data={"title": "Nonexistent Book", "quantity": 10}, follow_redirects=True)
    html = response.data.decode()

    # Validate error message (depending on template wording)
    assert "Book not found" in html or "Invalid title" in html

    # Ensure **_1984_** is still in the cart with quantity = 2
    cart_response = client.get("/cart")
    cart_html = cart_response.data.decode()
    assert "1984" in cart_html
    assert "Quantity: 2" in cart_html or ">2<" in cart_html
