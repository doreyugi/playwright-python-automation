from playwright.sync_api import Page, expect
import re

class SignupLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.signup_name = page.locator('[data-qa="signup-name"]')
        self.signup_email = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.get_by_role('button', name="Signup")

        self.signup_gender = page.get_by_role('radio', name="Mr.")
        self.signup_password = page.locator('[data-qa="password"]')
        self.signup_DOB_days = page.locator("#days")
        self.signup_DOB_months = page.locator("#months")
        self.signup_DOB_years = page.locator("#years")

        self.signup_newsletter_checkbox = page.get_by_role("checkbox", name='Sign up for our newsletter!')
        self.signup_receive_special_offers_checkbox = page.get_by_role("checkbox", name='Receive special offers from our partners!')
        
        self.signup_first_name = page.locator("#first_name")
        self.signup_last_name = page.locator("#last_name")
        self.signup_company = page.locator("#company")
        self.signup_address1 = page.locator("#address1")
        self.signup_address2 = page.locator("#address2")
        self.signup_country = page.locator("#country")
        self.signup_state = page.locator("#state")
        self.signup_city = page.locator("#city")
        self.signup_zipcode = page.locator("#zipcode")
        self.signup_mobile_number = page.locator("#mobile_number")
        self.signup_state = page.locator("#state")
        self.signup_city = page.locator("#city")
        self.signup_zipcode = page.locator("#zipcode")
        self.signup_mobile_number = page.locator("#mobile_number")
      
        self.signup_create_account_button = page.get_by_role('button', name='Create Account')

        self.signup_success_continue_button = page.get_by_role('link', name='Continue')

        self.login_email = page.locator('[data-qa="login-email"]')
        self.login_password = page.locator('[data-qa="login-password"]')
        self.login_button = page.get_by_role("button", name="Login")

    def verify_signup_login_page(self):
        expect(self.page).to_have_title(re.compile("Signup / Login", re.IGNORECASE))

    def is_new_user_signup_visible(self):
        expect(self.page.get_by_text('New User Signup!')).to_be_visible()

    def signup(self, username, user_email):
        self.signup_name.fill(username)
        self.signup_email.fill(user_email)
        self.signup_button.click()

    def login(self, user_email, user_password):
        self.login_email.fill(user_email)
        self.login_password.fill(user_password)
        self.login_button.click()

    def verify_login_error_message(self):
        expect(self.page.get_by_text('Your email or password is incorrect!')).to_be_visible()

    def verify_signup_email_exists_message(self):
        expect(self.page.get_by_text('Email Address already exist!')).to_be_visible()

    def is_enter_account_information_visible(self):
        expect(self.page.get_by_text('ENTER ACCOUNT INFORMATION')).to_be_visible()

    def verify_signup_success_message(self):
        expect(self.page.get_by_text('ACCOUNT CREATED!')).to_be_visible()

    def click_continue_button(self):
        self.signup_success_continue_button.click()

    def is_login_to_your_account_visible(self):
        expect(self.page.get_by_text('Login to your account')).to_be_visible()

    def fill_signup_form(self, password, day, month, year, first_name, last_name, company, address1, address2, country, state, city, zipcode, mobile_number):
        self.signup_gender.click()
        self.signup_password.fill(password)
        self.signup_DOB_days.select_option(day)
        self.signup_DOB_months.select_option(month)
        self.signup_DOB_years.select_option(year)
        # Select checkbox 'Sign up for our newsletter!'
        self.signup_newsletter_checkbox.check()
        # Select checkbox 'Receive special offers from our partners!'
        self.signup_receive_special_offers_checkbox.check()
        # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
        self.signup_first_name.fill(first_name)
        self.signup_last_name.fill(last_name)
        self.signup_company.fill(company)
        self.signup_address1.fill(address1)
        self.signup_address2.fill(address2)
        self.signup_country.select_option(country)
        self.signup_state.fill(state)
        self.signup_city.fill(city)
        self.signup_zipcode.fill(zipcode)
        self.signup_mobile_number.fill(mobile_number)
        # Click 'Create Account button'
        self.signup_create_account_button.click()

class DeleteAccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.delete_account_continue_button = page.get_by_role('link', name='Continue')

    def verify_delete_account_page(self):
        expect(self.page.get_by_text('ACCOUNT DELETED!')).to_be_visible()

    def click_continue_button(self):
        self.delete_account_continue_button.click()