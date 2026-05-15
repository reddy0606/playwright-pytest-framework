from pages.login_page import LoginPage
from utils.data_reader import load_test_data


def test_valid_login(page):

    data = load_test_data()

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    assert "inventory" in page.url


def test_invalid_login(page):

    data = load_test_data()

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        data["invalid_user"]["username"],
        data["invalid_user"]["password"]
    )

    assert "Epic sadface" in login_page.get_error_message()