#from locators.locators import *
#from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.common.by import By
#from selenium import webdriver
from selenium.webdriver.common.by import By
#import selenium.webdriver.remote.webelement
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException


class BaseElement(object):
    "Base elements"
    element_timeout_value = 10

    def __init__(self, driver):
        self.driver = driver

    def getText(self,locatorr):
        self.wait_for_element_to_load(locatorr)
        text = self.driver.find_element(*locatorr).text
        return text
     
    def setText(self,locatorr,text):
        self.wait_for_element_to_load(locatorr)
        self.driver.find_element(*locatorr).send_keys(text)

    def click(self,locatorr):
        self.wait_for_element_to_load(locatorr)
        test = self.driver.find_element(*locatorr)
        test.click()

    def wait_for_element_to_load(self,element_locator):
        #self.driver.wait
        #selenium.webdriver.support.ui
        print element_locator
        print 'waiting for element...'
        WebDriverWait(self.driver, self.element_timeout_value).until(EC.presence_of_element_located(element_locator))
        print 'found element'
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "LoginForm")))"""


class submitButton(BaseElement):
    "submit element"
    """def click(self,locatorr):
        test = self.driver.find_element(*locatorr)
        test.click()"""


class inputText(BaseElement):

    def getValue(self,locator):
        text = self.driver.find_element(*locator).get_attribute('value').encode('utf-8')
        return text

    def setValue(self,locator,text):
        self.driver.find_element(*locator).send_keys(text)

    def clearValue(self,locator):
        self.driver.find_element(*locator).clear()


class checkBox(BaseElement):
    """checkbox element"""


class TEMPinputFile(BaseElement):
    "File upload input"
    def select_file(self):
        pass
    

class image(BaseElement):
    pass
