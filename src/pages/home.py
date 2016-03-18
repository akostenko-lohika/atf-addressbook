"""This is Home page
"""
from pages.base_page import BasePage
from locators.locators import HomePageLocators
from elements.elements import InputText, WebComponent
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """Home page"""

    sort_column = (By.CSS_SELECTOR, "#search-az>form>input")


    def search_on_page(self, search_string):
        """Search some string in search filter."""
        InputText(self.driver, HomePageLocators.search_field).set_value(search_string)

    def sort_table(self, sort_column):
        WebComponent(self.driver,sort_column).click()
        pass