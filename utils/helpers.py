from playwright.sync_api import expect, TimeoutError

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

def click(page, locator, timeout=5000):
    element = page.locator(locator)
    element.wait_for(state="visible", timeout=timeout)
    element.scroll_into_view_if_needed()
    try:
        element.click(timeout=timeout)
    except TimeoutError:
        # Retry with force if normal click fails
        element.click(force=True, timeout=timeout)
    page.wait_for_timeout(500)

def fill(page, locator, value):
    page.locator(locator).fill(value)

def expect_text(page, locator, text, timeout=5000):
    expect(page.locator(locator)).to_have_text(text, timeout=timeout)

def expect_visible(page, locator, timeout=5000):
    expect(page.locator(locator)).to_be_visible(timeout=timeout)

def expect_first_visible(page, *locators, timeout=10000):
    for locator in locators:
        element = page.locator(locator).first
        element.scroll_into_view_if_needed()
        element.wait_for(state="visible", timeout=timeout)
        assert element.is_visible(), f"Element {locator} not visible"

def expect_contains_text(page, locator, text, timeout=5000):
    expect(page.locator(locator)).to_contain_text(text, timeout=timeout)

def expect_not_visible(page, locator, timeout=5000):
    expect(page.locator(locator)).not_to_be_visible(timeout=timeout)

def expect_error_message(page, locator, expected_text, timeout=5000):
    expect(page.locator(locator)).to_contain_text(expected_text, timeout=timeout)
