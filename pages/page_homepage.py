from playwright.sync_api import Page, expect
from pages.page_product import ProductList, CartModal
from pages.page_header_footer import Header, Footer

class HomePage():
    def __init__(self, page: Page):
        self.page = page
        self.footer = Footer(page)
        self.header = Header(page)
        self.product_list = ProductList(page)
        self.cart_modal = CartModal(page)

    def verify_homepage(self):
        expect(self.page).to_have_title("Automation Exercise")
