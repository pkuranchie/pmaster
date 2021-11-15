from behave import when, then


@when('Open cart page')
def open_cart_page(context):
    context.app.cart_page.open_cart_page()


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    context.app.header.verify_cart_count(expected_count)


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name(context.current_product_name)