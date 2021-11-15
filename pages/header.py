from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CART = (By.ID, 'nav-cart-count')

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FILED)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)
