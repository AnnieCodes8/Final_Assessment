# TC-FR002-UT009: Verify clearing an already empty cart does not cause errors

import pytest
from app import app, cart

@pytest.fixture
def client():
    """Flask test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_clear_already_empty_cart(client):
    """
    Test Case: TC-FR002-UT009
    Requirement: FR-002
    Title: Verify clearing an already empty cart does not cause errors
    Preconditions: Cart is empty
    Steps:
      - Call clear_cart() function
    Expected Result:
      - System handles gracefully
      - Cart remains empty
      - No errors are thrown
    """

    # Ensure cart is empty before test
    cart.clear()

    # Attempt to clear the already empty cart
    response = client.post("/clear-cart", follow_redirects=True)
    html = response.data.decode()

    # Verify no errors occurred and cart is still empty
    assert response.status_code == 200
    assert "Your cart is empty" in html or "0 items" in html
    assert "Traceback" not in html  # sanity check: no crash output
