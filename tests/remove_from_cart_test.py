from utils import urls
from pages import remove_cart_page as remove_cart
from locators import remove_cart_locator as loc
from playwright.sync_api import expect

def test_remove_from_cart(launch_website):
    page=launch_website
    remove_cart.add_samsung_phone(page)
    remove_cart.add_sony_laptop(page)
    remove_cart.open_cart(page)
    remove_cart.remove_product_from_cart(page, "Samsung galaxy s6")
    expect(page.locator(loc.cart_sony)).to_be_visible()
