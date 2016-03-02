#from selenium.webdriver.common.by import By
#import selenium.webdriver.remote.webelement
#from selenium import * 
from selenium.webdriver.common.by import By
from base_page import BasePage
from locators.locators import BaseLocators,GroupsPageLocators,GroupAddPageLocators,GroupUpdatedPageLocators
from elements.elements import submitButton,checkBox,inputText


class GroupsPage(BasePage):
    """Groups main page"""
    def click_add_group(self):
        """click Add Group button"""
        submitButton(self.driver).click(GroupsPageLocators.add_group_button)
    
    def click_edit_group(self):
        """click Edit Group button"""
        submitButton(self.driver).click(GroupsPageLocators.edit_group_button)
        
    def click_delete_group(self):
        """click Delete Group button"""
        submitButton(self.driver).click(GroupsPageLocators.delete_group_button)

    def select_group(self,group_name):
        """click checkbox for specific Group"""
        locator = (By.CSS_SELECTOR, "input[title='Select ("+group_name+")']")
        checkBox(self.driver).click(locator)


class GroupAddPage(BasePage):
    """Group Add page"""
    
    """
    expected_status_message_for_added_group = "A new group has been entered into the address book.\n\
return to the group page"
    expected_status_message_for_updated_group = "Group record has been updated.\n\
return to the group page"
    expected_status_message_for_deleted_group = "Group has been removed.\n\
return to the group page"
"""


    def get_value(self,field_name):
        newfield_name = getattr(GroupAddPageLocators, field_name)
        return inputText(self.driver).getValue(newfield_name)
    
    def set_value(self,field_name,new_value):
        newfield_name = getattr(GroupAddPageLocators, field_name)
        inputText(self.driver).setValue(newfield_name, new_value)

    def clear_value(self,field_name):
        newfield_name = getattr(GroupAddPageLocators, field_name)
        inputText(self.driver).clearValue(newfield_name)
        
    def submit(self):
        submitButton(self.driver).click(BaseLocators.submit)
        

class GroupEditPage(GroupAddPage):
    """created for testing purposes"""


class GroupUpdatedPage(BasePage):
    """created for testing purposes"""
    expected_status_message_for_added_group = "A new group has been entered into the address book.\n\
return to the group page"
    expected_status_message_for_updated_group = "Group record has been updated.\n\
return to the group page"
    expected_status_message_for_deleted_group = "Group has been removed.\n\
return to the group page"
    def get_status_message(self):
        div_element = self.driver.find_element(*GroupUpdatedPageLocators.status).text
        #div_element = self.driver.find_element(*GroupUpdatedPageLocators.status).get_attribute('textContent')
        return div_element