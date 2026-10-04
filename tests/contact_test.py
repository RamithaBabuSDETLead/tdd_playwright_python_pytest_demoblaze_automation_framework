from utils import urls
from test_data import user_data as data
from pages import contact_page

def test_contact_form(launch_website):
    page=launch_website
    info = data.get_contact_message()
    contact_page.open_contact(page)
    contact_page.fill_contact_form(page, info["email"], info["name"], info["message"])
    contact_page.send_message(page)
