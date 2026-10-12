import pytest
from playwright.sync_api import Playwright
from setup.browser_setup import get_web_app
from utils import data_handle

@pytest.fixture
def launch_website(playwright:Playwright):
    dev_path="config.dev.json"
    dev_url = data_handle.get_data_from_json("dev_url",dev_path)
    browser = data_handle.get_data_from_json("browser", dev_path)
    page = get_web_app(browser,dev_url,playwright)
    yield page
    page.context.close()