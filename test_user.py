from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register_user(driver):
    driver.get("http://automationexercise.com")

    # Wait till the homepage load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "col-sm-12" )))
    # driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    driver.find_element(By.CSS_SELECTOR, 'a[href="login"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "signup-form")))
