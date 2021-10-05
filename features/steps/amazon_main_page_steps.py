from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HAM_MENU_ICON = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a.nav_a')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {search_word} into amazon search')
def search_amazon(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)


@when('Click on amazon search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify hamburger menu icon is present')
def verify_ham_menu(context):
     context.driver.find_element(*HAM_MENU_ICON)


@then('Verify {expected_amount} footer links are present')
def verify_footer_links_count(context, expected_amount):
    links = context.driver.find_elements(*FOOTER_LINKS)
    print(links)
    assert len(links) == int(expected_amount), f'Expected expected_amount   links, but got {len(links)}'

    for l in links:
        print(l.text)



