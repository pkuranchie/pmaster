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
    NEW_ARRIVAL = (By.XPATH, "//a[@href='/s/ref=sr_hi_2/?_encoding=UTF8&bbn=17020138011&ie=UTF8&qid=1498592471&rh=n%3A7141123011%2Cn%3A17020138011&ref_=sv_sl_6']")
    ARRIVAL_LINK =(By.XPATH, "//a[@href='/s?i=fashion-womens&bbn=19225926011&rh=n%3A7141123011%2Cn%3A19225926011%2Cn%3A%217141124011%2Cn%3A7147440011&s=date-desc-rank&pf_rd_i=17020138011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=ef277cd2-3f4d-47ec-95c2-e1e8f71edf3c&pf_rd_r=TTPGSTXKPBP77T2TCK2T&pf_rd_s=merchandised-search-2&pf_rd_t=101&qid=1559772727&rnid=7147440011&ref=sv_sl_fl_na_1']")

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FILED)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def hover_over_language_options(self):
        lang = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang)
        actions.perform()

    def hover_over_new_arrivals_options(self):
        arrival = self.find_element(*self.NEW_ARRIVAL)
        actions = ActionChains(self.driver)
        actions.move_to_element(arrival)
        actions.perform()

    def select_department_by_alias(self, alias):
        select = Select(self.find_element(*self.DEPARTMENT_SELECT))
        select.select_by_value(f'search-alias={alias}')

    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)

    def verify_lang_options_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG_LINK)
        self.find_element(*self.ENGLISH_LANG_LINK)

    def verify_deals_present(self):
        self.wait_for_element_appear(*self.NEW_ARRIVAL)
        self.find_element(*self.ARRIVAL_LINK)



