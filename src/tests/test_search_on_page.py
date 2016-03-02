#import pytest
#from selenium import webdriver
#from pages import login
#from config.config import *
#from selenium.webdriver.common.by import By
# Imported the following for explicit wait
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest
#from pages.base_page import BasePage
from pages.home import HomePage


#should try fixtures definition @pytest.fixture ...
#like def open_browser():

class Test_Search_on_main_page(BaseTest):
    """Test to verify that login page works"""

    """def setup_class(self):
        print ("basic setup into module")
        self.driver = webdriver.Firefox()
        print "opening firefox"
        self.driver.get(URL_MAIN)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "LoginForm")))"""
       
    #lines = super(Test_Click_Links, self).setup_class()

    def test_search_with_some_word(self):
        self.do_login()
        test_page = HomePage(self.driver)
        test_page.search_on_page('hehe')

    def test_search_with_some_word2(self):
        #self.do_login()
        test_page = HomePage(self.driver)
        test_page.search_on_page('hehe')
        test_page.navigate_to("5.ua")

