from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Cancel Items or Orders text is shown')
def verify_text_shown(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    expected_result = "Cancel Items or Orders"
    assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result} '
