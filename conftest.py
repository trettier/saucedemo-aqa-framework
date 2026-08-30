import pytest
from playwright.sync_api import Browser, Page, sync_playwright


YANDEX_BROWSER = r"C:\Program Files\Yandex\YandexBrowser\Application\browser.exe"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            executable_path=YANDEX_BROWSER,
            headless=False
        )

        yield browser

        browser.close()


@pytest.fixture
def page(browser: Browser) -> Page:
    page = browser.new_page()

    yield page

    page.close()