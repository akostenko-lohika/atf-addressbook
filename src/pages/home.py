"""This is Home page
"""
from pages.base_page import BasePage
from locators.locators import HomePageLocators
from elements.elements import InputText, WebComponent
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """Home page"""

    results_table_sort_column_photo = (By.CSS_SELECTOR, '[class*="column-1"]>a.fdTableSortTrigger')
    results_table_sort_column_name = (By.CSS_SELECTOR, '[class*="column-2"]>a.fdTableSortTrigger')
    results_table_sort_column_address = (By.CSS_SELECTOR, '[class*="column-3"]>a.fdTableSortTrigger')
    results_table_sort_column_email = (By.CSS_SELECTOR, '[class*="column-4"]>a.fdTableSortTrigger')
    results_table_sort_column_phone = (By.CSS_SELECTOR, '[class*="column-5"]>a.fdTableSortTrigger')
    sort_options_dict = {'photo' : 'results_table_sort_column_photo',
                         'name' : 'results_table_sort_column_name',
                         'address' : 'results_table_sort_column_address',
                         'email' : 'results_table_sort_column_email',
                         'phone' : 'results_table_sort_column_phone'
                         }


    def search_on_page(self, search_string):
        """Search some string in search filter."""
        search_field = InputText(self.driver, HomePageLocators.search_field)
        search_field.clear_value()
        search_field.set_value(search_string)

    def sort_table(self, name=('photo','name','address','email','phone')):
        #var_name = self.sort_options_dict[name]
        newfield_name = getattr(self, self.sort_options_dict[name])
        WebComponent(self.driver,newfield_name).click()
        #pass

    def sort_table_test(self, name=sort_options_dict):
        #var_name = self.sort_options_dict[name]
        newfield_name = getattr(self, self.sort_options_dict[name])
        WebComponent(self.driver,newfield_name).click()
        #pass