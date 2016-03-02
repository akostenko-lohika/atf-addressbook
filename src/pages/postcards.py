"""This is Contacts page. 
"""
from base_page import BasePage
from locators.locators import BaseLocators, ContactAddPageLocators, ContactEditPageLocators, ContactViewPageLocators
from elements.elements import inputText, submitButton
import time

URL_MAIN = "https://postcard-ua.com/postcard_ch.php?id=1"

class ContactAddPage(BasePage):
    """Contact Add page."""
    def enter_address(self, address):
        """Enter address."""
        inputText(self.driver).setValue(ContactAddPageLocators.addresses, address)

    def submit(self):
        """Submit form on page."""
        submitButton(self.driver).click(BaseLocators.submit)


class ContactEditPage(BasePage):
    """Contact Edit page."""
    def get_value(self, field_name):
        """Get value of some input on page."""
        newfield_name = getattr(ContactEditPageLocators, field_name)
        return inputText(self.driver).getValue(newfield_name)

    def set_value(self, field_name, new_value):
        """Set value in some input on page."""
        newfield_name = getattr(ContactEditPageLocators, field_name)
        inputText(self.driver).setValue(newfield_name, new_value)

    def clear_value(self, field_name):
        """Clear value in some input on page."""
        newfield_name = getattr(ContactEditPageLocators, field_name)
        inputText(self.driver).clearValue(newfield_name)

    def submit(self):
        """Submit form on page."""
        submitButton(self.driver).click(BaseLocators.submit)


class ContactViewPage(BasePage):
    """Contact View page."""
    def edit_contact(self):
        submitButton(self.driver).click(ContactViewPageLocators.modifiy)

    def print_contact(self):
        submitButton(self.driver).click(ContactViewPageLocators.print_button)
