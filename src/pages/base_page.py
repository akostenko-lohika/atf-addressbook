"""This is base page class."""
from locators.locators import BaseLocators
from elements.elements import WebComponent, Link, Image

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        """Initialize."""
        self.driver = driver

    def get_header_username(self):
        """Get specific element in page header."""
        return WebComponent(self.driver, BaseLocators.header_username).get_text()

    def click_header_logo(self):
        """Click specific element in page header."""
        Image(self.driver, BaseLocators.header_logo_link).click()
        #self.driver.find_element(*BaseLocators.header_logo_link).click()

    def click_menu_link_main(self):
        """Click specific element in page header."""
        Link(self.driver, BaseLocators.menu_link_main).click()

    def click_menu_link_add_contact(self):
        """Click specific element in page header."""
        Link(self.driver, BaseLocators.menu_link_add_contact).click()

    def click_menu_link_groups(self):
        """Click specific element in page header."""
        Link(self.driver, BaseLocators.menu_link_groups).click()

    def click_menu_link_birthdays(self):
        """Click specific element in page header."""
        Link(self.driver, BaseLocators.menu_link_birthdays).click()

    def click_menu_link_print_all(self):
        """Click specific element in page header."""
        Link(self.driver, BaseLocators.menu_link_print_all).click()

    def click_menu_link_print_phone(self):
        """Click specific element in page header."""
        Link(self.driver, BaseLocators.menu_link_print_phone).click()

    def click_menu_link_map(self):
        """Click specific element in page header."""
        Link(self.driver, BaseLocators.menu_link_map).click()

    def click_menu_link_export(self):
        """Click specific element in page header."""
        Link(self.driver, BaseLocators.menu_link_export).click()

    def click_menu_link_import(self):
        """Click specific element in page header."""
        Link(self.driver, BaseLocators.menu_link_import).click()

    def click_footer_link_sourceforge(self):
        """Click specific element in page footer."""
        Link(self.driver, BaseLocators.footer_link_sourceforge).click()

    def click_footer_link_release_notes(self):
        """Click specific element in page footer."""
        Link(self.driver, BaseLocators.footer_link_release_notes).click()

    def click_logout_link(self):
        """Click logout link."""
        Link(self.driver, BaseLocators.header_logout_link).click()

    def navigate_to(self, path_or_url):
        """Navigate to specific URL or page."""
        self.driver.get(path_or_url)

    def enter_field(self):
        """Enter value into some field."""
        pass

    def submit(self):
        """Submit page."""
        pass
