import pytest

from test_data import user_data
from pages import order_page

@pytest.mark.cart
def test_order_product(launch_website):
    page=launch_website
    creds = user_data.get_order_details()
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
