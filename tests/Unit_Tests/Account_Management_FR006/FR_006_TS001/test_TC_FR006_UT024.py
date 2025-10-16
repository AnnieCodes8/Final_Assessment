# TC-FR006-UT024: Verify registration fails when email format is invalid

import pytest
from app import app, users, User

def test_register_invalid_email_format():
    """
    Test Case: TC-FR006-UT024
    Requirement: FR-006
    Title: Verify registration fails when email format is invalid
    Preconditions:
      - No existing account with the test email
      - Application running and /register route accessible
    Steps:
      1. Navigate to /register.
      2. Enter invalid email format (missing '@').
      3. Fill in other required fields (password, name, address).
      4. Submit the form.
    Expected Result:
      - System rejects registration
      - No new user is created
      - Session not updated
      - Error message such as "Invalid email format" displayed
    """

    test_client = app.test_client()

    # Ensure the invalid email is not already in users
    users.pop("invalid email.com", None)

    response = test_client.post(
        "/register",
        data={
            "email": "invalid email.com",  # invalid format
            "password": "password123",
            "name": "Alice Example",
            "address": "123 High Street"
        },
        follow_redirects=True
    )

    # 1. Verify no user was created
    assert "invalid email.com" not in users

    # 2. Verify session does not contain the invalid email
    with test_client.session_transaction() as sess:
        assert sess.get("user_email") is None

    # 3. Verify error message is present in response
    # NOTE: Adjust this string once you implement validation
    assert b"Invalid email format" in response.data

    # 4. Verify still on /register (not redirected to /index)
    assert response.request.path == "/register"
