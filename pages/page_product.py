from playwright.sync_api import Page, expect
from pages.page_cart import CartPage
from test_data.product_data import Product
import re

class CartModal():
    def __init__(self, page: Page):
        self.page = page
        self.cart_modal = self.page.locator("#cartModal")

    def click_continue_shopping(self):
        self.cart_modal.get_by_role('button', name="Continue Shopping").click()

    def click_view_cart(self):
        self.cart_modal.get_by_role('link', name="View Cart").click()
        return CartPage(self.page)

class ProductList():
    def __init__(self, page: Page):
        self.page = page
        self.product_list = self.page.locator('.features_items .col-sm-4')

    def verify_product_list_title(self, title_text):
        expect(self.page.locator('.features_items').get_by_text(title_text)).to_be_visible()

    def is_product_list_visible(self):
        # expect(self.product_list).to_be_visible() 
        count = self.product_list.count()
        for i in range(count):
            expect(self.product_list.nth(i)).to_be_visible()
    
    def click_view_nth_product(self, idx):
        self.product_list.nth(idx).get_by_text("View Product").click()
        return ProductDetailPage(self.page)

    def click_add_to_cart_nth_product(self, idx):
        self.product_list.nth(idx).hover()
        self.product_list.nth(idx).locator('.product-overlay').get_by_text("Add to cart").click()

    def get_nth_product_info(self, idx):
        product = self.product_list.nth(idx).locator('.productinfo')
        name = product.locator("p").inner_text().strip()
        price_text = product.locator("h2").inner_text().strip().replace("Rs. ", "")
        price = int(price_text)
        return Product(name, price)

class CategoryList():
    def __init__(self, page: Page):
        self.page = page
        self.category_list = self.page.locator('.left-sidebar .category-products .panel')

    def is_category_list_visible(self):
        count = self.category_list.count()
        for i in range(count):
            expect(self.category_list.nth(i)).to_be_visible()

    def click_category(self, category_name):
        self.category_list.get_by_text(category_name, exact=True).click()

    def get_nth_subcategory(self, category_name, idx):
        subcategories = self.category_list.locator(f'#{category_name} .panel-body ul li')
        return subcategories.nth(idx).get_by_role('link').inner_text().strip()

    def click_nth_subcategory(self, category_name, idx):
        subcategories = self.category_list.locator(f'#{category_name} .panel-body ul li')
        subcategories.nth(idx).get_by_role('link').click()
        return ProductPage(self.page)

class BrandList():
    def __init__(self, page: Page):
        self.page = page
        self.brand_list = self.page.locator('.left-sidebar .brands_products .brands-name')

    def is_brand_list_visible(self):
        count = self.brand_list.count()
        for i in range(count):
            expect(self.brand_list.nth(i)).to_be_visible()

    def click_brand(self, brand_name):
        self.brand_list.get_by_text(brand_name).click()
        return ProductPage(self.page)

class ProductPage():
    def __init__(self, page: Page):
        self.page = page
        self.product_list = ProductList(page)
        self.brand_list = BrandList(page)
        self.category_list = CategoryList(page)
        self.cart_modal = CartModal(page)
        self.search_bar = self.page.locator('[id="search_product"]')
        self.search_button = self.page.locator('[id="submit_search"]')
        self.searched_product_text = self.page.get_by_text("Searched Product")
    
    def is_all_products_page(self):
        expect(self.page).to_have_title(re.compile(r"\ball\s+products\b", re.IGNORECASE))

    def search_product(self, keyword):
        self.search_bar.fill(keyword)
        self.search_button.click()

    def is_searched_product_visible(self):
        expect(self.searched_product_text).to_be_visible()

class ProductDetailPage():
    def __init__(self, page: Page):
        self.page = page
        self.cart_modal = CartModal(page)
        #product name, category, price, availability, condition, brand
        self.product_info = page.locator(".product-information")
        self.product_name = self.product_info.locator("h2")
        self.product_category = self.product_info.get_by_text("Category:")
        self.product_price = self.product_info.get_by_text("Rs.")
        self.product_availability = self.product_info.locator("p").filter(has_text="Availability:")
        self.product_condition = self.product_info.locator("p").filter(has_text="Condition:")
        self.product_brand = self.product_info.locator("p").filter(has_text="Brand:")
        self.product_quantity = self.product_info.locator('#quantity')
        self.review_name = page.locator('#review-form #name')
        self.review_email = page.locator('#review-form #email')
        self.review_text = page.locator('#review-form #review')
        self.submit_review_button = page.locator('#button-review')

    def is_product_detail_visible(self):
        expect(self.product_info).to_be_visible()
        expect(self.product_name).to_be_visible()
        expect(self.product_name).not_to_be_empty()
        expect(self.product_category).to_be_visible()
        expect(self.product_availability).to_be_visible()
        expect(self.product_condition).to_be_visible()
        expect(self.product_brand).to_be_visible()

    def is_write_your_review_visible(self):
        expect(self.page.get_by_text("Write Your Review")).to_be_visible()

    def increase_quantity(self, num):
        self.product_quantity.fill(str(num))

    def click_add_to_cart(self):
        self.product_info.get_by_role('button', name='Add to cart').click()

    def fill_review_form(self, name, email, review):
        self.review_name.fill(name)
        self.review_email.fill(email)
        self.review_text.fill(review)

    def click_submit_review(self):
        self.submit_review_button.click()

    def verify_review_success_message(self):
        expect(self.page.get_by_text("Thank you for your review.")).to_be_visible()

    def get_product_info(self):
        name = self.product_name.inner_text().strip()
        price_text = self.product_price.inner_text().strip().removeprefix('Rs. ')
        price = int(price_text)
        quantity = int(self.product_quantity.input_value())
        return Product(name, price, quantity)