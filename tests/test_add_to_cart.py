"""
Test Case ID: T001
Function ID/Name: F3 Add to cart
Tester: Tylah Jenkins (14248037)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_add_to_cart():
    # Step 1: Open browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    try:
        # Step 2: Navigate to homepage
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")
        time.sleep(3)

        # Step 3: Locate product 'HTC Touch HD'
        product_name = "HTC Touch HD"
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(2)
        product_element = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, product_name)))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_element)
        time.sleep(2)

        # Step 4: Click "Add to cart" icon
        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(@onclick, 'cart.add')]")
        for button in add_to_cart_buttons:
            try:
                parent_div = button.find_element(By.XPATH, "./ancestor::div[contains(@class, 'product-thumb')]")
                if product_name in parent_div.text:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", button)
                    break
            except:
                continue
        time.sleep(3)

        # Step 5 & 6: Validate notification (optional - may not always appear)
        time.sleep(2)

        # Step 7: Navigate to cart page directly
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=checkout/cart")
        time.sleep(3)

        # Step 8: Validate product appears in cart
        cart_product = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, product_name)))
        assert cart_product.is_displayed()

        print("TEST PASSED")

    finally:
        # Step 9: Close browser
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    test_add_to_cart()
