"""This is Contacts page.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.elements import InputText, SubmitButton


class ContactAddPage(BasePage):
    """Contact Add page."""
    addresses = (By.CSS_SELECTOR, "#content>form>textarea")
    def enter_address(self, address):
        """Enter address."""
        InputText(self.driver, self.addresses).set_value(address)


class ContactEditPage(BasePage):
    """Contact Edit page."""

    firstname = (By.CSS_SELECTOR, "input[name='firstname']")
    middlename = (By.CSS_SELECTOR, "input[name='middlename']")
    lastname = (By.CSS_SELECTOR, "input[name='lastname']")
    nickname = (By.CSS_SELECTOR, "input[name='nickname']")
    photo = (By.CSS_SELECTOR, "input[name='photo']")
    title = (By.CSS_SELECTOR, "input[name='title']")
    company = (By.CSS_SELECTOR, "input[name='company']")
    address = (By.CSS_SELECTOR, "textarea[name='address']")
    home = (By.CSS_SELECTOR, "input[name='home']")
    mobile = (By.CSS_SELECTOR, "input[name='mobile']")
    work = (By.CSS_SELECTOR, "input[name='work']")
    fax = (By.CSS_SELECTOR, "input[name='fax']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    email2 = (By.CSS_SELECTOR, "input[name='email2']")
    email3 = (By.CSS_SELECTOR, "input[name='email3']")
    homepage = (By.CSS_SELECTOR, "input[name='homepage']")
    bday = (By.CSS_SELECTOR, "select[name='bday']")
    bmonth = (By.CSS_SELECTOR, "select[name='bmonth']")
    byear = (By.CSS_SELECTOR, "input[name='byear']")
    aday = (By.CSS_SELECTOR, "select[name='aday']")
    amonth = (By.CSS_SELECTOR, "select[name='amonth']")
    ayear = (By.CSS_SELECTOR, "input[name='ayear']")
    new_group = (By.CSS_SELECTOR, "select[name='new_group']")
    address2 = (By.CSS_SELECTOR, "textarea[name='address2']")
    phone2 = (By.CSS_SELECTOR, "input[name='phone2']")
    notes = (By.CSS_SELECTOR, "textarea[name='notes']")


    def get_value(self, field_name):
        """Get value of some input on page."""
        newfield_name = getattr(self, field_name)
        return InputText(self.driver, newfield_name).get_value()

    def set_value(self, field_name, new_value):
        """Set value in some input on page."""
        newfield_name = getattr(self, field_name)
        InputText(self.driver, newfield_name).set_value(new_value)

    def clear_value(self, field_name):
        """Clear value in some input on page."""
        newfield_name = getattr(self, field_name)
        InputText(self.driver, newfield_name).clear_value()


class ContactViewPage(BasePage):
    """Contact View page."""

    modifiy = (By.CSS_SELECTOR, "input[name='modifiy']")
    print_button = (By.CSS_SELECTOR, "input[name='print']")

    def edit_contact(self):
        """click Edit Contact button."""
        SubmitButton(self.driver, self.modifiy).click()

    def print_contact(self):
        """click Print Contact button."""
        SubmitButton(self.driver, self.print_button).click()
