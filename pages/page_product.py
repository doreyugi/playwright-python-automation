from playwright.sync_api import Page, expect
import re

class AllProductPage():
    def __init__(self, page: Page):
        self.page = page
        self.product_list = self.page.locator('.features_items .col-sm-4')
        self.search_bar = self.page.locator('[id="search_product"]')
        self.search_button = self.page.locator('[id="submit_search"]')
        self.searched_product_text = self.page.get_by_text("Searched Product")
        self.cart_modal = self.page.locator("#cartModal")
    
    def is_all_products_page(self):
        expect(self.page).to_have_title(re.compile(r"\ball\s+products\b", re.IGNORECASE))

    def is_product_list_visible(self):
        expect(self.product_list.first).to_be_visible() #at least one product is visible
    
    def click_view_nth_product(self, idx):
        self.product_list.nth(idx).get_by_text("View Product").click()

    def click_add_to_cart_nth_product(self, idx):
        self.product_list.nth(idx).get_by_text("Add to cart").click()

    def click_continue_shopping(self):
        self.cart_modal.get_by_role('button', name="Continue Shopping").click()

    def click_view_cart(self):
        self.cart_modal.get_by_role('link', name="View Cart").click()

    def search_product(self, keyword):
        self.search_bar.fill(keyword)
        self.search_button.click()

    def is_searched_product_visible(self):
        expect(self.searched_product_text).to_be_visible()

    def is_search_result_visible(self, keyword):
        self.is_product_list_visible()
        # Check each product is rendered correctly
        count = self.product_list.count()
        for i in range(count):
            expect(self.product_list.nth(i)).to_be_visible()
        # # Check each product is relevant
        # for i in range(count):
        #     product_name = self.product_list.nth(i).locator("p").first
        #     expect(product_name).to_contain_text(keyword,ignore_case=True)


class ProductDetailPage():
    def __init__(self, page: Page):
        self.page = page
        #product name, category, price, availability, condition, brand
        self.product_info = page.locator(".product-information")
        self.product_name = self.product_info.locator("h2")
        self.product_category = self.product_info.get_by_text("Category:")
        self.product_price = self.product_info.get_by_text("Rs.")
        self.product_availability = self.product_info.locator("p").filter(has_text="Availability:")
        self.product_condition = self.product_info.locator("p").filter(has_text="Condition:")
        self.product_brand = self.product_info.locator("p").filter(has_text="Brand:")


    def is_product_detail_visible(self):
        expect(self.product_info).to_be_visible()
        expect(self.product_name).to_be_visible()
        expect(self.product_name).not_to_be_empty()
        expect(self.product_category).to_be_visible()
        expect(self.product_availability).to_be_visible()
        expect(self.product_condition).to_be_visible()
        expect(self.product_brand).to_be_visible()



