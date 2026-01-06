from pages.page_homepage import Footer
from playwright.sync_api import Page, expect

class CartPage():
    def __init__(self, page: Page):
        self.page = page
        self.footer = Footer(page)

    def verify_cart_page(self):
        expect(self.page.locator("#cart_items").get_by_text("Shopping Cart")).to_be_visible()