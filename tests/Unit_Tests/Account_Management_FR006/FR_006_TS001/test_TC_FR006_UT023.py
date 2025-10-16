# TC-FR006-UT023: Verify user can register a new account successfully

import pytest
from app import app, users, User

def test_register_new_account_success():
    """
    Test Case: TC-FR006-UT023
    Requirement: FR-006
    Title: Verify user can register a new account successfully
    Preconditions:
      - Email not already in users dictionary
    Steps:
      1. Navigate to /register.
      2. Submit form with:
         - Email = newuser@bookstore.com
         - Password = password123
         - Name = Alice Example
         - Address = 123 High Street
    Expected Result:
      1. New User object created in users.
      2. Session contains user_email = newuser@bookstore.com.
      3. Flash message: "Account created successfully! You are now logged in."
      4. Redirect to /index.
    """

    test_client = app.test_client()

    # Ensure the test email is not already registered
    users.pop("newuser@bookstore.com", None)

    response = test_client.post(
        "/register",
        data={
            "email": "newuser@bookstore.com",
            "password": "password123",
            "name": "Alice Example",
            "address": "123 High Street"
        },
        follow_redirects=True
    )

    # 1. Verify new user is created in users dictionary
    assert "newuser@bookstore.com" in users
    new_user = users["newuser@bookstore.com"]
    assert isinstance(new_user, User)
    assert new_user.password == "password123"
    assert new_user.name == "Alice Example"
    assert new_user.address == "123 High Street"

    # 2. Verify session contains user_email
    with test_client.session_transaction() as sess:
        assert sess.get("user_email") == "newuser@bookstore.com"

    # 3. Verify flash message is present in response
    assert b"Account created successfully! You are now logged in." in response.data

    # 4. Verify redirect landed on index page
    assert response.request.path == "/"

