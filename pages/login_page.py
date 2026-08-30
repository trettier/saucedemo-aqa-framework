from playwright.sync_api import Page


class LoginPage:

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page: Page):
        self.page = page

    def enter_username(self, username: str):
        self.page.locator(self.USERNAME_INPUT).fill(username)

    def enter_password(self, password: str):
        self.page.locator(self.PASSWORD_INPUT).fill(password)

    def click_login(self):
        self.page.locator(self.LOGIN_BUTTON).click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()