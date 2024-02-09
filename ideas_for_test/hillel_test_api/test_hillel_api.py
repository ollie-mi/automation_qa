from hillel_api import *


def test_auth_signup_positive():
    """Positive test for user sign up"""
    request_body = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 201, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    assert r_json["data"]["userId"] is not None, "userId is empty"
    assert r_json["data"]["distanceUnits"] == 'km', "Key 'distanceUnits' is not 'km'"
    assert r_json["data"]["currency"] == 'usd', "Key 'currency' is not 'usd'"

    # delete user by userId
    users.users(s, r_json["data"]["userId"])


def test_auth_signup_password_mismatch():
    """Negative test for user sign up"""
    request_body = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "123"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not ok"
    assert r_json["message"] == "Passwords do not match", "Wrong error message"


