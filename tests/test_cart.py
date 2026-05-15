from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_reader import load_test_data


def test_add_item_to_cart(page):

    data = load_test_data()

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open_login_page()

    login_page.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    inventory_page.add_item_to_cart()

    assert inventory_page.get_cart_count() == "1"


def test_remove_item_from_cart(page):

    data = load_test_data()

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open_login_page()

    login_page.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    inventory_page.add_item_to_cart()

    inventory_page.remove_item_from_cart()

    assert page.locator(".shopping_cart_badge").count() == 0