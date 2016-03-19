"""This is Home page
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from elements.elements import InputText, Link


class HomePage(BasePage):
    """Home page"""
    search_field = (By.CSS_SELECTOR, "#search-az>form>input")
    results_table_sort_column_photo =\
        (By.CSS_SELECTOR, '[class*="column-1"]>a.fdTableSortTrigger')
    results_table_sort_column_name =\
        (By.CSS_SELECTOR, '[class*="column-2"]>a.fdTableSortTrigger')
    results_table_sort_column_addr =\
        (By.CSS_SELECTOR, '[class*="column-3"]>a.fdTableSortTrigger')
    results_table_sort_column_email =\
        (By.CSS_SELECTOR, '[class*="column-4"]>a.fdTableSortTrigger')
    results_table_sort_column_phone =\
        (By.CSS_SELECTOR, '[class*="column-5"]>a.fdTableSortTrigger')
    sort_options_dict = {'photo': 'results_table_sort_column_photo',
                         'name': 'results_table_sort_column_name',
                         'address': 'results_table_sort_column_addr',
                         'email': 'results_table_sort_column_email',
                         'phone': 'results_table_sort_column_phone'}

    def search_on_page(self, search_string):
        """Search some string in search filter."""
        search_field = InputText(self.driver, self.search_field)
        search_field.clear_value()
        search_field.set_value(search_string)

    def sort_table(self, name=('photo', 'name', 'address', 'email', 'phone')):
        """Sort table by one of table columns."""
        Link(self.driver, getattr(self, self.sort_options_dict[name])).click()
