def get_chrome_browser(playwright):
    browser=playwright.chromium.launch (headless=False)
    browser_context=browser.new_context()
    return browser_context
def get_firefox_browser(playwright):
    browser = playwright.firefox.launch (headless=False)
    browser_context = browser.new_context()
    return browser_context
def get_safari_browser(playwright):
    browser = playwright.webkit.launch (headless=False)
    browser_context = browser.new_context()
    return browser_context

def get_web_app(browser,url,playwright):
    browser_context=browser_factory(browser,playwright)
    page=browser_context.new_page()
    page.goto(url)
    return page

def browser_factory(browser,playwright):
    match browser:
        case "chrome":
            return get_chrome_browser(playwright)
        case "firefox":
            return get_firefox_browser(playwright)
        case "safari":
            return get_safari_browser(playwright)
    return get_chrome_browser(playwright)
