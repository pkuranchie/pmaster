from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResults(Page):
    PRODUCT_PRICE = (By.XPATH, "//div[@class='a-section a-spacing-none a-spacing-top-small']/h2/a")
    SEARCH_RESULT_TEXT = By.XPATH, "//span[@class='a-color-state a-text-bold']"

    def verify_search_result_text(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT_TEXT)

    def click_first_product(self):
        self.find_element(*self.PRODUCT_PRICE).click()



