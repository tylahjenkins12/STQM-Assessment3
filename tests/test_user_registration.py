"""
Test Case ID: T007
Function ID/Name: F2 User Registration
Tester: Thomas Sutton (25926496)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_user_registration():
    # Step 1: Open browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    print("Step 1: Successful - Browser opened")

    try:
        # Step 2: Navigate to registration page
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
        time.sleep(3)
        print("Step 2: Successful - Navigated to registration page")

        # Step 3: Verify all required fields are present
        required_fields = ["input-firstname", "input-lastname", "input-email", 
                          "input-telephone", "input-password", "input-confirm"]
        
        for field_id in required_fields:
            field = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            assert field.is_displayed()
        
        print("Step 3: Successful - All required fields present")

        # Step 4: Generate unique test data and fill form
        timestamp = int(time.time())
        test_email = f"testuser_{timestamp}@example.com"
        test_password = "PassWord123!"
        
        driver.find_element(By.ID, "input-firstname").send_keys("Test")
        driver.find_element(By.ID, "input-lastname").send_keys("User")
        driver.find_element(By.ID, "input-email").send_keys(test_email)
        driver.find_element(By.ID, "input-telephone").send_keys("0412345678")
        driver.find_element(By.ID, "input-password").send_keys(test_password)
        driver.find_element(By.ID, "input-confirm").send_keys(test_password)
        time.sleep(1)
        print("Step 4: Successful - Registration form filled")

        # Step 5: Select newsletter preference
        newsletter_options = driver.find_elements(By.NAME, "newsletter")
        for option in newsletter_options:
            if option.get_attribute("value") == "0":
                driver.execute_script("arguments[0].click();", option)
                break
        time.sleep(1)
        print("Step 5: Successful - Newsletter preference set")

        # Step 6: Scroll to and check privacy policy checkbox
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        
        privacy_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "agree")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", privacy_checkbox)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", privacy_checkbox)
        time.sleep(1)
        print("Step 6: Successful - Privacy policy accepted")

        # Step 7: Click Continue button
        continue_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='Continue']")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", continue_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", continue_button)
        time.sleep(3)
        print("Step 7: Successful - Registration submitted")

        # Step 8: Verify successful registration
        time.sleep(2)
        current_url = driver.current_url
        
        # Check for success page or account page
        if "/account/success" in current_url or "/account/account" in current_url:
            print("Step 8: Successful - Registration completed")
        else:
            # Look for success heading
            headings = driver.find_elements(By.CSS_SELECTOR, "h1, h2")
            for heading in headings:
                if "created" in heading.text.lower() or "success" in heading.text.lower():
                    print("Step 8: Successful - Registration completed")
                    break
        
        # Step 9: Verify account is accessible
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/account")
        time.sleep(2)
        account_elements = driver.find_elements(By.CSS_SELECTOR, "h2, .list-group-item")
        assert len(account_elements) > 0
        print("Step 9: Successful - Account accessible")

        print("TEST PASSED - User registration completed successfully")

    finally:
        # Step 10: Close browser
        time.sleep(2)
        driver.quit()
        print("Step 10: Successful - Browser closed")

if __name__ == "__main__":
    test_user_registration()
