from utils import urls
from test_data import user_data
from pages import order_page

def test_order_product(page):
    creds = user_data.get_order_details()
    page.goto(urls.demoblaze_url)
    order_page.add_product_to_cart(page)
    order_page.open_cart(page)
    order_page.place_order(
        page,
        creds["name"],
        creds["country"],
        creds["city"],
        creds["card"],
        creds["month"],
        creds["year"]
    )
