#import pytest
from selenium import webdriver
from config.config import *
#from selenium.webdriver.common.by import By
# Imported the following for explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login import LoginPage
from pages.base_page import BasePage
#from selenium.webdriver.chrome.service.time import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class BaseTest(object):
    """Base class to initialize the base test that will be called from all tests"""

    def setup_class(self):
        print ("basic setup into module")
        if test_browser == 'Chrome':
            self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)
            #self.driver = webdriver.Chrome()
            print "Should be Firefox"
        else:
            self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        print "opening browser"+test_browser
        self.driver.get(URL_MAIN)
        ####WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "LoginForm")))
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.login_form))


    def Asetup_class(self):
        print ("basic setup into module")
        if test_browser == 'Chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        print "opening firefox"
        self.driver.get(URL_MAIN)
        ####WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "LoginForm")))
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.login_form))

    def do_login(self):
        test_page = LoginPage(self.driver)
        test_page.enter_login_username(valid_username)
        test_page.enter_login_password(valid_password)
        test_page.submit_login_form()

    def do_logout(self):
        test_page = BasePage(self.driver)
        test_page.click_logout_link()


    def create_screeshot(self, name, path=None):
        self.driver.save_screenshot(path+'/'+name)


    def teardown_class(self):
        print ("basic teardown into module")
        self.driver.close()

