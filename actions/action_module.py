from playwright.sync_api import expect

def click_element(page, locator, timeout=5000):
    page.locator(locator).click(timeout=timeout)

def fill_field(page, locator, value, timeout=5000):
    page.locator(locator).fill(value, timeout=timeout)

def navigate_to_url(page, url):
    page.goto(url)

def handle_dialog(page, timeout=10000):
    dialog = page.wait_for_event("dialog", timeout=timeout)
    message = dialog.message
    dialog.accept()
    return message

def get_dialog_message(page, timeout=10000):
    dialog = page.wait_for_event("dialog", timeout=timeout)
    return dialog.message

def accept_dialog(page, timeout=10000):
    dialog = page.wait_for_event("dialog", timeout=timeout)
    dialog.accept()
