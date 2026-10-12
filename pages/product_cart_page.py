import conftest
from pages import remove_cart_page as cart
from locators import remove_cart_locator as loc
from playwright.sync_api import expect

def test_product_cart(page):
    cart.add_samsung_phone(page)
    page.wait_for_load_state("networkidle")
    cart.add_sony_laptop(page)
    page.wait_for_load_state("networkidle")
    cart.open_cart(page)
    expect(page.locator(loc.product_cell_template.format("Samsung galaxy s6"))).to_be_visible()
    expect(page.locator(loc.product_cell_template.format("Sony vaio i5"))).to_be_visible()
    expect(page.locator(loc.total)).to_be_visible()
