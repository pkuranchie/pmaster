from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@then('Verify user can click through colors')
def verity_can_click_through_colors(context):
    expected_colors = ['Black', 'Blue', 'Burgundy', 'Caramel', 'Denim Blue',
                       'Gray', 'Green', 'Khaki', 'Light Green(also One Size)',
                       'Light-green', 'Pink', 'Red', 'White', 'Yellow']

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    # for i in range(len(colors)):
    #   colors[i].click()
    #  current_color = context.driver.find_element(*CURRENT_COLOR).text
    # assert current_color == expected_colors[i], f'Error, expected {expected_colors[i]} did not match {current_color}'

    actual_colors = []
    for color in colors:
        color.click()
        actual_colors += [context.driver.find_element(*CURRENT_COLOR).text]
        print(f'Actual colors, {actual_colors}')

    assert expected_colors == actual_colors, f'Error expected {expected_colors} did not match {actual_colors}'
