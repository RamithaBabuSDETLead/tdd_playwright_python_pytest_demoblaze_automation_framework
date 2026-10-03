from utils import urls, helpers
from locators import home_locators as home

def test_home_page_loads(page):
    page.goto(urls.demoblaze_url)
    helpers.expect_first_visible(page, home.products)

def test_navigate_categories(page):
    page.goto(urls.demoblaze_url)
    helpers.click(page, home.category_laptops)
    helpers.expect_first_visible(page, home.products)

def test_next_page_navigation(page):
    page.goto(urls.demoblaze_url)
    helpers.click(page, home.next_button)
    helpers.expect_first_visible(page, home.products)

def test_previous_page_navigation(page):
    page.goto(urls.demoblaze_url)
    helpers.click(page, home.previous_button)
    helpers.expect_first_visible(page, home.products)

def test_homepage_carousel(page):
    page.goto(urls.demoblaze_url)
    helpers.expect_first_visible(page, home.carousel)

def test_homepage_title(page):
    page.goto(urls.demoblaze_url)
    assert page.title() == "STORE"

def test_homepage_navigation_links(page):
    page.goto(urls.demoblaze_url)
    helpers.expect_first_visible(page, home.nav_home)
    helpers.expect_first_visible(page, home.nav_contact)
    helpers.expect_first_visible(page, home.nav_about)
    helpers.expect_first_visible(page, home.nav_cart)
    helpers.expect_first_visible(page, home.nav_login)
    helpers.expect_first_visible(page, home.nav_signup)
