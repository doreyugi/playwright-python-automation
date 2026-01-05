from playwright.sync_api import Page, expect
import re

class AllProductPage():
    def __init__(self, page: Page):
        self.page = page
        self.product_list = self.page.locator('.features_items .col-sm-4')
    
    def is_all_products_page(self):
        expect(self.page).to_have_title(re.compile(r"\ball\s+products\b", re.IGNORECASE))

    def is_product_list_visible(self):
        expect(self.product_list.first).to_be_visible() #at least one product is visible
    
    def click_view_nth_product(self, idx):
        self.product_list.nth(idx).get_by_text("View Products").click()


class ProductDetailPage():
    def __init__(self, page: Page):
        self.page = page