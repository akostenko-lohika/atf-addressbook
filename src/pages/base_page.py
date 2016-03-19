"""This is base page class."""
from selenium.webdriver.common.by import By
#from locators.locators import BaseLocators
from elements.elements import WebComponent, Link, Image, InputText

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    #" Base locators, that are located on main page "
    header_username = (By.CSS_SELECTOR, "form[name='logout'] b")
    header_logout_link = (By.CSS_SELECTOR, "form[name='logout'] a")
    # header_logo_link = (By.ID, "logo")
    header_logo_link = (By.CSS_SELECTOR, "#header>a>img")
    menu_link_main = (By.CSS_SELECTOR, "#nav>ul>li>a")
    menu_link_add_contact = (By.CSS_SELECTOR, ".all>a")
    menu_link_groups = (By.CSS_SELECTOR, ".admin>a")
    menu_link_birthdays = (By.XPATH, ".//*[@id='nav']/ul/li[4]/a")
    menu_link_print_all = (By.XPATH, ".//*[@id='nav']/ul/li[5]/a")
    menu_link_print_phone = (By.XPATH, ".//*[@id='nav']/ul/li[6]/a")
    menu_link_map = (By.XPATH, ".//*[@id='nav']/ul/li[7]/a")
    menu_link_export = (By.XPATH, ".//*[@id='nav']/ul/li[8]/a")
    menu_link_import = (By.XPATH, ".//*[@id='nav']/ul/li[9]/a")
    footer_link_sourceforge = (By.XPATH, ".//*[@id='footer']/ul/li/a[1]")
    footer_link_release_notes = (By.XPATH, ".//*[@id='footer']/ul/li/a[2]")
    # Basic locators
    submit_button = (By.CSS_SELECTOR, "input[type='submit']")


    def __init__(self, driver):
        """Initialize."""
        self.driver = driver

    def get_header_username(self):
        """Get specific element in page header."""
        return WebComponent(self.driver, self.header_username).get_text()

    def click_header_logo(self):
        """Click specific element in page header."""
        Image(self.driver, self.header_logo_link).click()
        #self.driver.find_element(*BaseLocators.header_logo_link).click()

    def click_menu_link_main(self):
        """Click specific element in page header."""
        Link(self.driver, self.menu_link_main).click()

    def click_menu_link_add_contact(self):
        """Click specific element in page header."""
        Link(self.driver, self.menu_link_add_contact).click()

    def click_menu_link_groups(self):
        """Click specific element in page header."""
        Link(self.driver, self.menu_link_groups).click()

    def click_menu_link_birthdays(self):
        """Click specific element in page header."""
        Link(self.driver, self.menu_link_birthdays).click()

    def click_menu_link_print_all(self):
        """Click specific element in page header."""
        Link(self.driver, self.menu_link_print_all).click()

    def click_menu_link_print_phone(self):
        """Click specific element in page header."""
        Link(self.driver, self.menu_link_print_phone).click()

    def click_menu_link_map(self):
        """Click specific element in page header."""
        Link(self.driver, self.menu_link_map).click()

    def click_menu_link_export(self):
        """Click specific element in page header."""
        Link(self.driver, self.menu_link_export).click()

    def click_menu_link_import(self):
        """Click specific element in page header."""
        Link(self.driver, self.menu_link_import).click()

    def click_footer_link_sourceforge(self):
        """Click specific element in page footer."""
        Link(self.driver, self.footer_link_sourceforge).click()

    def click_footer_link_release_notes(self):
        """Click specific element in page footer."""
        Link(self.driver, self.footer_link_release_notes).click()

    def click_logout_link(self):
        """Click logout link."""
        Link(self.driver, self.header_logout_link).click()

    def navigate_to(self, path_or_url):
        """Navigate to specific URL or page."""
        self.driver.get(path_or_url)

    def enter_field(self):
        """Enter value into some field."""
        pass

    def submit(self):
        """Submit page."""
        InputText(self.driver, self.submit_button).click()
