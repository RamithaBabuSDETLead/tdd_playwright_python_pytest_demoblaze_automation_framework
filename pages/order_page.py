from utils import helpers
import locators.order_locators as loc

def add_product_to_cart(page):
    helpers.click(page, loc.product_link)
    helpers.click(page, loc.add_to_cart_button)

def open_cart(page):
    helpers.click(page, loc.cart_link)

def place_order(page, name, country, city, card, month, year):
    helpers.click(page, loc.place_order_button)
    helpers.expect_visible(page, loc.order_modal)
    helpers.fill(page, loc.order_name, name)
    helpers.fill(page, loc.order_country, country)
    helpers.fill(page, loc.order_city, city)
    helpers.fill(page, loc.order_credit_card, card)
    helpers.fill(page, loc.order_month, month)
    helpers.fill(page, loc.order_year, year)
    helpers.click(page, loc.purchase_button)
    helpers.expect_visible(page, loc.confirmation_box)
    helpers.click(page, loc.confirmation_ok)
