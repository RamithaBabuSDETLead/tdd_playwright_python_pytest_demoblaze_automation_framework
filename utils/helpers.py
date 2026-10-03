from playwright.sync_api import expect

def handle_alert(page):
    dialog = page.wait_for_event("dialog")
    dialog.accept()

def get_alert_text(page):
    dialog = page.wait_for_event("dialog")
    message = dialog.message
    dialog.accept()
    return message

def goto(page, url):
    page.goto(url)

def click(page, locator):
    page.locator(locator).click()

def fill(page, locator, value):
    page.locator(locator).fill(value)

def expect_text(page, locator, text, timeout=5000):
    expect(page.locator(locator)).to_have_text(text, timeout=timeout)

def expect_visible(page, locator, timeout=5000):
    expect(page.locator(locator)).to_be_visible(timeout=timeout)

def expect_first_visible(page, locator, timeout=5000):
    expect(page.locator(locator).first).to_be_visible(timeout=timeout)

def expect_contains_text(page, locator, text, timeout=5000):
    expect(page.locator(locator)).to_contain_text(text, timeout=timeout)

def expect_not_visible(page, locator, timeout=5000):
    expect(page.locator(locator)).not_to_be_visible(timeout=timeout)

def expect_error_message(page, locator, expected_text, timeout=5000):
    expect(page.locator(locator)).to_contain_text(expected_text, timeout=timeout)