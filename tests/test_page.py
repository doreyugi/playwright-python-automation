from playwright.sync_api import expect
from playwright.sync_api import Page

# Test Case 6: Contact Us Form
def test_contact_us_form(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto('http://automationexercise.com')
    # 3. Verify that home page is visible successfully
    expect(page).to_have_title("Automation Exercise")
    # 4. Click on 'Contact Us' button
    page.get_by_role('link', name='Contact Us').click()
    # 5. Verify 'GET IN TOUCH' is visible
    expect(page.get_by_text('GET IN TOUCH')).to_be_visible()
    # 6. Enter name, email, subject and message
    page.locator('[data-qa="name"]').fill("banana")
    page.locator('[data-qa="email"]').fill("banana123@gmail.com")
    page.locator('[data-qa="subject"]').fill("Complaint about banana")
    page.locator('[data-qa="message"]').fill("The banana is not ripe enough")
    # 7. Upload file
    page.locator('[name="upload_file"]').set_input_files(r'.\tests\fixtures\Complaint.txt')
    
    # Register handling dialog before click submit
    page.on('dialog', lambda dialog: dialog.accept())
    # 8. Click 'Submit' button
    page.locator('[data-qa="submit-button"]').click()
    # 9. Click OK button
    # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
    expect(page.get_by_text('Success! Your details have been submitted successfully.')).to_be_visible()
    # 11. Click 'Home' button and verify that landed to home page successfully
    page.get_by_role('button', name='Home').click()
    expect(page).to_have_title("Automation Exercise")