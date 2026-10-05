import actions.action_module as act
import locators.about_us_locators as loc

def open_about_us(page):
    act.click_element(page, loc.about_us_link)
    page.wait_for_selector(loc.about_us_modal_label, state="visible", timeout=5000)

def play_video(page):
    return page.locator(loc.about_us_video)

def click_video_play(page):
    page.locator(loc.video_click).click(force=True)

def close_about_us(page):
    act.click_element(page, loc.about_us_close)
    page.wait_for_selector(loc.about_us_modal_label, state="hidden", timeout=5000)
