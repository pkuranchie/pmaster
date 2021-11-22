from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

HAM_MENU_ICON = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a.nav_a')
SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a[data-nav-role]')


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Input {search_word} into amazon search')
def search_amazon(context, search_word):
    context.app.header.input_search(search_word)


@when('Click on amazon search icon')
def click_search(context):
    context.app.header.click_search()


@when('Click Sign In from popup')
def click_sign_in_popup(context):
    e = context.driver.wait.until(EC.element_to_be_clickable((SIGN_IN_POPUP_BTN)), message='Sign in btn not clickable')
    e.click()


@when('Sign In pop up appears')
def sign_in_popup_appears(context):
    context.driver.wait.until(EC.element_to_be_clickable((SIGN_IN_POPUP_BTN)), message='Sign in btn not clickable')


@when('Wait for {sec} sec')
def wait_sec(context, sec):
    sleep(int(sec))


@when('Hover over language options')
def hover_over_language_options(context):
    context.app.header.hover_over_language_options()


@when('Hover over New Arrivals option')
def hover_over_new_arrivals_options(context):
    context.app.header.hover_over_new_arrivals_options()


@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department_by_alias(alias)


def verify_ham_menu(context):
     context.driver.find_element(*HAM_MENU_ICON)


@then('Verify {expected_amount} footer links are present')
def verify_footer_links_count(context, expected_amount):
    links = context.driver.find_elements(*FOOTER_LINKS)
    print(links)
    assert len(links) == int(expected_amount), f'Expected expected_amount   links, but got {len(links)}'

    for l in links:
        print(l.text)


@then('Verify Sign In pop up disappeared')
def verify_sign_in_disappeared(context):
    context.driver.wait.until(EC.invisibility_of_element((SIGN_IN_POPUP_BTN)), message='Sign in btn is visible')
    assert context.driver.current_url == 'https://www.amazon.com/'


@then('Verify correct options present')
def verify_lang_options_present(context):
    context.app.header.verify_lang_options_present()


@then('Verify deals are present')
def verify_deals_present(context):
    context.app.header.verify_deals_present()


@then('Verify {expected_department} department is selected')
def verify_correct_department_selected(context, expected_department):
    context.app.search_results_page.verify_correct_department_selected(expected_department)