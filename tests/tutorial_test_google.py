from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from playwright.sync_api import Page
import pytest
import re

def test_title_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://google.com")
        page.wait_for_load_state('load')
        title = page.title()
        assert "Google" in title, f"Expected 'Google' in title, but got {title}"
        browser.close()

#@pytest.mark.headed #mark to run separately
def test_google_search_playwright(page: Page):
    page.goto("https://google.com/ncr") #no country redirect
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("No popup")
    page.get_by_role("combobox",name="Search").fill("Playwright")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))

def test_google_search_python(page: Page):
    page.goto("https://google.com/ncr") #no country redirect
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("No popup")
    page.get_by_role("combobox",name="Search").fill("Python for beginner")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Python", re.IGNORECASE))