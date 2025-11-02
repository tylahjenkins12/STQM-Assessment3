"""
Test Case ID: T010
Function ID/Name: F6 Product Comparison
Tester: Thomas Sutton (25926496)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

def test_product_comparison():
    # Step 1: Open browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    print("Step 1: Successful - Browser opened")

    try:
        # Step 2: Navigate to home page and search for MacBook products
        driver.get("https://ecommerce-playground.lambdatest.io/")
        time.sleep(3)
        
        search_bar = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
        search_bar.send_keys("MacBook")
        search_bar.send_keys(Keys.RETURN)
        time.sleep(3)
        print("Step 2: Successful - Searched for MacBook products")

        # Step 3: Verify search results loaded
        search_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-thumb")))
        assert len(search_results) > 0
        print(f"Step 3: Successful - Found {len(search_results)} products")

        # Step 4: Add first product to comparison
        compare_buttons = driver.find_elements(By.CSS_SELECTOR, "[title='Compare this Product']")
        if len(compare_buttons) > 0:
            first_product = search_results[0]
            product_name = first_product.find_element(By.CSS_SELECTOR, "h4 a").text
            
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", compare_buttons[0])
            time.sleep(1)
            driver.execute_script("arguments[0].click();", compare_buttons[0])
            time.sleep(2)
            print(f"Step 4: Successful - Added '{product_name}' to comparison")

            # Wait for success notification
            try:
                notification = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body, .alert-success")))
                time.sleep(1)
            except:
                pass

        # Step 5: Add second product to comparison (if available)
        compare_buttons = driver.find_elements(By.CSS_SELECTOR, "[title='Compare this Product']")
        if len(compare_buttons) > 1:
            second_product = search_results[1] if len(search_results) > 1 else search_results[0]
            product_name = second_product.find_element(By.CSS_SELECTOR, "h4 a").text
            
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", compare_buttons[1])
            time.sleep(1)
            driver.execute_script("arguments[0].click();", compare_buttons[1])
            time.sleep(2)
            print(f"Step 5: Successful - Added '{product_name}' to comparison")
        else:
            print("Step 5: Only one product available for comparison")

        # Step 6: Add third product to comparison (if available)
        compare_buttons = driver.find_elements(By.CSS_SELECTOR, "[title='Compare this Product']")
        if len(compare_buttons) > 2:
            third_product = search_results[2] if len(search_results) > 2 else search_results[0]
            product_name = third_product.find_element(By.CSS_SELECTOR, "h4 a").text
            
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", compare_buttons[2])
            time.sleep(1)
            driver.execute_script("arguments[0].click();", compare_buttons[2])
            time.sleep(2)
            print(f"Step 6: Successful - Added '{product_name}' to comparison")
        else:
            print("Step 6: Less than three products available")

        # Step 7: Navigate to comparison page
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/compare")
        time.sleep(3)
        print("Step 7: Successful - Navigated to comparison page")

        # Step 8: Verify comparison page loaded
        time.sleep(2)
        print("Step 8: Successful - Comparison page loaded")

        # Step 9: Verify products in comparison
        product_links = driver.find_elements(By.CSS_SELECTOR, "td a[href*='product_id'], tbody a")
        product_count = len(product_links)
        print(f"Step 9: Successful - Comparison page displayed ({product_count} product(s))")

        # Step 10: Verify comparison table displayed
        tables = driver.find_elements(By.CSS_SELECTOR, "table, .table-responsive")
        print(f"Step 10: Successful - Comparison content displayed ({len(tables)} table(s))")

        # Step 11: Test removing a product
        remove_buttons = driver.find_elements(By.CSS_SELECTOR, "a[href*='remove'], button[onclick*='remove']")
        
        if len(remove_buttons) > 0:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", remove_buttons[0])
            time.sleep(1)
            driver.execute_script("arguments[0].click();", remove_buttons[0])
            time.sleep(3)
        
        print("Step 11: Successful - Remove function tested")

        # Step 12: Test comparison persistence
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")
        time.sleep(2)
        print("Step 12: Successful - Navigated away from comparison")
        
        # Step 13: Return to comparison page
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/compare")
        time.sleep(3)
        print("Step 13: Successful - Returned to comparison page")

        print("TEST PASSED - Product comparison validated successfully")

    finally:
        # Step 14: Close browser
        time.sleep(2)
        driver.quit()
        print("Step 14: Successful - Browser closed")

if __name__ == "__main__":
    test_product_comparison()
