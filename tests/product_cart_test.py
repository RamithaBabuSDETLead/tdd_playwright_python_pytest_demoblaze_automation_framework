import pytest

from pages import remove_cart_page as cart
from locators import remove_cart_locator as loc
from playwright.sync_api import expect

@pytest.mark.product
def test_product_cart(launch_website):
    page=launch_website
    cart.add_samsung_phone(page)
    cart.add_sony_laptop(page)
    cart.open_cart(page)
    expect(page.locator(loc.product_cell_template.format("Samsung galaxy s6"))).to_be_visible()
    expect(page.locator(loc.product_cell_template.format("Sony vaio i5"))).to_be_visible()
    expect(page.locator(loc.total_heading)).to_be_visible()
    expect(page.locator(loc.total_amount)).to_be_visible()
