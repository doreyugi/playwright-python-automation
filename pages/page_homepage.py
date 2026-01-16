from playwright.sync_api import Page, expect
from pages.page_product import CategoryList, ProductList, CartModal, BrandList
from pages.page_header_footer import Header, Footer
from test_data.product_data import Product

class HomePage():
    def __init__(self, page: Page):
        self.page = page
        self.footer = Footer(page)
        self.header = Header(page)
        self.product_list = ProductList(page)
        self.cart_modal = CartModal(page)
        self.category_list = CategoryList(page)
        self.brand_list = BrandList(page)
        self.recommendation_section = self.page.locator('.recommended_items')
        self.recommendation_items = self.recommendation_section.locator('.item.active .col-sm-4')
    def verify_homepage(self):
        expect(self.page).to_have_title("Automation Exercise")

    def verify_recommendation_items_text(self):
        expect(self.recommendation_section.get_by_text("RECOMMENDED ITEMS")).to_be_visible()

    def click_add_to_cart_nth_recommendation_item(self, idx):
        self.recommendation_items.nth(idx).get_by_text("Add to cart").click()
        
    def get_nth_recommended_product_info(self, idx):
        name = self.recommendation_items.nth(idx).locator('.productinfo p').inner_text().strip()
        price_text = self.recommendation_items.nth(idx).locator('.productinfo h2').inner_text().strip().replace("Rs. ", "")
        price = int(price_text)
        return Product(name, price)


