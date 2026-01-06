from playwright.sync_api import Page
from pages.page_homepage import HomePage
from pages.page_cart import CartPage

email = "banana@gmail.com"

# Test Case 10: Verify Subscription in home page
def test_subscription_homepage(page: Page):
    homepage = HomePage(page)
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    homepage.verify_homepage()
    # 4. Scroll down to footer
    # 5. Verify text 'SUBSCRIPTION'
    homepage.footer.verify_subscription_text()
    # 6. Enter email address in input and click arrow button
    homepage.footer.enter_subscription(email)
    # 7. Verify success message 'You have been successfully subscribed!' is visible
    homepage.footer.verify_subscribe_success_text()

# Test Case 11: Verify Subscription in Cart page
def test_subscription_cart_page(page: Page):
    homepage = HomePage(page)
    cart_page = CartPage(page)
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    homepage.verify_homepage()
    # 4. Click 'Cart' button
    homepage.header.click_cart_button()
    # 5. Verify that cart page is visible successfully
    cart_page.verify_cart_page()
    # 6. Scroll down to footer
    # 7. Verify text 'SUBSCRIPTION'
    cart_page.footer.verify_subscription_text()
    # 8. Enter email address in input and click arrow button
    cart_page.footer.enter_subscription(email)
    # 9. Verify success message 'You have been successfully subscribed!' is visible
    cart_page.footer.verify_subscribe_success_text()