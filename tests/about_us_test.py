from playwright.sync_api import expect
from pages import about_us_page
import locators.about_us_locators as loc

def test_about_us_modal_opens(launch_website):
    page = launch_website
    about_us_page.open_about_us(page)
    expect(page.locator(loc.about_us_modal_label)).to_be_visible()

def test_about_us_video_visible(launch_website):
    page = launch_website
    about_us_page.open_about_us(page)
    expect(page.locator(loc.about_us_video)).to_be_visible()

def test_about_us_modal_closes(launch_website):
    page = launch_website
    about_us_page.open_about_us(page)
    about_us_page.close_about_us(page)
    expect(page.locator(loc.about_us_modal_label)).not_to_be_visible()
