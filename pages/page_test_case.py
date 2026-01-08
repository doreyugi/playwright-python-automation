from playwright.sync_api import Page, expect
import re

class TestCasePage:
   def __init__(self, page: Page):
        self.page = page

   def verify_test_case_page(self):
      expect(self.page).to_have_title(re.compile(r"\btest\s+cases\b", re.IGNORECASE))