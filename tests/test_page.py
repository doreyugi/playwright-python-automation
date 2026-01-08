# Test Case 6: Contact Us Form
def test_contact_us_form(homepage):
    # 4. Click on 'Contact Us' button
    contact_us_page = homepage.header.click_contact_us_button()
    # 5. Verify 'GET IN TOUCH' is visible
    contact_us_page.verify_get_in_touch_text()
    # 6. Enter name, email, subject and message
    # 7. Upload file
    # 8. Click 'Submit' button
    # 9. Click OK button
    contact_us_page.fill_info_and_submit("banana123@gmail.com", "banana", "Complaint about banana", "The banana is not ripe enough", r'.\tests\fixtures\Complaint.txt')
    # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
    contact_us_page.verify_success_text()
    # 11. Click 'Home' button and verify that landed to home page successfully
    contact_us_page.click_home_button()
    homepage.verify_homepage()

# Test Case 7: Verify Test Cases Page
def test_test_case_page(homepage):
    # 4. Click on 'Test Cases' button
    test_case_page = homepage.header.click_test_cases_button()
    # 5. Verify user is navigated to test cases page successfully
    test_case_page.verify_test_case_page()

# def test_alert(page: Page):
#     page.on('dialog', lambda dialog: dialog.accept())
#     page.goto("https://www.tutorialspoint.com/selenium/practice/alerts.php")
#     page.locator('[onclick="myDesk()"]').click()
#     page.wait_for_timeout(5000)