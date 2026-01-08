from playwright.sync_api import Page, expect

class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.form_name = self.page.locator('[data-qa="name"]')
        self.form_email = self.page.locator('[data-qa="email"]')
        self.form_subject = self.page.locator('[data-qa="subject"]')
        self.form_message = self.page.locator('[data-qa="message"]')
        self.form_upload_file = self.page.locator('[name="upload_file"]')
        self.form_submit_button = page.locator('[data-qa="submit-button"]')

    def verify_get_in_touch_text(self):
        expect(self.page.get_by_text('GET IN TOUCH')).to_be_visible()

    def fill_info_and_submit(self, email, name = None, subject = None, message = None, filePath = None):
        # Register handling dialog before click submit
        self.page.on('dialog', lambda dialog: dialog.accept())
        self.form_email.fill(email)
        if name is not None: 
            self.form_name.fill(name)
        if subject is not None: 
            self.form_subject.fill(subject)
        if message is not None: 
            self.form_message.fill(message)
        if filePath is not None: 
            self.form_upload_file.set_input_files(filePath)
        self.form_submit_button.click(delay=500)

    def verify_success_text(self):
        expect(self.page.locator("#contact-page")).to_contain_text("Success! Your details have been submitted successfully.")

    def click_home_button(self):
        self.page.locator("#contact-page").get_by_role('link', name='Home').click()