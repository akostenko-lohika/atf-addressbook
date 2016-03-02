#import pytest
from config.config import *
from pages import login
# Imported the following for explicit wait
from base_test import BaseTest
from pages.base_page import BasePage
from services.services import LoginService

#should try fixtures definition @pytest.fixture ...
#like def open_browser():

class Test_Click_Links(BaseTest):
    """Test to verify that login page works"""

    """def setup_class(self):
        print ("basic setup into module")
        self.driver = webdriver.Firefox()
        print "opening firefox"
        self.driver.get(URL_MAIN)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "LoginForm")))"""
       
    #lines = super(Test_Click_Links, self).setup_class()
        
    def test_click_logo_link(self):
        """
        try to click logo link
        """
        test_page = BasePage(self.driver)
        test_page.click_header_logo()
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "logout")))
        #assert self.driver.find_element_by_name("logout")
        #assert (login_page.get_header_username()),"(admin)"

    def test_click_menu_link_main(self):
        """
        try to click main link from menu
        """
        LoginService(self.driver).login()
        test_page = BasePage(self.driver)
        test_page.click_menu_link_main()

    def test_click_menu_link_add_contact(self):
        """
        try to click main link from menu
        """
        test_page = login.LoginPage(self.driver)
        #test_page.enter_login_username(username="admin")
        #test_page.enter_login_password("secret")
        #test_page.submit_login_form()
        test_page.click_menu_link_add_contact()


    """def teardown_class(self):
        print ("basic teardown into module")
        self.driver.close()"""
