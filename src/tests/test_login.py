#import pytest
from selenium import webdriver
from pages import login
from config.config import *
from selenium.webdriver.common.by import By
# Imported the following for explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest
from locators.locators import LoginPageLocators
from services.services import LoginService

#should try fixtures definition @pytest.fixture ...
#like def open_browser():

class Test_Login(BaseTest):
    """Test to verify that login page works"""

    """def setup_class(self):
        print "test" """

    def test_login_with_invalid_credentials(self):
        """
        try to login with invalid user credentials
        """
        login_page = login.LoginPage(self.driver)
        login_page.enter_login_username(username="admin")
        login_page.enter_login_password("secrets")
        login_page.submit_login_form()
        # Wait until page is loaded and check whether there is logout form
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "LoginForm")))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.login_form))
        #EC.presence_of_element_located
        #assert self.driver.find_element_by_name("pass")

    def test_login_with_valid_credentials(self):
        """
        try to login with valid user credentials
        """
        login_page = login.LoginPage(self.driver)
        login_page.enter_login_username(username="admin")
        login_page.enter_login_password("secret")
        login_page.submit_login_form()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "logout")))
        assert self.driver.find_element_by_name("logout")
        assert (login_page.get_header_username()),"(admin)"

    def test_login_with_valid_credentials_and_service(self):
        """
        try to login with valid user credentials and service
        """
        somevar = LoginService(self.driver)
        somevar.logout()
        somevar.login()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "logout")))
        assert self.driver.find_element_by_name("logout")
        assert (login.LoginPage(self.driver).get_header_username()),"(admin)"




    """def teardown_class(self):
        print ("basic teardown into module")
        self.driver.close()"""
