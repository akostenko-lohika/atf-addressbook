"""This is Contacts page.
"""
from pages.base_page import BasePage
from locators.locators import BaseLocators, ContactAddPageLocators,\
    ContactEditPageLocators, ContactViewPageLocators
from elements.elements import InputText, SubmitButton


class ContactAddPage(BasePage):
    """Contact Add page."""
    def enter_address(self, address):
        """Enter address."""
        InputText(self.driver, ContactAddPageLocators.addresses).set_value(address)

    def submit(self):
        """Submit form on page."""
        SubmitButton(self.driver, BaseLocators.submit).click()


class ContactEditPage(BasePage):
    """Contact Edit page."""
    def get_value(self, field_name):
        """Get value of some input on page."""
        newfield_name = getattr(ContactEditPageLocators, field_name)
        return InputText(self.driver, newfield_name).get_value()

    def set_value(self, field_name, new_value):
        """Set value in some input on page."""
        newfield_name = getattr(ContactEditPageLocators, field_name)
        InputText(self.driver, newfield_name).set_value(new_value)

    def clear_value(self, field_name):
        """Clear value in some input on page."""
        newfield_name = getattr(ContactEditPageLocators, field_name)
        InputText(self.driver, newfield_name).clear_value()

    def submit(self):
        """Submit form on page."""
        SubmitButton(self.driver, BaseLocators.submit).click()


class ContactViewPage(BasePage):
    """Contact View page."""
    def edit_contact(self):
        """click Edit Contact button."""
        SubmitButton(self.driver, ContactViewPageLocators.modifiy).click()

    def print_contact(self):
        """click Print Contact button."""
        SubmitButton(self.driver, ContactViewPageLocators.print_button).click()
