from test_data.user_data import new_user, existing_user
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
def test_place_order_register_while_checkout(homepage):
    expected_products = []
    # 4. Add products to cart
    product_1 = homepage.product_list.get_nth_product_info(0)
    homepage.product_list.click_add_to_cart_nth_product(0)
    expected_products.append(product_1)
    homepage.cart_modal.click_continue_shopping()
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

# Test Case 15: Place Order: Register before Checkout
def test_place_order_register_before_checkout(homepage):
    expected_products = []
    # 4. Click 'Signup / Login' button
    signup_login_page = homepage.header.click_signup_login_button()
    # 5. Fill all details in Signup and create account
    signup_login_page.signup(new_user.username, new_user.email)
    signup_login_page.fill_signup_form(new_user.password, new_user.DOB_day, new_user.DOB_month, new_user.DOB_year, new_user.first_name, new_user.last_name, new_user.company, new_user.address1, new_user.address2, new_user.country, new_user.state, new_user.city, new_user.zipcode, new_user.mobile_number)
    # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    signup_login_page.verify_signup_success_message()
    signup_login_page.click_continue_button()
    # 7. Verify ' Logged in as username' at top
    homepage.header.verify_logged_in_as_username(new_user.username)
    # 8. Add products to cart
    product_1 = homepage.product_list.get_nth_product_info(0)
    homepage.product_list.click_add_to_cart_nth_product(0)
    expected_products.append(product_1)
    homepage.cart_modal.click_continue_shopping()
    product_2 = homepage.product_list.get_nth_product_info(1)
    homepage.product_list.click_add_to_cart_nth_product(1)
    expected_products.append(product_2)
    # 9. Click 'Cart' button
    cart_page = homepage.cart_modal.click_view_cart()
    # 10. Verify that cart page is displayed
    cart_page.verify_cart_page()
    # 11. Click Proceed To Checkout
    checkout_page = cart_page.click_proceed_to_checkout()
    # 12. Verify Address Details and Review Your Order
    checkout_page.verify_address_details(new_user)
    checkout_page.verify_billing_address_details(new_user)
    checkout_page.verify_order_review_section(expected_products)
    # 13. Enter description in comment text area and click 'Place Order'
    checkout_page.fill_comment("Please deliver between 9 AM to 5 PM.")
    payment_page = checkout_page.click_place_order()
    # 14. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    payment_page.fill_payment_info(payment_info.name_on_card, payment_info.card_number, payment_info.cvc, payment_info.expiration_month, payment_info.expiration_year)
    # 15. Click 'Pay and Confirm Order' button
    payment_page.click_pay_and_confirm_order()
    # 16. Verify success message 'Your order has been placed successfully!'
    payment_page.verify_order_success_message()    
    # 17. Click 'Delete Account' button
    delete_account_page = homepage.header.click_delete_account_button()
    # 18. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    delete_account_page.verify_delete_account_page()
    delete_account_page.click_continue_button()

# Test Case 16: Place Order: Login before Checkout
def test_place_order_login_before_checkout(homepage):
    expected_products = []
    # 4. Click 'Signup / Login' button
    signup_login_page = homepage.header.click_signup_login_button()
    # 5. Fill email, password and click 'Login' button
    signup_login_page.login(existing_user.email, existing_user.password)
    # 6. Verify ' Logged in as username' at top
    homepage.header.verify_logged_in_as_username(existing_user.username)
    # 7. Add products to cart
    product_1 = homepage.product_list.get_nth_product_info(0)
    homepage.product_list.click_add_to_cart_nth_product(0)
    expected_products.append(product_1)
    homepage.cart_modal.click_continue_shopping()
    product_2 = homepage.product_list.get_nth_product_info(1)
    homepage.product_list.click_add_to_cart_nth_product(1)
    expected_products.append(product_2)
    # 8. Click 'Cart' button
    cart_page = homepage.cart_modal.click_view_cart()
    # 9. Verify that cart page is displayed
    cart_page.verify_cart_page()
    # 10. Click Proceed To Checkout
    checkout_page = cart_page.click_proceed_to_checkout()
    # 11. Verify Address Details and Review Your Order
    checkout_page.verify_address_details(existing_user)
    checkout_page.verify_billing_address_details(existing_user)
    checkout_page.verify_order_review_section(expected_products)
    # 12. Enter description in comment text area and click 'Place Order'
    checkout_page.fill_comment("Please deliver between 9 AM to 5 PM.")
    payment_page = checkout_page.click_place_order()
    # 13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    payment_page.fill_payment_info(payment_info.name_on_card, payment_info.card_number, payment_info.cvc, payment_info.expiration_month, payment_info.expiration_year)
    # 14. Click 'Pay and Confirm Order' button
    payment_page.click_pay_and_confirm_order()
    # 15. Verify success message 'Your order has been placed successfully!'
    payment_page.verify_order_success_message()

# Test Case 17: Remove Products From Cart
def test_remove_products_cart(homepage):
    expected_products = []  
    # 4. Add products to cart
    product_1 = homepage.product_list.get_nth_product_info(0)
    homepage.product_list.click_add_to_cart_nth_product(0)
    expected_products.append(product_1)
    homepage.cart_modal.click_continue_shopping()
    product_2 = homepage.product_list.get_nth_product_info(1)
    homepage.product_list.click_add_to_cart_nth_product(1)
    expected_products.append(product_2)
    # 5. Click 'Cart' button
    cart_page = homepage.cart_modal.click_view_cart()
    # 6. Verify that cart page is displayed
    cart_page.verify_cart_page()
    # 7. Click 'X' button corresponding to particular product
    cart_page.click_remove_nth_product(0)
    expected_products.pop(0)
    # 8. Verify that product is removed from the cart
    cart_page.verify_num_cart_items(1)
    cart_page.verify_cart_items_details(expected_products)

# Test Case 20: Search Products and Verify Cart After Login
def test_search_products_and_verify_cart_after_login(homepage):
    expected_products = []
    # 3. Click on 'Products' button
    product_page = homepage.header.click_products_button()
    # 4. Verify user is navigated to ALL PRODUCTS page successfully
    product_page.is_all_products_page()
    # 5. Enter product name in search input and click search button
    keyword = "Top"
    product_page.search_product(keyword)
    # 6. Verify 'SEARCHED PRODUCTS' is visible
    product_page.is_searched_product_visible()
    # 7. Verify all the products related to search are visible
    product_page.product_list.is_product_list_visible()
    # 8. Add those products to cart
    product_1 = product_page.product_list.get_nth_product_info(0)
    product_page.product_list.click_add_to_cart_nth_product(0)
    expected_products.append(product_1)
    product_page.cart_modal.click_continue_shopping()
    product_2 = product_page.product_list.get_nth_product_info(1)
    product_page.product_list.click_add_to_cart_nth_product(1)
    expected_products.append(product_2)
    # 9. Click 'Cart' button and verify that products are visible in cart
    cart_page = product_page.cart_modal.click_view_cart()
    cart_page.verify_cart_items()
    cart_page.verify_num_cart_items(2)
    cart_page.verify_cart_items_details(expected_products)
    # 10. Click 'Signup / Login' button and submit login details
    signup_login_page = cart_page.header.click_signup_login_button()
    signup_login_page.login(existing_user.email, existing_user.password)
    # 11. Again, go to Cart page
    cart_page = homepage.header.click_cart_button()
    # 12. Verify that those products are visible in cart after login as well
    cart_page.verify_cart_items()
    cart_page.verify_num_cart_items(2)
    cart_page.verify_cart_items_details(expected_products)