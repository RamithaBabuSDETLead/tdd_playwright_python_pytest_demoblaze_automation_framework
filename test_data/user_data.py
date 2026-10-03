import time

def get_valid_user():
    return {"username": "ramitha", "password": "user@1234"}

def get_invalid_user():
    return {"username": "fakeuser123", "password": "user@1234"}

def get_wrong_password_user():
    return {"username": "ramitha", "password": "wrongpass"}

def get_logout_user():
    return {"username": "newuser_demo1", "password": "user@1234"}

def get_order_details():
    return {
        "name": "Ramitha",
        "country": "India",
        "city": "Bengaluru",
        "card": "4111111111111111",
        "month": "10",
        "year": "2026"
    }

def generate_signup_credentials():
    return {
        "username": f"user_{int(time.time())}",
        "password": "pass@123"
    }

def get_signup_user():
    return generate_signup_credentials()

def get_contact_message():
    return {
        "email": "ramitha@example.com",
        "name": "Ramitha",
        "message": "Hello, this is a test message!"
    }
