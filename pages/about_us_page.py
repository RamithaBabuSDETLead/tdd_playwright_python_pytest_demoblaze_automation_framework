import actions.action_module as act
import locators.about_us_locators as loc

def open_about_us(page):
    # Click the About Us link and wait for modal
    act.click_element(page, loc.about_us_link)
    page.wait_for_selector(loc.about_us_modal_label, state="visible", timeout=5000)

def play_video(page):
    # Return the video element
    return page.locator(loc.about_us_video)

def click_video_play(page):
    # Click the play button inside the video controls
    page.locator(loc.video_click).click(force=True)

def close_about_us(page):
    # Click the close button and wait for modal to disappear
    act.click_element(page, loc.about_us_close)
    page.wait_for_selector(loc.about_us_modal_label, state="hidden", timeout=5000)
