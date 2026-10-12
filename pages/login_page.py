# pages/login_page.py
import locators.login_locators as loc
from utils import helpers

def open_login_modal(page):
    page.wait_for_load_state("networkidle")
    login_btn = page.locator(loc.login_button)
    login_btn.wait_for(state="visible", timeout=5000)
    login_btn.scroll_into_view_if_needed()
    login_btn.click()
    page.wait_for_selector(loc.login_modal, state="visible", timeout=5000)
    page.wait_for_timeout(500)  # allow animation

def fill_login_form(page, username, password):
    helpers.fill(page, loc.login_username, username)
    helpers.fill(page, loc.login_password, password)

def submit_login(page):
    submit_btn = page.locator(loc.login_submit)
    submit_btn.wait_for(state="visible", timeout=5000)
    submit_btn.scroll_into_view_if_needed()
    submit_btn.click()

def perform_login(page, username, password):
    open_login_modal(page)
    fill_login_form(page, username, password)
    submit_login(page)

    alert_text = {"msg": None}
    def handle_dialog(dialog):
        alert_text["msg"] = dialog.message
        dialog.accept()
    page.on("dialog", handle_dialog)

    try:
        page.wait_for_selector(loc.login_modal, state="hidden", timeout=5000)
        page.wait_for_selector(loc.welcome_user, timeout=5000)
        return "success"
    except:
        return alert_text["msg"] or "Login failed"

def perform_logout(page):
    helpers.click(page, loc.logout_button)
    helpers.expect_not_visible(page, loc.welcome_user)
    return "success"
