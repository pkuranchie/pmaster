from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResults(Page):
    PRODUCT_PRICE = (By.XPATH, "//div[@class='a-section a-spacing-none a-spacing-top-small']/h2/a")
    SEARCH_RESULT_TEXT = By.XPATH, "//span[@class='a-color-state a-text-bold']"
    BOOKS = (By.CSS_SELECTOR, "#nav-subnav[data-category='books']")
    PC = (By.CSS_SELECTOR, "#nav-subnav[data-category='pc']")
    DEPARTMENT_LOCATOR = (By.CSS_SELECTOR, "#nav-subnav[data-category='{CATEGORY}']")

    def get_expected_category_locator(self, expected_category):
        return [self.DEPARTMENT_LOCATOR[0], self.DEPARTMENT_LOCATOR[1].replace('{CATEGORY}', expected_category)]

    def verify_search_result_text(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT_TEXT)

    def click_first_product(self):
        self.find_element(*self.PRODUCT_PRICE).click()

    def verify_correct_department_selected(self, expected_department: str):
        locator = self.get_expected_category_locator(expected_department)
        self.find_element(*locator)



