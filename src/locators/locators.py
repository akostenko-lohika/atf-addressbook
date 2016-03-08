"""This is Locators class
"""
from selenium.webdriver.common.by import By


class BaseLocators(object):
    "Base locators, that are located on main page"
    header_username = (By.CSS_SELECTOR, "form[name='logout'] b")
    header_logout_link = (By.CSS_SELECTOR, "form[name='logout'] a")
    #header_logo_link = (By.ID, "logo")
    header_logo_link = (By.CSS_SELECTOR, "#header>a>img")
    menu_link_main = (By.CSS_SELECTOR, "#nav>ul>li>a")
    menu_link_add_contact = (By.CSS_SELECTOR, ".all>a")
    menu_link_groups = (By.CSS_SELECTOR, ".admin>a")
    menu_link_birthdays = (By.XPATH, ".//*[@id='nav']/ul/li[4]/a")
    menu_link_print_all = (By.XPATH, ".//*[@id='nav']/ul/li[5]/a")
    menu_link_print_phone = (By.XPATH, ".//*[@id='nav']/ul/li[6]/a")
    menu_link_map = (By.XPATH, ".//*[@id='nav']/ul/li[7]/a")
    menu_link_export = (By.XPATH, ".//*[@id='nav']/ul/li[8]/a")
    menu_link_import = (By.XPATH, ".//*[@id='nav']/ul/li[9]/a")
    footer_link_sourceforge = (By.XPATH, ".//*[@id='footer']/ul/li/a[1]")
    footer_link_release_notes = (By.XPATH, ".//*[@id='footer']/ul/li/a[2]")
    # Basic locators
    submit = (By.CSS_SELECTOR, "input[type='submit']")


class LoginPageLocators(BaseLocators):
    """Locators for login page"""
    username_field = (By.NAME, "user")
    password_field = (By.NAME, "pass")
    submit_button = (By.CSS_SELECTOR, "form#LoginForm > input[type='submit']")
    login_form = (By.ID, "LoginForm")


class HomePageLocators(BaseLocators):
    """Locators for login page"""
    search_field = (By.CSS_SELECTOR, "#search-az>form>input")


class ContactAddPageLocators(BaseLocators):
    """Locators for ContactAdd page"""
    #nextButton = (By.CSS_SELECTOR, "#content>form>input")
    addresses = (By.CSS_SELECTOR, "#content>form>textarea")


class ContactEditPageLocators(BaseLocators):
    """Locators for ContactEdit page"""
    #submit = (By.CSS_SELECTOR, "input[type='submit']")
    firstname = (By.CSS_SELECTOR, "input[name='firstname']")
    middlename = (By.CSS_SELECTOR, "input[name='middlename']")
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


class ContactViewPageLocators(BaseLocators):
    """Locators for ContactViewPage page"""
    modifiy = (By.CSS_SELECTOR, "input[name='modifiy']")
    print_button = (By.CSS_SELECTOR, "input[name='print']")


class GroupsPageLocators(BaseLocators):
    """Locators for Groups page"""
    add_group_button = (By.CSS_SELECTOR, "input[name='new']")
    edit_group_button = (By.CSS_SELECTOR, "input[name='edit']")
    delete_group_button = (By.CSS_SELECTOR, "input[name='delete']")
    #test


class GroupAddPageLocators(BaseLocators):
    """Locators for Groups Add page"""
    group_name = (By.CSS_SELECTOR, "input[name='group_name']")
    group_parent_id = (By.CSS_SELECTOR, "select[name='group_parent_id']")
    group_header = (By.CSS_SELECTOR, "textarea[name='group_header']")
    group_footer = (By.CSS_SELECTOR, "textarea[name='group_footer']")
    enter_info_button = (By.CSS_SELECTOR, "input[type='submit']")


class GroupEditPageLocators(BaseLocators):
    """Locators for Groups Edit page"""
    pass


class GroupUpdatedPageLocators(BaseLocators):
    """Locators for Groups Updated page"""
    status = (By.CSS_SELECTOR, ".msgbox")
    #driver.findElement(By.xpath("//div[@id='recipient_div_3']/text()")).getText()
