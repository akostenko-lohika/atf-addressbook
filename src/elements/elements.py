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



class Component(object):
    """Basic Component Class, probably needs to be removed"""
    def __init__(self, driver):
        self.driver = driver
    """
    def TEMPis_available(self):
        print "inside COMPONENT: is_available"
        #self.driver.execute_script("document.write('<a href=None>Add Bookmark</a>');")
        #self.driver.execute_script("document.write('<a href=None>Add Bookmark from component is_available</a>');")
        pass

    def TEMPwaitUntilAvailable(self):
        print "inside COMPONENT: waitUntilAvailable"
        aaa = Wait(object)
        return aaa.WaitforComponent(self).toBeAvailable()"""


class Wait(Component):
    """Basic Wait Class, probably needs to be removed"""
    default_timeout = 240
    default_retry_delay = 1
    component = None
    """def TTTWaitforComponent(self,Component):
        self._component = Component
        return self

    def TTTtoBeAvailable(self):
        timePassed = 0
        while timePassed<self.default_timeout:
            if self._component.is_available():
                print "COMPONENT FOUND"
                return self._component
            timePassed = timePassed+self.delay()
        if not self._component.is_available():
            raise ('Oh no!Timeout after'+str(self.default_timeout)+'milliseconds')
        return self._component

    def TTTdelay(self):
        time.sleep(self.default_retry_delay)
        return self.default_retry_delay"""


class WebComponent(Component):
    locator = None
    findByMethod = None #from selenium.webdriver.common.by import By
    def __init__(self, driver, By):
        super(WebComponent, self).__init__(driver)
        self.findByMethod = By
        #self.waitUntilAvailable()

    def is_available(self):
        try:
            return self.get_web_element()
        except:
            return False

    def get_web_element(self):
        #return WebDriverWait(self.driver, 2).until(self.driver.find_element(*self.findByMethod))
        return self.driver.find_element(*self.findByMethod)

    def get_attribute(self,attribute_name):
        return self.get_web_element().get_attribute(attribute_name)

    def wait_until_element_invisible(self):
        """
        WebDriverWait wait = new WebDriverWait(yourWebDriver, 10);
        wait.until(ExpectedConditions.invisibilityOfElementLocated(By.id("yourSavingModalDialogDiv")));
        :return:
        """
        pass

    def waitUntilAvailable(self):
        print "I'm inside WebComponent: waitUntilAvailable()"
        try:
            print "I'm inside WebComponent: waitUntilAvailable(): first attempt"
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.findByMethod))
        except:
            try:
                print "I'm inside WebComponent: waitUntilAvailable(): second attempt"
                WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located(self.findByMethod))
            except:
                pass

        try:
            print "I'm inside WebComponent: waitUntilAvailable(): now will check element_to_be_clickable"
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.findByMethod))
        except:
            print "element_to_be_clickable failed"

        """
        try:
            print "I'm inside WebComponent: waitUntilAvailable(): second attempt"
            WebDriverWait(self.driver, 240).until(EC.visibility_of_element_located(self.findByMethod))
        except:
            pass
        """

        #WebDriverWait(self.driver, 240).until(EC.visibility_of_element_located(self.findByMethod))
        #visibility_of_element_located((self.by, self.value)))

        """ VOVAs METHOD
        try:

            WebDriverWait(self.drv, wait).until(ec.visibility_of_element_located((self.by, self.value)))
        except TimeoutException:
            # raise Exception("Can't wait the following element on page --> " + self.by + ' = ' + self.value +
            #                 "for " + str(wait) + " seconds")
            print "Can't wait element with <{1}> '{0}' on page for {2} seconds --> ".format(self.by,
                            self.value, wait)
            raise
            # print "Can't wait following element on page -->", self.by, ' = ', self.value
            # return False
        """

    def click(self):
        self.get_web_element().click()

    def get_text(self):
        return self.get_web_element().text


class Link(WebComponent):
    """Link element"""
    def __init__(self, driver, By):
        super(Link, self).__init__(driver, By)
        self.findByMethod = By
        self.waitUntilAvailable()

    def scroll_to_element(self,element):
        """Get location of element on page"""
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
    """
    def click(self):
        #self.waitUntilAvailable()
        #progress_bar_element_loading = WebComponent(self.driver,BaseLocators.progress_bar_loading)
        #progress_bar_element_loaded = WebComponent(self.driver,BaseLocators.progress_bar_loaded)
        #print progress_bar_element_loading.is_available()
        #print progress_bar_element_loaded.is_available()
        #if WebComponent(self.driver,BaseLocators.progress_bar_loaded).is_available():
        #    #print progress_bar_element_loaded
        #    print self.driver.find_element(*BaseLocators.progress_bar_loaded).value_of_css_property('visibility')
        #    print self.driver.find_element(*BaseLocators.progress_bar_loaded).get_attribute('max')
        #    print self.driver.find_element(*BaseLocators.progress_bar_loaded).get_attribute('value')
        element_to_click = self.getWebElement()
        #self.get_location_on_page(element_to_click)
        while not self.is_progress_bar_loading():
            print "sleeping because there is progress bar loading"
            time.sleep(3)
        element_to_click.click()
        #self.getWebElement().click()

    def click_menu_link(self):
        #if self.waitUntilAvailable():
        #    self.getWebElement().click()
        #if not self.is_available():
        #    print "Waiting for Link inside click_menu_link()"
        #self.waitUntilAvailable()
        element_to_click = self.getWebElement()
        #self.get_location_on_page(element_to_click)
        element_to_click.click()
        #self.getWebElement().click()

    def click_fast(self):
        self.click_menu_link()
    """


class SubmitButton(WebComponent):
    """Submit element"""
    def click(self):
        self.get_web_element().click()


class InputText(WebComponent):
    """Input element"""
    def get_value(self):
        text = self.get_web_element().get_attribute("value").encode("utf-8")
        return text

    def set_value(self,text):
        self.get_web_element().send_keys(text)

    def clear_value(self):
        self.get_web_element().clear()


class CheckBox(WebComponent):
    """Checkbox element"""


class Image(WebComponent):
    """Image element"""






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
