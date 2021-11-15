from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on the first product')
def click_first_product(context):
    context.app.search_results_page.click_first_product()


@then('Verify {expected_result} text is shown')
def verify_text_shown(context, expected_result):
    context.app.search_results_page.verify_search_result_text(expected_result)