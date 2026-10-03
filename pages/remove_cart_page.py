from playwright.sync_api import expect
from locators import remove_cart_locator as loc

def add_samsung_phone(page):
    page.locator(loc.phones_category).click()
    page.locator(loc.samsung_phone).first.click()
    page.locator(loc.add_to_cart_button).click()
    page.wait_for_event("dialog").accept()
    page.locator(loc.home_link).click()

def add_sony_laptop(page):
    page.locator(loc.laptops_category).click()
    page.locator(loc.sony_laptop).first.click()
    page.locator(loc.add_to_cart_button).click()
    page.wait_for_event("dialog").accept()

def open_cart(page):
    page.locator(loc.cart_link).click()
    expect(page.locator(loc.cart_samsung)).to_be_visible()
    expect(page.locator(loc.cart_sony)).to_be_visible()

def remove_product_from_cart(page, product_name):
    product_cell = loc.product_cell_template.format(product_name)
    remove_button = loc.remove_button_template.format(product_name)
    page.locator(remove_button).click()
    expect(page.locator(product_cell)).not_to_be_visible()
