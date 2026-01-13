from pages.page_header_footer import Footer
from playwright.sync_api import Page, expect
from test_data.user_data import User

class CheckoutModal():
    def __init__(self, page: Page):
        self.page = page
        self.checkout_modal = self.page.locator("#checkoutModal")
        self.register_login_button = self.checkout_modal.get_by_role('link', name="Register / Login")

    def click_register_login(self):
        self.register_login_button.click()
        from pages.page_signup_login import SignupLoginPage
        return SignupLoginPage(self.page)

class CartPage():
    def __init__(self, page: Page):
        self.page = page
        self.footer = Footer(page)
        self.checkout_modal = CheckoutModal(page)
        self.cart_table = self.page.locator('#cart_info_table')
        self.cart_items = self.cart_table.locator('tbody tr')

        self.checkout_button = self.page.get_by_text('Proceed To Checkout')

    def verify_cart_page(self):
        expect(self.page.locator("#cart_items").get_by_text("Shopping Cart")).to_be_visible()

    def verify_cart_items(self):
        expect(self.cart_table).to_be_visible()

    def verify_num_cart_items(self, num):
        expect(self.cart_items).to_have_count(num)

    def verify_cart_items_details(self, expected_products):
        count = self.cart_items.count()
        #their prices, quantity and total price
        for idx in range(count):
            row = self.cart_items.nth(idx)
            expect(row.locator('.cart_product')).to_be_visible()
            expect(row.locator('.cart_description')).to_contain_text(expected_products[idx].name)
            expect(row.locator('.cart_price')).to_have_value('Rs. ' + str(expected_products[idx].price))
            expect(row.locator('.cart_quantity')).to_have_value(str(expected_products[idx].quantity))
            price = int(row.locator('.cart_price').inner_text().removeprefix('Rs. '))
            quantity = int(row.locator('.cart_quantity').inner_text())
            total = 'Rs. ' + str(price * quantity)
            expect(row.locator('.cart_total')).to_have_text(total)

    def click_proceed_to_checkout(self):
        self.checkout_button.click()
        return CheckoutPage(self.page)

class CheckoutPage():
    def __init__(self, page: Page):
        self.page = page
        self.address_delivery = self.page.locator('#address_delivery')
        self.address_billing = self.page.locator('#address_invoice')
        self.order_review_section = self.page.locator('#cart_info')
        self.comment = self.page.locator('#ordemsg').locator('[name="message"]')

    def _verify_address(self, address_locator, user):
        expect(address_locator.locator('.address_firstname.address_lastname')).to_contain_text(user.first_name + " " + user.last_name)
        expect(address_locator.locator('.address_address1.address_address2').nth(0)).to_contain_text(user.company)
        expect(address_locator.locator('.address_address1.address_address2').nth(1)).to_contain_text(user.address1)
        expect(address_locator.locator('.address_address1.address_address2').nth(2)).to_contain_text(user.address2)
        expect(address_locator.locator('.address_city.address_state_name.address_postcode')).to_contain_text(user.city + " " + user.state + " " + user.zipcode)
        expect(address_locator.locator('.address_country_name')).to_contain_text(user.country)
        expect(address_locator.locator('.address_phone')).to_contain_text(user.mobile_number)

    def verify_address_details(self, user):
        self._verify_address(self.address_delivery, user)

    def verify_billing_address_details(self, user):
        self._verify_address(self.address_billing, user)

    def verify_order_review_section(self, products):
        expect(self.order_review_section).to_be_visible()
        cart_items = self.order_review_section.locator('tbody tr')
        count = cart_items.count()
        total_bill = 0
        for idx in range(count):
            row = cart_items.nth(idx)
            expect(row.locator('.cart_description h4')).to_contain_text(products[idx].name)
            expect(row.locator('.cart_price')).to_have_value('Rs. ' + str(products[idx].price))
            expect(row.locator('.cart_quantity')).to_have_value(str(products[idx].quantity))
            price = int(row.locator('.cart_price').inner_text().removeprefix('Rs. '))
            quantity = int(row.locator('.cart_quantity').inner_text())
            total_bill += price * quantity
            total = 'Rs. ' + str(price * quantity)
            expect(row.locator('.cart_total')).to_have_text(total)
        expect(cart_items.locator('.cart_total_price')).to_have_text('Rs. ' + str(total_bill))
    
    def fill_comment(self, comment_text):
        self.comment.fill(comment_text)

    def click_place_order(self):
        self.page.get_by_role('link', name='Place Order').click()
        from pages.page_payment import PaymentPage
        return PaymentPage(self.page)