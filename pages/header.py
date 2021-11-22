from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Page
from time import sleep


class Header(Page):
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')
    DEPARTMENT_OPTIONS = (By.CSS_SELECTOR, '#searchDropdownBox option')
    CART = (By.ID, 'nav-cart-count')
    FLAG = (By.CSS_SELECTOR, ".icp-nav-flag.icp-nav-flag-us")
    SPANISH_LANG_LINK = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    ENGLISH_LANG_LINK = (By.XPATH, "//header[@id='navbar-main']//*[contains(text(),'English - EN' )]")

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FILED)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def hover_over_language_options(self):
        lang = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang)
        actions.perform()

    def select_department_by_alias(self, alias):
        select = Select(self.find_element(*self.DEPARTMENT_SELECT))
        select.select_by_value(f'search-alias={alias}')

    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)

    def verify_lang_options_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG_LINK)
        self.find_element(*self.ENGLISH_LANG_LINK)
