import pytest
from pages.page_homepage import HomePage

BASE_URL = "http://automationexercise.com"

@pytest.fixture
def homepage(page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    page.goto(BASE_URL)
    # 3. Verify that home page is visible successfully
    homepage = HomePage(page)
    homepage.verify_homepage()
    return homepage

# Need some kind of adblock to prevent flaky tests?
