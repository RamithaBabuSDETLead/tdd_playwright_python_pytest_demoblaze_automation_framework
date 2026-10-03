from utils import helpers
import locators.login_locators as loc

def open_login_modal(page):
    helpers.click(page, loc.login_button)
    helpers.expect_visible(page, loc.login_modal)

def fill_login_form(page, username, password):
    helpers.fill(page, loc.login_username, username)
    helpers.fill(page, loc.login_password, password)

def submit_login(page):
    helpers.click(page, loc.login_submit)

def perform_login(page, username, password):
    open_login_modal(page)
    fill_login_form(page, username, password)
    submit_login(page)
