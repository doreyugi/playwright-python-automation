# Playwright Automation Testing (Python)

## Overview

This is a **personal QA automation project** built to practice **UI end-to-end testing** using **Playwright with Python**.

The project automates common user workflows for a sample e-commerce website:  
https://www.automationexercise.com/

It focuses on writing maintainable tests, applying the **Page Object Model (POM)**, and validating critical business flows such as authentication, product browsing, cart, and checkout.

---

## Tech Stack

- **Language:** Python  
- **Automation Tool:** Playwright  
- **Test Framework:** PyTest  
- **Dependency Management:** pip  
- **Browser:** Chromium / Chrome  

---

## Project Structure

```text
pages/          # Page Object Model (POM) classes
tests/          # Test cases grouped by feature
test_data/      # Test data (users, products)
reports/        # HTML test reports
conftest.py     # PyTest fixtures and setup
pytest.ini      # PyTest configuration
requirements.txt
README.md
```

## Automated Test Coverage

The project automates test scenarios **provided by the application** and focuses on implementing them as maintainable and reusable UI automation tests.

Covered scenarios include:

- User Registration & Authentication (valid / invalid cases)
- Product listing, product detail, and search
- Add to cart, quantity validation, and cart management
- Checkout flows (register before / during checkout, login checkout)
- Subscription verification (home & cart)
- Category and brand filtering
- Product reviews and recommended items
- Address validation and invoice download
- UI behavior (scroll up with / without arrow)

## How to Run the Tests

### 1. Install dependencies
Make sure Python is installed, then install required packages:

```bash
pip install -r requirements.txt
```

### 2. Run all tests
```bash
pytest
```

### 3. Run a specific test file (optional)
```bash
pytest tests/test_user.py
```

## Notes

- This is an **ongoing personal project** focused on learning and practicing QA automation.
- Test scenarios are **based on test cases provided by the sample application**, with emphasis on automation implementation and framework design.
- The project applies **Page Object Model (POM)** to improve maintainability and readability.
- Debug artifacts and local configuration files are excluded from version control.
- All test data used in this project (e.g. user accounts, emails, addresses) is **dummy data created for testing purposes only**.
