from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import LOGIN_PAGE_URL


class LoginPage(BasePage):

    def open_login_page(self):
        self.open_page(LOGIN_PAGE_URL)

    def login(self, email, password):
        self.find_element(
            LoginPageLocators.EMAIL_INPUT
        ).send_keys(email)

        self.find_element(
            LoginPageLocators.PASSWORD_INPUT
        ).send_keys(password)

        self.click_element(
            LoginPageLocators.LOGIN_BUTTON
        )