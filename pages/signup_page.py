from utils import helpers
import locators.signup_locators as loc

def signup(page, username, password):
    helpers.click(page, loc.signup_link)
    helpers.expect_visible(page, loc.signup_modal)

    helpers.fill(page, loc.signup_username, username)
    helpers.fill(page, loc.signup_password, password)
    helpers.click(page, loc.signup_button)
    try:
        dialog = page.wait_for_event("dialog", timeout=5000)
        assert "Sign up successful" in dialog.message or "This user already exist" in dialog.message
        dialog.accept()
    except Exception:
        helpers.expect_not_visible(page, loc.signup_modal)
