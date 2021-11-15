from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    PRODUCT_NAME = (By.ID, 'productTitle')
    PRICE_BUY_BOX = (By.ID, 'priceInsideBuyBox_feature_div')
    COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
    CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

    def open_product_page(self, product_id):
        self.open_page(f'dp/{product_id}/')

    def get_product_name(self) -> str:
        return self.find_element(*self.PRODUCT_NAME).text
        print(f'Current product: {product_name}')
        return product_name

    def click_add_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)



