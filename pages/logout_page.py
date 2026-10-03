from utils import helpers
import locators.login_locators as loc

def login(page, username, password):
    helpers.click(page, loc.login_button)
    helpers.fill(page, loc.login_username, username)
    helpers.fill(page, loc.login_password, password)
    helpers.click(page, loc.login_submit)

def logout(page):
    helpers.click(page, loc.logout_button)
    helpers.expect_not_visible(page, loc.nameofuser)
