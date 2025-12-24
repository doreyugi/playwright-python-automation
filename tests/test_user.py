from playwright.sync_api import expect
from playwright.sync_api import Page
import re

username = "apple"
user_email = "applebottomjeans@gmail.com"
user_password = "applebottomjeans"

# Test Case 1: Register User
def test_register_user(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto("http://automationexercise.com")
    # 3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")
    # 4. Click on 'Signup / Login' button
    page.get_by_role('link', name="Signup / Login").click()
    # 5. Verify 'New User Signup!' is visible
    expect(page.get_by_text('New User Signup!')).to_be_visible()
    # 6. Enter name and email address
    page.locator('[data-qa="signup-name"]').fill(username)
    page.locator('[data-qa="signup-email"]').fill(user_email)
    # 7. Click 'Signup' button
    page.get_by_role('button', name="Signup").click()
    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    expect(page.get_by_text('ENTER ACCOUNT INFORMATION')).to_be_visible()
    # 9. Fill details: Title, Name, Email, Password, Date of birth
    page.get_by_role('radio', name="Mr.").click()
    page.locator('[data-qa="password"]').fill(user_password)
    page.locator("#days").select_option("5")
    page.locator("#months").select_option("July")
    page.locator("#years").select_option("1993")
    # 10. Select checkbox 'Sign up for our newsletter!'
    page.get_by_role("checkbox", name='Sign up for our newsletter!').check()
    # 11. Select checkbox 'Receive special offers from our partners!'
    page.get_by_role("checkbox", name='Receive special offers from our partners!').check()
    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    page.locator("#first_name").fill("abc")
    page.locator("#last_name").fill("def")
    page.locator("#company").fill("ABC Co.")
    page.locator("#address1").fill("362 Celestia")
    page.locator("#address2").fill("462 Heavenly Celestia")
    page.locator("#country").select_option("Singapore")
    page.locator("#state").fill("New York")
    page.locator("#city").fill("New York")
    page.locator("#zipcode").fill("70000")
    page.locator("#mobile_number").fill("70000")
    # 13. Click 'Create Account button'
    page.get_by_role('button', name='Create Account').click()
    # 14. Verify that 'ACCOUNT CREATED!' is visible
    expect(page.get_by_text('ACCOUNT CREATED!')).to_be_visible()
    # 15. Click 'Continue' button
    page.get_by_role('link', name='Continue').click()
    # 16. Verify that 'Logged in as username' is visible
    expect(page.get_by_text('Logged in as apple')).to_be_visible()

# Test Case 2: Login User with correct email and password
def test_login_user_correct(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")
    # 4. Click on 'Signup / Login' button
    page.get_by_role('link', name='Signup / Login').click()
    # 5. Verify 'Login to your account' is visible
    expect(page.get_by_text('Login to your account')).to_be_visible()
    # 6. Enter correct email address and password
    page.locator('[data-qa="login-email"]').fill(user_email)
    page.locator('[data-qa="login-password"]').fill(user_password)
    # 7. Click 'login' button
    page.get_by_role("button", name="Login").click()
    # 8. Verify that 'Logged in as username' is visible
    expect(page.get_by_text('Logged in as apple')).to_be_visible()

# Test Case 3: Login User with incorrect email and password
def test_login_user_incorrect(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")
    # 4. Click on 'Signup / Login' button
    page.get_by_role('link', name='Signup / Login').click()
    # 5. Verify 'Login to your account' is visible
    expect(page.get_by_text('Login to your account')).to_be_visible()
    # 6. Enter incorrect email address and password
    page.locator('[data-qa="login-email"]').fill(user_email)
    page.locator('[data-qa="login-password"]').fill(user_password+"123")
    # 7. Click 'login' button
    page.get_by_role("button", name="Login").click()
    # 8. Verify error 'Your email or password is incorrect!' is visible
    expect(page.get_by_text('Your email or password is incorrect!')).to_be_visible()

# Test Case 4: Logout User
def test_logout_user(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")
    # 4. Click on 'Signup / Login' button
    page.get_by_role('link', name='Signup / Login').click()
    # 5. Verify 'Login to your account' is visible
    expect(page.get_by_text('Login to your account')).to_be_visible()
    # 6. Enter correct email address and password
    page.locator('[data-qa="login-email"]').fill(user_email)
    page.locator('[data-qa="login-password"]').fill(user_password)
    # 7. Click 'login' button
    page.get_by_role("button", name="Login").click()
    # 8. Verify that 'Logged in as username' is visible
    expect(page.get_by_text('Logged in as apple')).to_be_visible()
    # 9. Click 'Logout' button
    page.get_by_role('link', name='Logout').click()
    #10. Verify that user is navigated to login page
    expect(page).to_have_title(re.compile("Signup / Login", re.IGNORECASE))

# Test Case 5: Register User with existing email
def test_register_existing_user(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto("http://automationexercise.com")
    # 3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")
    # 4. Click on 'Signup / Login' button
    page.get_by_role('link', name="Signup / Login").click()
    # 5. Verify 'New User Signup!' is visible
    expect(page.get_by_text('New User Signup!')).to_be_visible()
    # 6. Enter name and already registered email address
    page.locator('[data-qa="signup-name"]').fill(username)
    page.locator('[data-qa="signup-email"]').fill(user_email)
    # 7. Click 'Signup' button
    page.get_by_role('button', name='Signup').click()
    # 8. Verify error 'Email Address already exist!' is visible
    expect(page.get_by_text('Email Address already exist!')).to_be_visible()

# Test Case ???: Delete user
def test_delete_user(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")
    # 4. Click on 'Signup / Login' button
    page.get_by_role('link', name='Signup / Login').click()
    # 5. Verify 'Login to your account' is visible
    expect(page.get_by_text('Login to your account')).to_be_visible()
    # 6. Enter correct email address and password
    page.locator('[data-qa="login-email"]').fill(user_email)
    page.locator('[data-qa="login-password"]').fill(user_password)
    # 7. Click 'login' button
    page.get_by_role("button", name="Login").click()
    # 8. Verify that 'Logged in as username' is visible
    expect(page.get_by_text('Logged in as apple')).to_be_visible()
    # 9. Click 'Delete Account' button
    page.get_by_role('link', name='Delete Account').click()
    # 10. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    expect(page.get_by_text('ACCOUNT DELETED!')).to_be_visible()
    page.get_by_role('link', name='Continue').click()