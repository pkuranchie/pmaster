from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


LINKS = (By.CSS_SELECTOR, "_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq")
LINKS_XPATH = (By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']/ul/li/div/a")


@given('Amazon Best Sellers page')
def open_amazon_bestsellers(context):
    context.driver.get("https://www.amazon.com")
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2')


@then('Verify {expected_amount} links present')
def verify_links_present(context, expected_amount):
    boxes = context.driver.find_elements(*LINKS_XPATH)
    print(boxes)
    assert len(boxes) == int(expected_amount), f'Expected expected_amount   links, but got {len(boxes)}'
