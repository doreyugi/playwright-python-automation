# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def test_register_user(driver):
#     driver.get("http://automationexercise.com")

#     # Wait till the homepage load
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "col-sm-12" )))
#     # driver.find_element(By.LINK_TEXT, "Signup / Login").click()
#     driver.find_element(By.CSS_SELECTOR, 'a[href="login"]').click()
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "signup-form")))

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from playwright.sync_api import Page

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
    page.locator('[data-qa="signup-name"]').fill("apple")
    page.locator('[data-qa="signup-email"]').fill("applebottomjeans@gmail.com")
    # 7. Click 'Signup' button
    page.get_by_role('button', name="Signup").click()
    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    expect(page.get_by_text('ENTER ACCOUNT INFORMATION')).to_be_visible()
    # 9. Fill details: Title, Name, Email, Password, Date of birth
    page.get_by_role('radio', name="Mr.").click()
    page.locator('[data-qa="password"]').fill("applebottomjeans")
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
    # 17. Click 'Delete Account' button
    page.get_by_role('link', name='Delete Account').click()
    # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    expect(page.get_by_text('ACCOUNT DELETED!')).to_be_visible()
    page.get_by_role('link', name='Continue').click()

def test_login_user_correct(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")
    # 4. Click on 'Signup / Login' button
    page.get_by_role('link', name='Signup / Login')
    # 5. Verify 'Login to your account' is visible
    expect(page.get_by_text('Login to your account')).to_be_visible()
    # 6. Enter correct email address and password
    page.locator('[data-qa="login-email"]').fill("banana@gmail.com")
    page.locator('[data-qa="login-password"]').fill("banana")
    # 7. Click 'login' button
    page.get_by_role("button", name="Login").click()
    # 8. Verify that 'Logged in as username' is visible
    expect(page.get_by_text('Logged in as apple')).to_be_visible()
    # 9. Click 'Delete Account' button
    # 10. Verify that 'ACCOUNT DELETED!' is visible