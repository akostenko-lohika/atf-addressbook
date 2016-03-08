"""This is Login page
"""
from pages.base_page import BasePage
from locators.locators import LoginPageLocators
from elements.elements import InputText, SubmitButton


class LoginPage(BasePage):
    """Login page"""
    def enter_login_username(self, username):
        """Enter value into username field."""
        InputText(self.driver, LoginPageLocators.username_field).set_value(username)

    def enter_login_password(self, password):
        """Enter value into password field."""
        InputText(self.driver, LoginPageLocators.password_field).set_value(password)

    def submit_login_form(self):
        """Click submit button."""
        SubmitButton(self.driver, LoginPageLocators.submit_button).click()
