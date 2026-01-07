from playwright.sync_api import Page, expect
from pages.page_product import ProductList, CartModal

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

    def click_cart_button(self):
        self.header.get_by_text("Cart").click()

    def click_products_button(self):
        self.header.get_by_text("Products").click()
        #page.locator('a:has(i)').filter(has_text="Products").click()
        
class HomePage():
    def __init__(self, page: Page):
        self.page = page
        self.footer = Footer(page)
        self.header = Header(page)
        self.product_list = ProductList(page)
        self.cart_modal = CartModal(page)

    def verify_homepage(self):
        expect(self.page).to_have_title("Automation Exercise")
