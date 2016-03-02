"""This is base page class. 
"""
#from selenium.webdriver.common.by import By
#import selenium.webdriver.remote.webelement
from locators.locators import BaseLocators
from elements.elements import BaseElement

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        """Initialize."""
        self.driver = driver


    #def click_menu_link(self):
    #    BaseElement(self.driver).click(BaseLocators.open_menu_link)

    def get_header_username(self):
        """Get specific element in page header."""
        #return self.driver.find_element(*BaseLocators.header_username).text
        return BaseElement(self.driver).getText(BaseLocators.header_username)

    def click_header_logo(self):
        """Click specific element in page header."""
        self.driver.find_element(*BaseLocators.header_logo_link).click()

    def click_menu_link_main(self):
        """Click specific element in page header."""
        self.driver.find_element(*BaseLocators.menu_link_main).click()

    def click_menu_link_add_contact(self):
        """Click specific element in page header."""
        self.driver.find_element(*BaseLocators.menu_link_add_contact).click()

    def click_menu_link_groups(self):
        """Click specific element in page header."""
        self.driver.find_element(*BaseLocators.menu_link_groups).click()

    def click_menu_link_birthdays(self):
        """Click specific element in page header."""
        self.driver.find_element(*BaseLocators.menu_link_birthdays).click()

    def click_menu_link_print_all(self):
        """Click specific element in page header."""
        self.driver.find_element(*BaseLocators.menu_link_print_all).click()

    def click_menu_link_print_phone(self):
        """Click specific element in page header."""
        self.driver.find_element(*BaseLocators.menu_link_print_phone).click()

    def click_menu_link_map(self):
        """Click specific element in page header."""
        self.driver.find_element(*BaseLocators.menu_link_map).click()

    def click_menu_link_export(self):
        """Click specific element in page header."""
        self.driver.find_element(*BaseLocators.menu_link_export).click()

    def click_menu_link_import(self):
        """Click specific element in page header."""
        self.driver.find_element(*BaseLocators.menu_link_import).click()

    def click_footer_link_sourceforge(self):
        """Click specific element in page footer."""
        self.driver.find_element(*BaseLocators.footer_link_sourceforge).click()

    def click_footer_link_release_notes(self):
        """Click specific element in page footer."""
        self.driver.find_element(*BaseLocators.footer_link_release_notes).click()

    def click_logout_link(self):
        """Click logout link."""
        self.driver.find_element(*BaseLocators.header_logout_link).click()

    def navigate_to(self, path_or_url):
        """Navigate to specific URL or page."""
        self.driver.get(path_or_url)

    def enter_field(self):
        """Enter value into some field."""
        pass

    def submit(self):
        """Submit page."""
        pass
