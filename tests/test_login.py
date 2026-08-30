from playwright.sync_api import Page

from pages.login_page import LoginPage


def test_login_valid_user(page: Page):
    login_page = LoginPage(page)

    login_page.login("standard_user", "secret_sauce")

    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_login_invalid_username(page: Page):
    login_page = LoginPage(page)

    login_page.login("user", "secret_sauce")

    assert login_page.get_error_message() == (
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_login_invalid_password(page: Page):
    login_page = LoginPage(page)

    login_page.login("standard_user", "password")

    assert login_page.get_error_message() == (
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_login_locked_out_user(page: Page):
    login_page = LoginPage(page)

    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.get_error_message() == (
        "Epic sadface: Sorry, this user has been locked out."
    )


def test_login_empty_username(page: Page):
    login_page = LoginPage(page)

    login_page.login("", "secret_sauce")

    assert login_page.get_error_message() == (
        "Epic sadface: Username is required"
    )


def test_login_empty_password(page: Page):
    login_page = LoginPage(page)

    login_page.login("standard_user", "")

    assert login_page.get_error_message() == (
        "Epic sadface: Password is required"
    )


def test_login_empty_username_and_password(page: Page):
    login_page = LoginPage(page)

    login_page.login("", "")

    assert login_page.get_error_message() == (
        "Epic sadface: Username is required"
    )
