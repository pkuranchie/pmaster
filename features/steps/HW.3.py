from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon Home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Amazon chart icon')
def click_chart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/gp/cart/view.html?ref_=nav_cart']").click()




