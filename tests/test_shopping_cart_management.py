"""
Test Case ID: T003
Function ID/Name: F5 Shopping cart management
Tester: Tylah Jenkins (14248037)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_shopping_cart_management():
    # Step 1: Open browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    print("Step 1: Successful - Browser opened")

    try:
        # Step 2: Navigate to homepage
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")
        time.sleep(3)
        print("Step 2: Successful - Navigated to homepage")

        # Step 3: Find and add a product to cart
        product_name = "HTC Touch HD"
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(2)
        product_element = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, product_name)))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_element)
        time.sleep(2)

        # Use same approach as T001
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
        time.sleep(2)
        print("Step 3: Successful - Product added to cart")

        # Step 4: Click View Cart button from notification
        view_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'View Cart')]")))
        view_cart.click()
        time.sleep(3)
        print("Step 4: Successful - Navigated to cart page")

        # Step 5: Verify cart displays product name, image, and price
        cart_product = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, product_name)))
        assert cart_product.is_displayed()

        product_images = driver.find_elements(By.CSS_SELECTOR, ".table-responsive img")
        assert len(product_images) > 0

        # Get total price before quantity change
        import re
        time.sleep(2)
        total_price = driver.find_element(By.XPATH, "//div[@class='col-md-4']//td[text()='Total:']/following-sibling::td/strong")
        original_price = float(re.sub(r'[^\d.]', '', total_price.text))
        print("Step 5: Successful - Cart displays product details")

        # Step 6: Locate quantity input field and update from 1 to 2
        quantity_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name^='quantity']")))
        quantity_input.clear()
        quantity_input.send_keys("2")
        time.sleep(1)
        print("Step 6: Successful - Quantity updated to 2")

        # Step 7: Click update button (the one next to quantity)
        update_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]//i[@class='fas fa-sync-alt']")))
        driver.execute_script("arguments[0].click();", update_button)
        time.sleep(5)
        print("Step 7: Successful - Update button clicked")

        # Step 8: Validate quantity updated to 2 and total price doubled
        time.sleep(3)
        quantity_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name^='quantity']")))
        assert quantity_input.get_attribute("value") == "2", "Quantity not updated to 2"

        # Validate price doubled
        updated_total = driver.find_element(By.XPATH, "//div[@class='col-md-4']//td[text()='Total:']/following-sibling::td/strong")
        updated_price = float(re.sub(r'[^\d.]', '', updated_total.text))
        expected_price = original_price * 2
        assert updated_price == expected_price, f"Price did not double. Expected: ${expected_price}, Got: ${updated_price}"

        print("Step 8: Successful - Quantity and price validated")

        # Step 9: Click X icon to remove product from cart
        remove_buttons = driver.find_elements(By.CSS_SELECTOR, "button[type='button']")
        for btn in remove_buttons:
            onclick = btn.get_attribute('onclick') or ''
            if 'remove' in onclick.lower():
                driver.execute_script("arguments[0].click();", btn)
                break
        time.sleep(3)
        print("Step 9: Successful - Product removed from cart")

        # Step 10: Validate product removed and cart is empty
        try:
            empty_cart_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'shopping cart is empty') or contains(text(), 'Your cart is empty')]")))
            assert empty_cart_message is not None
        except:
            # Alternative check - product should be gone
            products = driver.find_elements(By.PARTIAL_LINK_TEXT, product_name)
            assert len(products) == 0, "Product still in cart"

        print("Step 10: Successful - Cart is empty")
        print("TEST PASSED - Cart management operations successful")

    finally:
        # Step 11: Close browser
        time.sleep(2)
        driver.quit()
        print("Step 11: Successful - Browser closed")

if __name__ == "__main__":
    test_shopping_cart_management()
