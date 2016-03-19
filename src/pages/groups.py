"""This is Groups page
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.elements import WebComponent, CheckBox, InputText, SubmitButton


class GroupsPage(BasePage):
    """Groups main page"""

    add_group_button = (By.CSS_SELECTOR, "input[name='new']")
    edit_group_button = (By.CSS_SELECTOR, "input[name='edit']")
    delete_group_button = (By.CSS_SELECTOR, "input[name='delete']")


    def click_add_group(self):
        """click Add Group button."""
        SubmitButton(self.driver, self.add_group_button).click()

    def click_edit_group(self):
        """click Edit Group button."""
        SubmitButton(self.driver, self.edit_group_button).click()

    def click_delete_group(self):
        """click Delete Group button."""
        SubmitButton(self.driver, self.delete_group_button).click()

    def select_group(self, group_name):
        """click checkbox for specific Group."""
        locator = (By.CSS_SELECTOR, "input[title='Select (" + group_name + ")']")
        CheckBox(self.driver, locator).click()


class GroupAddPage(BasePage):
    """Group Add page"""

    group_name = (By.CSS_SELECTOR, "input[name='group_name']")
    group_parent_id = (By.CSS_SELECTOR, "select[name='group_parent_id']")
    group_header = (By.CSS_SELECTOR, "textarea[name='group_header']")
    group_footer = (By.CSS_SELECTOR, "textarea[name='group_footer']")
    enter_info_button = (By.CSS_SELECTOR, "input[type='submit']")


    expected_mess_for_added = "A new group has been entered into the address" \
                              " book.\nreturn to the group page"
    expected_mess_for_updated = "Group record has been updated.\n" \
                                "return to the group page"
    expected_mess_for_deleted = "Group has been removed.\n" \
                                "return to the group page"

    def get_value(self, field_name):
        """Get value from specified input field."""
        newfield_name = getattr(self, field_name)
        return InputText(self.driver, newfield_name).get_value()

    def set_value(self, field_name, new_value):
        """Set value in specified input field."""
        newfield_name = getattr(self, field_name)
        InputText(self.driver, newfield_name).set_value(new_value)

    def clear_value(self, field_name):
        """Clear value in specified input field."""
        newfield_name = getattr(self, field_name)
        InputText(self.driver, newfield_name).clear_value()


class GroupEditPage(GroupAddPage):
    """created for testing purposes"""


class GroupUpdatedPage(BasePage):
    """created for testing purposes"""

    status = (By.CSS_SELECTOR, ".msgbox")

    expected_mess_for_added = "A new group has been entered into the address" \
                              " book.\nreturn to the group page"
    expected_mess_for_updated = "Group record has been updated.\n" \
                                "return to the group page"
    expected_mess_for_deleted = "Group has been removed.\n return to the group page"

    def get_status_message(self):
        """Get status message on page."""
        return WebComponent(self.driver, self.status).get_text()
