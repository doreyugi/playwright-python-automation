from playwright.sync_api import expect
from playwright.sync_api import Page

username = "apple"
user_email = "applebottomjeans@gmail.com"
user_password = "applebottomjeans"
DOB_day = "5"
DOB_month = "July"
DOB_year = "1993"
first_name = "abc"
last_name = "def"
company = "ABC Co."
address1 = "362 Celestia"
address2 = "462 Heavenly Celestia"
country = "Singapore"
state = "New York"
city = "New York"
zipcode = "70000"
mobile_number = "70000"

# Test Case 1: Register User
def test_register_user(homepage):
    # 4. Click on 'Signup / Login' button
    signup_login_page = homepage.header.click_signup_login_button()
    # 5. Verify 'New User Signup!' is visible
    signup_login_page.is_new_user_signup_visible()
    # 6. Enter name and email address
    # 7. Click 'Signup' button
    signup_login_page.signup(username, user_email)
    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    signup_login_page.is_enter_account_information_visible()
    # 9. Fill details: Title, Name, Email, Password, Date of birth
    # 10. Select checkbox 'Sign up for our newsletter!'
    # 11. Select checkbox 'Receive special offers from our partners!'
    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    # 13. Click 'Create Account button'
    signup_login_page.fill_signup_form(user_password, DOB_day, DOB_month, DOB_year, first_name, last_name, company, address1, address2, country, state, city, zipcode, mobile_number)
    # 14. Verify that 'ACCOUNT CREATED!' is visible
    signup_login_page.verify_signup_success_message()
    # 15. Click 'Continue' button
    signup_login_page.click_continue_button()
    # 16. Verify that 'Logged in as username' is visible
    homepage.header.verify_logged_in_as_username(username)

# Test Case 2: Login User with correct email and password
def test_login_user_correct(homepage):
    # 4. Click on 'Signup / Login' button
    signup_login_page = homepage.header.click_signup_login_button()
    # 5. Verify 'Login to your account' is visible
    signup_login_page.is_login_to_your_account_visible()
    # 6. Enter correct email address and password
    # 7. Click 'login' button
    signup_login_page.login(user_email, user_password)
    # 8. Verify that 'Logged in as username' is visible
    homepage.header.verify_logged_in_as_username(username)

# Test Case 3: Login User with incorrect email and password
def test_login_user_incorrect(homepage):
    # 4. Click on 'Signup / Login' button
    signup_login_page = homepage.header.click_signup_login_button()
    # 5. Verify 'Login to your account' is visible
    signup_login_page.is_login_to_your_account_visible()
    # 6. Enter incorrect email address and password
    # 7. Click 'login' button
    signup_login_page.login(user_email, user_password+"123")
    # 8. Verify error 'Your email or password is incorrect!' is visible
    signup_login_page.verify_login_error_message()

# Test Case 4: Logout User
def test_logout_user(homepage):
    # 4. Click on 'Signup / Login' button
    signup_login_page = homepage.header.click_signup_login_button()
    # 5. Verify 'Login to your account' is visible
    signup_login_page.is_login_to_your_account_visible()
    # 6. Enter correct email address and password
    # 7. Click 'login' button
    signup_login_page.login(user_email, user_password)
    # 8. Verify that 'Logged in as username' is visible
    homepage.header.verify_logged_in_as_username(username)
    # 9. Click 'Logout' button
    signup_login_page = homepage.header.click_logout_button()
    #10. Verify that user is navigated to login page
    signup_login_page.verify_signup_login_page()

# Test Case 5: Register User with existing email
def test_register_existing_user(homepage):
    # 4. Click on 'Signup / Login' button
    signup_login_page = homepage.header.click_signup_login_button()
    # 5. Verify 'New User Signup!' is visible
    signup_login_page.is_new_user_signup_visible()
    # 6. Enter name and already registered email address
    # 7. Click 'Signup' button
    signup_login_page.signup(username, user_email)
    # 8. Verify error 'Email Address already exist!' is visible
    signup_login_page.verify_signup_email_exists_message()

# Test Case ???: Delete user
def test_delete_user(homepage):
    # 4. Click on 'Signup / Login' button
    signup_login_page = homepage.header.click_signup_login_button()
    # 5. Verify 'Login to your account' is visible
    signup_login_page.is_login_to_your_account_visible()
    # 6. Enter correct email address and password
    # 7. Click 'login' button
    signup_login_page.login(user_email, user_password)
    # 8. Verify that 'Logged in as username' is visible
    homepage.header.verify_logged_in_as_username(username)
    # 9. Click 'Delete Account' button
    delete_account_page = homepage.header.click_delete_account_button()
    # 10. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    delete_account_page.verify_delete_account_page()
    delete_account_page.click_continue_button()