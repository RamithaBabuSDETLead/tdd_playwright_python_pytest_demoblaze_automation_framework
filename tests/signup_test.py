from utils import urls
from test_data import user_data
from pages import signup_page

def test_signup(page):
    creds = user_data.get_signup_user()
    page.goto(urls.demoblaze_url)
    signup_page.signup(page, creds["username"], creds["password"])
