from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from utils.data_reader import load_test_data


def test_complete_checkout(page):

    data = load_test_data()

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open_login_page()

    login_page.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    inventory_page.add_item_to_cart()

    inventory_page.open_cart()

    checkout_page.start_checkout()

    checkout_page.fill_checkout_information(
        "John",
        "Doe",
        "500001"
    )

    checkout_page.continue_checkout()

    checkout_page.finish_checkout()

    assert "Thank you for your order!" in checkout_page.get_success_message()