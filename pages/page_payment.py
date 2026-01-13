from playwright.sync_api import Page, expect

class PaymentPage():
    def __init__(self, page: Page):
        self.page = page
        self.name_on_card = self.page.locator('[name="name_on_card"]')
        self.card_number = self.page.locator('[name="card_number"]')
        self.cvc = self.page.locator('[name="cvc"]')
        self.expiration_month = self.page.locator('[name="expiry_month"]')
        self.expiration_year = self.page.locator('[name="expiry_year"]')
        self.pay_and_confirm_button = self.page.get_by_role('button', name="Pay and Confirm Order")

    def enter_payment_details(self, name_on_card, card_number, cvc, exp_month, exp_year):
        self.name_on_card.fill(name_on_card)
        self.card_number.fill(card_number)
        self.cvc.fill(cvc)
        self.expiration_month.fill(exp_month)
        self.expiration_year.fill(exp_year)

    def click_pay_and_confirm_order(self):
        self.pay_and_confirm_button.click()

    def verify_order_success_message(self):
        expect(self.page.get_by_text('Your order has been placed successfully!')).to_be_visible()