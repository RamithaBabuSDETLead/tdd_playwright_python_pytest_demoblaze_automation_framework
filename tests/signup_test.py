from utils import urls
from test_data import user_data
from pages import signup_page

def test_signup(launch_website):
    page=launch_website
    creds = user_data.get_signup_user()
    signup_page.signup(page, creds["username"], creds["password"])
