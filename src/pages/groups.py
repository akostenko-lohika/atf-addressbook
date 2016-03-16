"""This is Groups page
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.locators import BaseLocators, GroupsPageLocators, \
    GroupAddPageLocators, GroupUpdatedPageLocators
from elements.elements import WebComponent, CheckBox, InputText, SubmitButton


class GroupsPage(BasePage):
    """Groups main page"""

    def click_add_group(self):
        """click Add Group button."""
        SubmitButton(self.driver, GroupsPageLocators.add_group_button).click()

    def click_edit_group(self):
        """click Edit Group button."""
        SubmitButton(self.driver, GroupsPageLocators.edit_group_button).click()

    def click_delete_group(self):
        """click Delete Group button."""
        SubmitButton(self.driver, GroupsPageLocators.delete_group_button).click()

    def select_group(self, group_name):
        """click checkbox for specific Group."""
        locator = (By.CSS_SELECTOR, "input[title='Select (" + group_name + ")']")
        CheckBox(self.driver, locator).click()


class GroupAddPage(BasePage):
    """Group Add page"""
    expected_mess_for_added = "A new group has been entered into the address" \
                              " book.\nreturn to the group page"
    expected_mess_for_updated = "Group record has been updated.\n" \
                                "return to the group page"
    expected_mess_for_deleted = "Group has been removed.\n" \
                                "return to the group page"

    def get_value(self, field_name):
        """Get value from specified input field."""
        newfield_name = getattr(GroupAddPageLocators, field_name)
        return InputText(self.driver, newfield_name).get_value()

    def set_value(self, field_name, new_value):
        """Set value in specified input field."""
        newfield_name = getattr(GroupAddPageLocators, field_name)
        InputText(self.driver, newfield_name).set_value(new_value)

    def clear_value(self, field_name):
        """Clear value in specified input field."""
        newfield_name = getattr(GroupAddPageLocators, field_name)
        InputText(self.driver, newfield_name).clear_value()

    def submit(self):
        """Submit form."""
        SubmitButton(self.driver, BaseLocators.submit).click()


class GroupEditPage(GroupAddPage):
    """created for testing purposes"""


class GroupUpdatedPage(BasePage):
    """created for testing purposes"""
    expected_mess_for_added = "A new group has been entered into the address" \
                              " book.\nreturn to the group page"
    expected_mess_for_updated = "Group record has been updated.\n" \
                                "return to the group page"
    expected_mess_for_deleted = "Group has been removed.\n return to the group page"

    def get_status_message(self):
        """Get status message on page."""
        return WebComponent(self.driver, GroupUpdatedPageLocators.status).get_text()
