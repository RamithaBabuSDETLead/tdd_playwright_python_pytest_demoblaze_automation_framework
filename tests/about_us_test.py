from utils import urls, helpers
from pages import about_us_page
from locators import about_us_locators as about

def test_about_us_modal_opens(page):
    page.goto(urls.demoblaze_url)
    about_us_page.open_about_us(page)
    helpers.expect_visible(page, about.about_us_modal_label)

def test_about_us_video_visible(page):
    page.goto(urls.demoblaze_url)
    about_us_page.open_about_us(page)
    helpers.expect_visible(page, about.about_us_video)

def test_about_us_modal_closes(page):
    page.goto(urls.demoblaze_url)
    about_us_page.open_about_us(page)
    about_us_page.close_about_us(page)
    helpers.expect_not_visible(page, about.about_us_modal_label)
