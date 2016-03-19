"""This is Login page
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.elements import InputText, SubmitButton


class LoginPage(BasePage):
    """Login page"""
    username_field = (By.NAME, "user")
    password_field = (By.NAME, "pass")
    submit_button = (By.CSS_SELECTOR, "form#LoginForm > input[type='submit']")
    login_form = (By.ID, "LoginForm")

    def enter_login_username(self, username):
        """Enter value into username field."""
        InputText(self.driver, self.username_field).set_value(username)

    def enter_login_password(self, password):
        """Enter value into password field."""
        InputText(self.driver, self.password_field).set_value(password)

    def submit_login_form(self):
        """Click submit button."""
        SubmitButton(self.driver, self.submit_button).click()
