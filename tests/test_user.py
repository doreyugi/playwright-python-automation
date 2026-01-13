from test_data.user_data import new_user

# Test Case 1: Register User
def test_register_user(homepage):
    # 4. Click on 'Signup / Login' button
    signup_login_page = homepage.header.click_signup_login_button()
    # 5. Verify 'New User Signup!' is visible
    signup_login_page.is_new_user_signup_visible()
    # 6. Enter name and email address
    # 7. Click 'Signup' button
    signup_login_page.signup(new_user.username, new_user.email)
    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    signup_login_page.is_enter_account_information_visible()
    # 9. Fill details: Title, Name, Email, Password, Date of birth
    # 10. Select checkbox 'Sign up for our newsletter!'
    # 11. Select checkbox 'Receive special offers from our partners!'
    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    # 13. Click 'Create Account button'
    signup_login_page.fill_signup_form(new_user.password, new_user.DOB_day, new_user.DOB_month, new_user.DOB_year, new_user.first_name, new_user.last_name, new_user.company, new_user.address1, new_user.address2, new_user.country, new_user.state, new_user.city, new_user.zipcode, new_user.mobile_number)
    # 14. Verify that 'ACCOUNT CREATED!' is visible
    signup_login_page.verify_signup_success_message()
    # 15. Click 'Continue' button
    signup_login_page.click_continue_button()
    # 16. Verify that 'Logged in as username' is visible
    homepage.header.verify_logged_in_as_username(new_user.username)

# Test Case 2: Login User with correct email and password
def test_login_user_correct(homepage):
    # 4. Click on 'Signup / Login' button
    signup_login_page = homepage.header.click_signup_login_button()
    # 5. Verify 'Login to your account' is visible
    signup_login_page.is_login_to_your_account_visible()
    # 6. Enter correct email address and password
    # 7. Click 'login' button
    signup_login_page.login(new_user.email, new_user.password)
    # 8. Verify that 'Logged in as username' is visible
    homepage.header.verify_logged_in_as_username(new_user.username)

# Test Case 3: Login User with incorrect email and password
def test_login_user_incorrect(homepage):
    # 4. Click on 'Signup / Login' button
    signup_login_page = homepage.header.click_signup_login_button()
    # 5. Verify 'Login to your account' is visible
    signup_login_page.is_login_to_your_account_visible()
    # 6. Enter incorrect email address and password
    # 7. Click 'login' button
    signup_login_page.login(new_user.email, new_user.password+"123")
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
    signup_login_page.login(new_user.email, new_user.password)
    # 8. Verify that 'Logged in as username' is visible
    homepage.header.verify_logged_in_as_username(new_user.username)
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
    signup_login_page.signup(new_user.username, new_user.email)
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
    signup_login_page.login(new_user.email, new_user.password)
    # 8. Verify that 'Logged in as username' is visible
    homepage.header.verify_logged_in_as_username(new_user.username)
    # 9. Click 'Delete Account' button
    delete_account_page = homepage.header.click_delete_account_button()
    # 10. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    delete_account_page.verify_delete_account_page()
    delete_account_page.click_continue_button()