#from selenium.webdriver.common.by import By
#import selenium.webdriver.remote.webelement
#from selenium import * 
#from selenium.webdriver.common.by import By
from base_page import BasePage
from locators.locators import LoginPageLocators
from elements.elements import inputText,submitButton

#class BasePage(object):
#    """Base class to initialize the base page that will be called from all pages"""
#
#    def __init__(self, driver):
#        self.driver = driver


class LoginPage(BasePage):
    """Login page"""
    
    def enter_login_username(self,username):
        #self.driver.find_element(*LoginPageLocators.username_field).send_keys(username)
        inputText(self.driver).setValue(LoginPageLocators.username_field, username)

    def enter_login_password(self,password):
        inputText(self.driver).setValue(LoginPageLocators.password_field, password)

    def submit_login_form(self):
        #mysubmit_button = submit_element(self.driver)
        #mysubmit_button.click(LoginPageLocators.submit_button)
        submitButton(self.driver).click(LoginPageLocators.submit_button)
        #self.driver.find_element(*LoginPageLocators.submit_button).click()
        

