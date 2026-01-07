from pages.page_cart import CartPage
from pages.page_product import AllProductPage, ProductDetailPage
from pages.page_homepage import HomePage
from playwright.sync_api import Page

# def test_cart_item(page: Page):
#     homepage = HomePage(page)
#     cart_page = CartPage(page)
#     product_page = AllProductPage(page)
#     # 1. Launch browser
#     # 2. Navigate to url 'http://automationexercise.com'
#     page.goto('http://automationexercise.com')
#     # 3. Verify that home page is visible successfully
#     homepage.verify_homepage()
#     homepage.header.click_cart_button()
#     cart_page.verify_cart_items()


# Test Case 12: Add Products in Cart
def test_add_products_cart(page: Page):
    homepage = HomePage(page)
    cart_page = CartPage(page)
    product_page = AllProductPage(page)
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    homepage.verify_homepage()
    # 4. Click 'Products' button
    homepage.header.click_products_button()
    # 5. Hover over first product and click 'Add to cart'
    product_page.product_list.click_add_to_cart_nth_product(0)
    # 6. Click 'Continue Shopping' button
    product_page.cart_modal.click_continue_shopping()
    # 7. Hover over second product and click 'Add to cart'
    product_page.product_list.click_add_to_cart_nth_product(1)
    # 8. Click 'View Cart' button
    product_page.cart_modal.click_view_cart()
    # 9. Verify both products are added to Cart
    cart_page.verify_cart_items()
    cart_page.verify_num_cart_items(2)
    # 10. Verify their prices, quantity and total price
    cart_page.verify_cart_items_detail()

# Test Case 13: Verify Product quantity in Cart
def test_add_multiple_quantity_cart(page: Page):
    homepage = HomePage(page)
    cart_page = CartPage(page)
    product_detail_page = ProductDetailPage(page)
    quantity = 4
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    homepage.verify_homepage()
    # 4. Click 'View Product' for any product on home page
    homepage.product_list.click_view_nth_product(0)
    # 5. Verify product detail is opened
    product_detail_page.is_product_detail_visible()
    # 6. Increase quantity to 4
    product_detail_page.increase_quantity(quantity)
    # 7. Click 'Add to cart' button
    product_detail_page.click_add_to_cart()
    # 8. Click 'View Cart' button
    product_detail_page.cart_modal.click_view_cart()
    # 9. Verify that product is displayed in cart page with exact quantity
    cart_page.verify_nth_cart_item_quantity(0, quantity)