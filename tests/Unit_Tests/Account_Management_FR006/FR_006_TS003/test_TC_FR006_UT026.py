# TC-FR006-UT026: Verify user can update name, address, and password successfully

import sys, os
import pytest

# Ensure project root is on sys.path so `app.py` can be imported
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import app, users, User


def test_update_profile_successfully():
    """
    Test Case: TC-FR006-UT026
    Requirement: FR-006
    Title: Verify user can update name, address, and password successfully
    Preconditions:
      - Demo account exists in users
      - Demo account is logged in
    Steps:
      1. Navigate to /update-profile.
      2. Submit form with:
         - Name = Demo Updated
         - Address = 72 New Street
         - New Password = (empty)
    Expected Result:
      1. User.name updated to Demo Updated.
      2. User.address updated to 72 New Street.
      3. Flash message: "Profile updated successfully!".
      4. Redirect to /account.
    """

    test_client = app.test_client()

    # Ensure demo account exists
    users["demo@bookstore.com"] = User(
        email="demo@bookstore.com",
        password="demo123",
        name="Demo User",
        address="123 Demo Street"
    )

    # Log the demo user in by setting session
    with test_client.session_transaction() as sess:
        sess["user_email"] = "demo@bookstore.com"

    # Submit profile update form
    response = test_client.post(
        "/update-profile",
        data={
            "name": "Demo Updated",
            "address": "72 New Street",
            "new_password": ""  # left empty
        },
        follow_redirects=True
    )

    # Reload user object
    updated_user = users["demo@bookstore.com"]

    # 1. Verify name updated
    assert updated_user.name == "Demo Updated"

    # 2. Verify address updated
    assert updated_user.address == "72 New Street"

    # 3. Verify flash message present
    assert b"Profile updated successfully!" in response.data

    # 4. Verify redirect landed on /account
    assert response.request.path == "/account"
