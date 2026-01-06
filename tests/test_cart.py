from pages.page_cart import CartPage
from pages.page_product import AllProductPage
from pages.page_homepage import HomePage
from playwright.sync_api import Page

# Test Case 12: Add Products in Cart
def test_subscription_cart_page(page: Page):
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
    product_page.click_add_to_cart_nth_product(0)
    # 6. Click 'Continue Shopping' button
    product_page.click_continue_shopping()
    # 7. Hover over second product and click 'Add to cart'
    product_page.click_add_to_cart_nth_product(1)
    # 8. Click 'View Cart' button
    product_page.click_view_cart()
    # 9. Verify both products are added to Cart
    # 10. Verify their prices, quantity and total price