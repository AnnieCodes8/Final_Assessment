# TC-FR006-UT025: Verify login succeeds with valid demo account credentials

import sys, os
import pytest

# Ensure project root is on sys.path so `app.py` can be imported
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import app, users, User


def test_login_with_valid_demo_account():
    """
    Test Case: TC-FR006-UT025
    Requirement: FR-006
    Title: Verify login succeeds with valid demo account credentials
    Preconditions:
      - Demo account exists in users dictionary
    Steps:
      1. Navigate to /login.
      2. Submit form with:
         - Email = demo@bookstore.com
         - Password = demo123
    Expected Result:
      1. Session contains user_email = demo@bookstore.com.
      2. Flash message: "Logged in successfully!".
      3. Redirect to /index.
    """

    test_client = app.test_client()

    # Ensure demo account exists in users
    users["demo@bookstore.com"] = User(
        email="demo@bookstore.com",
        password="demo123",
        name="Demo User",
        address="123 Demo Street"
    )

    response = test_client.post(
        "/login",
        data={
            "email": "demo@bookstore.com",
            "password": "demo123"
        },
        follow_redirects=True
    )

    # 1. Verify session contains user_email
    with test_client.session_transaction() as sess:
        assert sess.get("user_email") == "demo@bookstore.com"

    # 2. Verify flash message is present in response
    assert b"Logged in successfully!" in response.data

    # 3. Verify redirect landed on index page
    assert response.request.path == "/"
