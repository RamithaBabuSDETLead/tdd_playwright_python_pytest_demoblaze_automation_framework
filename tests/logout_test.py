from playwright.sync_api import expect
from test_data import user_data as data
from pages import login_page
from locators import login_locators as loc

def test_logout(launch_website):
    page = launch_website
    creds = data.get_valid_user()
    login_page.perform_login(page, creds["username"], creds["password"])
    expect(page.locator(loc.welcome_user)).to_be_visible()
    result = login_page.perform_logout(page)
    assert result == "success"
    expect(page.locator(loc.login_button)).to_be_visible()
