from utils import helpers
import locators.contact_locators as loc

def open_contact(page):
    helpers.click(page, loc.contact_link)
    helpers.expect_text(page, loc.contact_modal_label, "New message")

def fill_contact_form(page, email, name, message):
    helpers.fill(page, loc.contact_email, email)
    helpers.fill(page, loc.contact_name, name)
    helpers.fill(page, loc.contact_message, message)

def send_message(page):
    helpers.click(page, loc.contact_send)
    try:
        # Try to capture alert dialog
        dialog = page.wait_for_event("dialog", timeout=5000)
        assert "Thanks for the message" in dialog.message
        dialog.accept()
    except Exception:
        # Fallback: just check modal closed
        helpers.expect_not_visible(page, loc.contact_modal)

def close_modal(page):
    helpers.click(page, loc.contact_close)
    helpers.expect_not_visible(page, loc.contact_modal)
