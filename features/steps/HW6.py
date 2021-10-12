from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@given('Open Amazon T&C page')
def amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


@when('Store original windows')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    print(f'Current window handle: {context.original_window } ')


@when('Click on Amazon Privacy Notice link')
def amazon_privacy_notice_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']").click()


@when('Switch to the newly opened window')
def switch_opened_window(context):
    all_window_handles = context.driver.window_handles
    print(all_window_handles)
    context.driver.switch_to.window(all_window_handles[1])  # [0, 1]
    print(f'Current window handle (after switch): {context.driver.current_window_handle}')


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_opened(context):
    assert 'https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ' in context.driver.current_url, \
        f'Error, https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ not opened'


@then('User can close new window and switch back to original')
def close_new_window_switch_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)







