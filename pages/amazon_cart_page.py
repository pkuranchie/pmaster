from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    PRODUCT_NAME = (By.CSS_SELECTOR, '#sc-active-cart li')

    def open_cart_page(self):
        self.open_page('gp/cart/view.html?ref_#nav_cart')

    def verify_product_name(self, expected_name):
        self.verify_text(expected_name, *self.PRODUCT_NAME)