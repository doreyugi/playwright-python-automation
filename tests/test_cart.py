from test_data.user_data import new_user
from test_data.payment_data import payment_info

# Test Case 12: Add Products in Cart
def test_add_products_cart(homepage):
    expected_products = []
    # 4. Click 'Products' button
    product_page = homepage.header.click_products_button()
    # 5. Hover over first product and click 'Add to cart'
    product_1 = product_page.product_list.get_nth_product_info(0)
    product_page.product_list.click_add_to_cart_nth_product(0)
    expected_products.append(product_1)
    # 6. Click 'Continue Shopping' button
    product_page.cart_modal.click_continue_shopping()
    # 7. Hover over second product and click 'Add to cart'
    product_2 = product_page.product_list.get_nth_product_info(1)
    product_page.product_list.click_add_to_cart_nth_product(1)
    expected_products.append(product_2)
    # 8. Click 'View Cart' button
    cart_page = product_page.cart_modal.click_view_cart()
    # 9. Verify both products are added to Cart
    cart_page.verify_cart_items()
    cart_page.verify_num_cart_items(2)
    # 10. Verify their prices, quantity and total price
    cart_page.verify_cart_items_details(expected_products)

# Test Case 13: Verify Product quantity in Cart
def test_add_multiple_quantity_cart(homepage):
    quantity = 4
    expected_products = []
    # 4. Click 'View Product' for any product on home page
    product_detail_page = homepage.product_list.click_view_nth_product(0)
    # 5. Verify product detail is opened
    product_detail_page.is_product_detail_visible()
    # 6. Increase quantity to 4
    product_detail_page.increase_quantity(quantity)
    # 7. Click 'Add to cart' button
    product_1 = product_detail_page.get_product_info()
    product_detail_page.click_add_to_cart()
    expected_products.append(product_1)
    # 8. Click 'View Cart' button
    cart_page = product_detail_page.cart_modal.click_view_cart()
    # 9. Verify that product is displayed in cart page with exact quantity
    cart_page.verify_cart_items_details(expected_products)

# Test Case 14: Place Order: Register while Checkout
def test_place_order_register_checkout(homepage):
    expected_products = []
    # 4. Add products to cart
    product_1 = homepage.product_list.get_nth_product_info(0)
    homepage.product_list.click_add_to_cart_nth_product(0)
    expected_products.append(product_1)
    homepage.product_list.cart_modal.click_continue_shopping()
    product_2 = homepage.product_list.get_nth_product_info(1)
    homepage.product_list.click_add_to_cart_nth_product(1)
    expected_products.append(product_2)
    # 5. Click 'Cart' button
    cart_page = homepage.cart_modal.click_view_cart()
    # 6. Verify that cart page is displayed
    cart_page.verify_cart_page()
    # 7. Click Proceed To Checkout
    cart_page.click_proceed_to_checkout()
    # 8. Click 'Register / Login' button
    signup_login_page = cart_page.checkout_modal.click_register_login()
    # 9. Fill all details in Signup and create account
    signup_login_page.signup(new_user.username, new_user.email)
    signup_login_page.fill_signup_form(new_user.password, new_user.DOB_day, new_user.DOB_month, new_user.DOB_year, new_user.first_name, new_user.last_name, new_user.company, new_user.address1, new_user.address2, new_user.country, new_user.state, new_user.city, new_user.zipcode, new_user.mobile_number)
    # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    signup_login_page.verify_signup_success_message()
    signup_login_page.click_continue_button()
    # 11. Verify ' Logged in as username' at top
    homepage.header.verify_logged_in_as_username(new_user.username)
    # 12.Click 'Cart' button
    cart_page = homepage.header.click_cart_button()
    # 13. Click 'Proceed To Checkout' button
    checkout_page = cart_page.click_proceed_to_checkout()
    # 14. Verify Address Details and Review Your Order
    checkout_page.verify_address_details(new_user)
    checkout_page.verify_billing_address_details(new_user)
    checkout_page.verify_order_review_section(expected_products)
    # 15. Enter description in comment text area and click 'Place Order'
    checkout_page.fill_comment("Please deliver between 9 AM to 5 PM.")
    payment_page = checkout_page.click_place_order()
    # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    payment_page.fill_payment_info(payment_info.name_on_card, payment_info.card_number, payment_info.cvc, payment_info.expiration_month, payment_info.expiration_year)
    # 17. Click 'Pay and Confirm Order' button
    payment_page.click_pay_and_confirm_order()
    # 18. Verify success message 'Your order has been placed successfully!'
    payment_page.verify_order_success_message()    
    # 19. Click 'Delete Account' button
    delete_account_page = homepage.header.click_delete_account_button()
    # 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    delete_account_page.verify_delete_account_page()
    delete_account_page.click_continue_button()