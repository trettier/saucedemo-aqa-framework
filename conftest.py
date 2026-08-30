import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True
        )
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")
    yield page
    page.close()