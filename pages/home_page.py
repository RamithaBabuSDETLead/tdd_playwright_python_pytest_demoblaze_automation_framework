from playwright.sync_api import expect
from  locators import home_locators as home

def load(page):
    page.goto("https://www.demoblaze.com")

def verify_products_visible(page):
    expect(page.locator(home.products).first).to_be_visible()

def navigate_to_laptops(page):
    page.click(home.category_laptops)

def next_page(page):
    page.click(home.next_button)

def previous_page(page):
    page.click(home.previous_button)

def verify_carousel(page):
    expect(page.locator(home.carousel)).to_be_visible()

def verify_title(page):
    assert page.title() == "STORE"

def verify_navigation_links(page):
    expect(page.locator(home.nav_home)).to_be_visible()
    expect(page.locator(home.nav_contact)).to_be_visible()
    expect(page.locator(home.nav_about)).to_be_visible()
    expect(page.locator(home.nav_cart)).to_be_visible()
    expect(page.locator(home.nav_login)).to_be_visible()
    expect(page.locator(home.nav_signup)).to_be_visible()
