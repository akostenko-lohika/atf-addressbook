"""This is services file
"""
import random
import string
from faker import Faker
from pages import base_page, login, contacts, home, groups


class LoginService(object):
    """Login service"""
    def __init__(self, driver):
        self.driver = driver

    def login(self, username="admin", password="secret"):
        """Do login."""
        login_page = login.LoginPage(self.driver)
        login_page.enter_login_username(username)
        login_page.enter_login_password(password)
        login_page.submit_login_form()

    def logout(self):
        """Do logout."""
        some_page = base_page.BasePage(self.driver)
        some_page.click_logout_link()


class UsersService(object):
    """User service"""
    def create(self, username='testuser'):
        """Create user."""

    def delete(self, username='testuser'):
        """Delete user."""

class ContactsService(object):
    """Contacts service"""
    def __init__(self, driver):
        self.driver = driver

    def create(self, username='testuser'):
        """Add new contact."""
        homepage = home.HomePage(self.driver)
        homepage.click_menu_link_add_contact()
        contactspage1 = contacts.ContactAddPage(self.driver)
        #generating random string
        somestring = ''.join(random.sample(string.uppercase + string.digits, 10))
        contactspage1.enter_address(username)
        contactspage1.submit()
        # Now user should be located on next page
        #contactspage1.submit()
        contactspage2 = contacts.ContactEditPage(self.driver)
        #print contactspage2.get_value('firstname')
        #assert contactspage2.get_value('firstname'),'someAddress_'+somestring

        fake = Faker()
        #fake.seed(22)
        contactspage2.set_value('middlename', fake.last_name())
        contactspage2.set_value('lastname', fake.first_name())
        contactspage2.set_value('nickname', fake.last_name())
        contactspage2.set_value('photo', 'test_files/pictures/001.jpg')
        contactspage2.set_value('title', 'title'+somestring)
        contactspage2.set_value('company', 'company'+somestring)
        contactspage2.set_value('address', fake.address())
        contactspage2.set_value('home', fake.phone_number())
        contactspage2.set_value('mobile', fake.phone_number())
        contactspage2.set_value('work', fake.phone_number())
        contactspage2.set_value('fax', fake.phone_number())
        contactspage2.clear_value('email')
        contactspage2.set_value('email', fake.free_email())
        #   'email'+somestring)
        contactspage2.set_value('email2', fake.free_email())
        contactspage2.set_value('email3', fake.free_email())
        contactspage2.set_value('homepage', 'http://localhost/#'+somestring)
        contactspage2.set_value('bday', 'bday'+somestring)
        contactspage2.set_value('bmonth', 'bmonth'+somestring)
        contactspage2.set_value('byear', 'byear'+somestring)
        contactspage2.set_value('aday', 'aday'+somestring)
        contactspage2.set_value('amonth', 'amonth'+somestring)
        contactspage2.set_value('ayear', 'ayear'+somestring)
        contactspage2.set_value('new_group', 'new_group'+somestring)
        contactspage2.set_value('address2', fake.address())
        contactspage2.set_value('phone2', 'phone2'+somestring)
        contactspage2.set_value('notes', 'notes'+somestring)
        contactspage2.submit()
        # Now user should be located on next page
        #contactspage1.submit()
        #contactspage2 = contacts.ContactEditPage(self.driver)

    def delete(self, username='testuser'):
        """Delete contact."""


class GroupsService(object):
    """Groups service"""
    def __init__(self, driver):
        self.driver = driver

    def create(self, groupname='testgroup'):
        """Add new group."""
        homepage = home.HomePage(self.driver)
        homepage.click_menu_link_groups()
        groupspage = groups.GroupsPage(self.driver)
        groupspage.click_add_group()
        groupaddpage = groups.GroupAddPage(self.driver)
        groupaddpage.set_value('group_name', groupname)
        #groupaddpage.set_value('group_parent_id', 'some parent groups')
        groupaddpage.set_value('group_header', groupname+'group header')
        groupaddpage.set_value('group_footer', groupname+'group footer')
        groupaddpage.submit()
