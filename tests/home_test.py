import pytest

from utils import  helpers
from locators import home_locators as home

@pytest.mark.dashboard
def test_home_page_loads(launch_website):
    page = launch_website
    page.wait_for_load_state("networkidle")
    helpers.expect_first_visible(page, home.products)

@pytest.mark.dashboard
def test_navigate_categories(launch_website):
    page = launch_website
    helpers.click(page, home.category_laptops)
    page.wait_for_load_state("networkidle")
    helpers.expect_first_visible(page, home.products)

@pytest.mark.dashboard
def test_next_page_navigation(launch_website):
    page = launch_website
    helpers.click(page, home.next_button)
    page.wait_for_load_state("networkidle")
    helpers.expect_first_visible(page, home.products)

@pytest.mark.dashboard
def test_previous_page_navigation(launch_website):
    page = launch_website
    # Only click if enabled (DemoBlaze disables Previous until Next is clicked)
    if page.is_enabled(home.previous_button):
        helpers.click(page, home.previous_button)
        page.wait_for_load_state("networkidle")
        helpers.expect_first_visible(page, home.products)

@pytest.mark.dashboard
def test_homepage_carousel(launch_website):
    page = launch_website
    helpers.expect_first_visible(page, home.carousel)

@pytest.mark.dashboard
def test_homepage_title(launch_website):
    page = launch_website
    assert page.title() == "STORE"

@pytest.mark.dashboard
def test_homepage_navigation_links(launch_website):
    page = launch_website
    page.wait_for_load_state("networkidle")
    assert page.get_by_role("link", name="Home").is_visible()
    assert page.get_by_role("link", name="Contact").is_visible()
    assert page.get_by_role("link", name="About us").is_visible()
    assert page.get_by_role("link", name="Cart").is_visible()
    assert page.get_by_role("link", name="Log in").is_visible()
    assert page.get_by_role("link", name="Sign up").is_visible()

