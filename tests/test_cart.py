from test_data.user_data import existing_user

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

# Test Case 22: Add to cart from Recommended items
def test_add_to_cart_from_recommended_items(homepage):
    expected_products = []
    # 3. Scroll to bottom of page
    # 4. Verify 'RECOMMENDED ITEMS' are visible
    homepage.verify_recommendation_items_text()
    # 5. Click on 'Add to cart' on recommended product
    product_1 = homepage.get_nth_recommended_product_info(0)
    homepage.click_add_to_cart_nth_recommendation_item(0)
    expected_products.append(product_1)
    # 6. Click 'View Cart' button
    cart_page = homepage.cart_modal.click_view_cart()
    # 7. Verify that product is added to cart
    cart_page.verify_cart_items()
    cart_page.verify_num_cart_items(1)
    cart_page.verify_cart_items_details(expected_products)