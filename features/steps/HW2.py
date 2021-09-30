from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@given('Open Amazon help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input Cancel Order into search field')
def search_amazon(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys(' Cancel order' + Keys.RETURN)





