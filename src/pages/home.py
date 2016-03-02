#from selenium.webdriver.common.by import By
#import selenium.webdriver.remote.webelement
#from selenium import * 
from base_page import BasePage
from locators.locators import HomePageLocators,LoginPageLocators
from elements.elements import inputText,submitButton

#class BasePage(object):
#    """Base class to initialize the base page that will be called from all pages"""
#
#    def __init__(self, driver):
#        self.driver = driver


class HomePage(BasePage):
    """Login page"""
    def search_on_page(self,string):
        inputText(self.driver).setValue(HomePageLocators.search_field, string)
    
    def enter_login_username(self,username):
        inputText(self.driver).setValue(LoginPageLocators.username_field, username)

    def enter_login_password(self,password):
        inputText(self.driver).setValue(LoginPageLocators.password_field, password)

    def submit_login_form(self):
        submitButton(self.driver).click(LoginPageLocators.submit_button)
