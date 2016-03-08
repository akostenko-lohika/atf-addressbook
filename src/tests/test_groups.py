#import pytest
#from selenium import webdriver
from pages import home,groups
#from config.config import *
#from selenium.webdriver.common.by import By
# Imported the following for explicit wait
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest
#from locators.locators import LoginPageLocators,ContactEditPageLocators
from services.services import LoginService,GroupsService
#import random
#import string
#from elements.elements import inputText

#should try fixtures definition @pytest.fixture ...
#like def open_browser():

class Test_Groups(BaseTest):

    def test_groups_view_without_service(self):
        """
        try to add new contact without using groups service
        """
                
        loginpage = LoginService(self.driver)
        loginpage.login()
        homepage = home.HomePage(self.driver)
        homepage.click_menu_link_groups()
        groupspage = groups.GroupsPage(self.driver)
        groupspage.click_add_group()
        groupaddpage = groups.GroupAddPage(self.driver)
        groupaddpage.set_value('group_name', 'some group')
        #groupaddpage.set_value('group_parent_id', 'some parent groups')
        groupaddpage.set_value('group_header', 'group header')
        groupaddpage.set_value('group_footer', 'group footer')
        groupaddpage.submit()
        groupaddedpage = groups.GroupUpdatedPage(self.driver)
        assert groupaddedpage.get_status_message()==groupaddedpage.expected_mess_for_added
        groupaddedpage.click_menu_link_groups()
        groupspage.select_group('some group')
        groupspage.click_edit_group()
        groupeditpage = groups.GroupEditPage(self.driver)
        groupeditpage.clear_value('group_name')
        groupeditpage.set_value('group_name', 'somevalue')
        groupeditpage.submit()
        assert groupaddedpage.get_status_message()==groupaddedpage.expected_mess_for_updated
        groupeditpage.click_menu_link_groups()
        groupspage.select_group('somevalue')
        groupspage.click_delete_group()

        #groupspage.create()

    def test_groups_view_with_service(self):
        """
        try to add new contact using service
        """
        #loginpage = LoginService(self.driver)
        #loginpage.login()
        GroupsService(self.driver).create("hehehe")

    def teardown_class(self):
        print ("basic teardown into module")
        self.driver.close()
