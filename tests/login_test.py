import pytest
from playwright.sync_api import expect
from test_data import user_data as data
from pages import login_page
from locators import login_locators as loc

@pytest.mark.login
def test_login_valid_user(launch_website):
    page = launch_website
    creds = data.get_valid_user()
    result = login_page.perform_login(page, creds["username"], creds["password"])
    assert result == "success"
    expect(page.locator(loc.welcome_user)).to_be_visible()
    expect(page.locator(loc.welcome_user)).to_contain_text(creds["username"])

@pytest.mark.login
def test_login_invalid_user(launch_website):
    page = launch_website
    creds = data.get_invalid_user()
    result = login_page.perform_login(page, creds["username"], creds["password"])
    assert "User does not exist" in result

@pytest.mark.login
def test_login_wrong_password(launch_website):
    page = launch_website
    creds = data.get_wrong_password_user()
    result = login_page.perform_login(page, creds["username"], creds["password"])
    assert "Wrong password." in result
