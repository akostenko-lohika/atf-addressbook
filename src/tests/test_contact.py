#import pytest
#from selenium import webdriver
from pages import contacts,home
#from config.config import *
#from selenium.webdriver.common.by import By
# Imported the following for explicit wait
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest
#from locators.locators import LoginPageLocators,ContactEditPageLocators
from services.services import LoginService, ContactsService
import random
import string
#from elements.elements import inputText

#should try fixtures definition @pytest.fixture ...
#like def open_browser():

class Test_Contact(BaseTest):

    def test_contact_add_without_service(self):
        """
        try to add new contact
        """
        loginpage = LoginService(self.driver)
        loginpage.login()
        # DO SOME SCREENSHOTS
        # self.create_screeshot('screenie222.png','/tmp')
        homepage = home.HomePage(self.driver)
        homepage.click_menu_link_add_contact()
        contactspage1 = contacts.ContactAddPage(self.driver)
        #generating random string
        somestring = ''.join(random.sample(string.uppercase + string.digits,10))
        contactspage1.enter_address('someAddress_'+somestring)
        contactspage1.submit()
        # Now user should be located on next page
        #contactspage1.submit()
        contactspage2 = contacts.ContactEditPage(self.driver)
        print contactspage2.get_value('firstname')
        assert contactspage2.get_value('firstname'),'someAddress_'+somestring
        
        contactspage2.set_value('middlename','middlename'+somestring)
        contactspage2.set_value('lastname','lastname'+somestring)
        contactspage2.set_value('nickname','nickname'+somestring)
        contactspage2.set_value('photo','/Users/andrijkostenko/Test-python/12605283_787259251406544_5802194393579230887_o.jpg')
        contactspage2.set_value('title','title'+somestring)
        contactspage2.set_value('company','company'+somestring)
        contactspage2.set_value('address','address'+somestring)
        contactspage2.set_value('home','home'+somestring)
        contactspage2.set_value('mobile','mobile'+somestring)
        contactspage2.set_value('work','work'+somestring)
        contactspage2.set_value('fax','fax'+somestring)
        contactspage2.clear_value('email')
        contactspage2.set_value('email','email'+somestring)
        contactspage2.set_value('email2','email2'+somestring)
        contactspage2.set_value('email3','email3'+somestring)
        contactspage2.set_value('homepage','http://localhost/#'+somestring)
        contactspage2.set_value('bday','bday'+somestring)
        contactspage2.set_value('bmonth','bmonth'+somestring)
        contactspage2.set_value('byear','byear'+somestring)
        contactspage2.set_value('aday','aday'+somestring)
        contactspage2.set_value('amonth','amonth'+somestring)
        contactspage2.set_value('ayear','ayear'+somestring)
        contactspage2.set_value('new_group','new_group'+somestring)
        contactspage2.set_value('address2','address2'+somestring)
        contactspage2.set_value('phone2','phone2'+somestring)
        contactspage2.set_value('notes','notes'+somestring)
        contactspage2.submit()
          
        #homepageconhome.HomePage(self.driver)
        #homepage.click_menu_link_add_contact()
        
        """
            firstname = (By.CSS_SELECTOR, "input[name='firstname']")
    lastname = (By.CSS_SELECTOR, "input[name='lastname']")
    nickname = (By.CSS_SELECTOR, "input[name='nickname']")
    photo = (By.CSS_SELECTOR, "input[name='photo']")
    title = (By.CSS_SELECTOR, "input[name='title']")
    company = (By.CSS_SELECTOR, "input[name='company']")
    address = (By.CSS_SELECTOR, "textarea[name='address']")
    home = (By.CSS_SELECTOR, "input[name='home']")
    mobile = (By.CSS_SELECTOR, "input[name='mobile']")
    work = (By.CSS_SELECTOR, "input[name='work']")
    fax = (By.CSS_SELECTOR, "input[name='fax']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    email2 = (By.CSS_SELECTOR, "input[name='email2']")
    email3 = (By.CSS_SELECTOR, "input[name='email3']")
    homepage = (By.CSS_SELECTOR, "input[name='homepage']")
    bday = (By.CSS_SELECTOR, "select[name='bday']")
    bmonth = (By.CSS_SELECTOR, "select[name='bmonth']")
    byear = (By.CSS_SELECTOR, "input[name='byear']")
    aday = (By.CSS_SELECTOR, "select[name='aday']")
    amonth = (By.CSS_SELECTOR, "select[name='amonth']")
    ayear = (By.CSS_SELECTOR, "input[name='ayear']")
    new_group = (By.CSS_SELECTOR, "select[name='new_group']")    
    address2 = (By.CSS_SELECTOR, "textarea[name='address2']")
    phone2 = (By.CSS_SELECTOR, "input[name='phone2']")
    notes = (By.CSS_SELECTOR, "textarea[name='notes']")
        """
        
        
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "logout")))
        #assert self.driver.find_element_by_name("logout")
        #assert (login.LoginPage(self.driver).get_header_username()),"(admin)"

    def test_contact_add_with_service(self):
        """
        try to add new contact using service
        """
        #loginpage = LoginService(self.driver)
        #loginpage.login()
        contactspage = ContactsService(self.driver)
        contactspage.create()
        


    """def teardown_class(self):
        print ("basic teardown into module")
        self.driver.close()"""
