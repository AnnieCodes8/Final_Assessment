# TC-FR003-UT015: Verify user can apply the discount code SAVE10 successfully

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_apply_discount_save10(client):
    """
    Test Case: TC-FR003-UT015
    Requirement: FR-003
    Scenario: FR-003-TS003 (User applies discount code)
    Title: Verify user can apply the discount code SAVE10 successfully
    Preconditions:
      - Cart contains "The Great Gatsby" (£10.99, Quantity: 1)
    Steps:
      - Add "The Great Gatsby" (q = 1) to cart
      - Enter discount code "SAVE10"
      - Call apply_discount() function
    Expected Result:
      - Cart total updates from £10.99 to £9.89 (10% off)
      - Discount shown in summary
    """

    # Reset cart and add item
    cart.clear()
    client.post("/add-to-cart", data={"title": "The Great Gatsby", "quantity": 1}, follow_redirects=True)

    # Apply discount code SAVE10
    response = client.post(
        "/apply-discount",
        data={"code": "SAVE10"},
        follow_redirects=True
    )
    html = response.data.decode()

    # Verify discount applied
    assert response.status_code == 200
    # Discount summary should be visible
    assert "Discount" in html or "SAVE10" in html
    # Verify updated total (rounded to 2 decimal places)
    assert "£9.89" in html or "9.89" in html
