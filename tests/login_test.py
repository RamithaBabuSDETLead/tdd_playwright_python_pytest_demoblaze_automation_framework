from playwright.sync_api import expect
from utils import urls,helpers
from test_data import user_data as data
from pages import login_page
from locators import login_locators as loc

def test_login_valid_user(page):
    creds = data.get_valid_user()
    page.goto(urls.demoblaze_url)
    login_page.perform_login(page, creds["username"], creds["password"])
    expect(page.locator(loc.welcome_user)).to_be_visible()
    expect(page.locator(loc.welcome_user)).to_contain_text(creds["username"])

def test_login_invalid_user(page):
    creds = data.get_invalid_user()
    page.goto(urls.demoblaze_url)
    login_page.perform_login(page, creds["username"], creds["password"])
    alert_text = helpers.get_alert_text(page)
    assert "User does not exist" in alert_text

def test_login_wrong_password(page):
    creds = data.get_wrong_password_user()
    page.goto(urls.demoblaze_url)
    login_page.perform_login(page, creds["username"], creds["password"])
    alert_text = helpers.get_alert_text(page)
    assert "Wrong password" in alert_text
