"""This is Home page
"""
from pages.base_page import BasePage
from locators.locators import HomePageLocators
from elements.elements import InputText


class HomePage(BasePage):
    """Home page"""
    def search_on_page(self, search_string):
        """Search some string in search filter."""
        InputText(self.driver, HomePageLocators.search_field).set_value(search_string)
