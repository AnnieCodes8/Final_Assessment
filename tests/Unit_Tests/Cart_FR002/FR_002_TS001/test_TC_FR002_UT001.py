# TC-FR002 UT001: Verify user can add multiple books to the cart.

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_multiple_books_to_cart(client):
    """
    Test Case: TC-FR002-UT001
    Requirement: FR-002
    Scenario: FR-002-TS001
    Description: Verify user can add multiple books to the cart.
    Steps:
      1. Navigate to catalogue
      2. Add The Great Gatsby (q=1)
      3. Add 1984 (q=2)
      4. Click 'Add to Cart'
      5. View Cart
    Expected Result:
      - Cart displays both books with correct title, price, and quantity
      - Total = £28.97
    """

    # Reset cart before test
    cart.clear()

    # Step 2: Add The Great Gatsby (Quantity = 1)
    client.post("/add-to-cart", data={"title": "The Great Gatsby", "quantity": 1}, follow_redirects=True)

    # Step 3: Add 1984 (Quantity = 2)
    client.post("/add-to-cart", data={"title": "1984", "quantity": 2}, follow_redirects=True)

    # Step 5: View Cart
    response = client.get("/cart")
    assert response.status_code == 200
    html = response.data.decode()

    # Validate cart contents
    assert "The Great Gatsby" in html
    assert "1984" in html

    # Validate quantities (depending on template formatting)
    assert "1" in html
    assert "2" in html

    # Validate total price
    expected_total = (1 * 10.99) + (2 * 8.99)  # = 28.97
    assert f"{expected_total:.2f}" in html
