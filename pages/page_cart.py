from pages.page_header_footer import Footer
from playwright.sync_api import Page, expect

class CartPage():
    def __init__(self, page: Page):
        self.page = page
        self.footer = Footer(page)
        self.cart_table = self.page.locator('#cart_info_table')
        self.cart_items = self.cart_table.locator('tbody tr')

    def verify_cart_page(self):
        expect(self.page.locator("#cart_items").get_by_text("Shopping Cart")).to_be_visible()

    def verify_cart_items(self):
        expect(self.cart_table).to_be_visible()

    def verify_num_cart_items(self, num):
        expect(self.cart_items).to_have_count(num)

    def verify_cart_items_detail(self):
        count = self.cart_items.count()
        #their prices, quantity and total price
        for idx in range(count):
            row = self.cart_items.nth(idx)
            expect(row.locator('.cart_product')).to_be_visible()
            expect(row.locator('.cart_description')).to_be_visible()
            expect(row.locator('.cart_price')).to_be_visible()
            expect(row.locator('.cart_quantity')).to_be_visible()
            expect(row.locator('.cart_total')).to_be_visible()
            price = int(row.locator('.cart_price').inner_text().removeprefix('Rs. '))
            quantity = int(row.locator('.cart_quantity').inner_text())
            total = 'Rs. ' + str(price * quantity)
            expect(row.locator('.cart_total')).to_have_text(total)

    def verify_nth_cart_item_quantity(self, idx, quantity):
        row = self.cart_items.nth(idx)
        expect(row.locator('.cart_quantity')).to_have_text(str(quantity))