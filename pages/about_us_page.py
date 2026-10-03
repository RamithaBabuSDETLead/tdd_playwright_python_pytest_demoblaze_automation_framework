import actions.action_module as act
import locators.about_us_locators as loc

def open_about_us(page):
    act.click_element(page, loc.about_us_link)

def play_video(page):
    return page.locator(loc.about_us_video)

def close_about_us(page):
    act.click_element(page, loc.about_us_close)
