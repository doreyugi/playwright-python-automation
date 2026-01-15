from playwright.sync_api import Page, expect

class Footer():
    def __init__(self, page: Page):
        self.page = page
        self.footer = self.page.locator('footer')

    def verify_subscription_text(self):
        expect(self.footer.get_by_text('Subscription')).to_be_visible()

    def enter_subscription(self, email):
        self.footer.locator("#susbscribe_email").fill(email)
        self.footer.locator("#subscribe").click()

    def verify_subscribe_success_text(self):
        expect(self.footer.get_by_text('You have been successfully subscribed!')).to_be_visible()

class Header():
    def __init__(self, page: Page):
        self.page = page
        self.header = self.page.locator('header')

    def verify_logged_in_as_username(self, username):
        expect(self.page.get_by_text(f'Logged in as {username}')).to_be_visible()

    def click_cart_button(self):
        from pages.page_cart import CartPage
        self.header.get_by_text("Cart").click()
        return CartPage(self.page)

    def click_products_button(self):
        from pages.page_product import ProductPage
        self.header.get_by_text("Products").click()
        #page.locator('a:has(i)').filter(has_text="Products").click()
        return ProductPage(self.page)
    
    def click_contact_us_button(self):
        from pages.page_contact_us import ContactUsPage
        self.header.get_by_text("Contact Us").click()
        return ContactUsPage(self.page)
    
    def click_test_cases_button(self):
        from pages.page_test_case import TestCasePage
        self.header.get_by_text("Test Cases").click()
        return TestCasePage(self.page)
    
    def click_signup_login_button(self):
        from pages.page_signup_login import SignupLoginPage
        self.header.get_by_text("Signup / Login").click()
        return SignupLoginPage(self.page)
    
    def click_logout_button(self):
        from pages.page_signup_login import SignupLoginPage
        self.header.get_by_text("Logout").click()
        return SignupLoginPage(self.page)
    
    def click_delete_account_button(self):
        from pages.page_signup_login import DeleteAccountPage
        self.header.get_by_text("Delete Account").click()
        return DeleteAccountPage(self.page)