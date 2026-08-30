from playwright.sync_api import Page

from pages.login_page import LoginPage


def test_login_valid_user(page):
    login_page = LoginPage(page)

    page.goto("https://www.saucedemo.com/")

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_login_invalid_username(page: Page):
    login_page = LoginPage(page)

    page.goto("https://www.saucedemo.com/")

    login_page.enter_username("user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert login_page.get_error_message() == (
        "Epic sadface: Username and password do not match any user in this service"
    )