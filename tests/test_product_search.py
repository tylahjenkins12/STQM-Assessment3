"""
Test Case ID: T002
Function ID/Name: F4 Product search
Tester: Tylah Jenkins (14248037)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_product_search():
    # Step 1: Open browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    try:
        # Step 2: Navigate to homepage
        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")
        time.sleep(3)

        # Step 3: Locate and click the search bar
        search_bar = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
        search_bar.click()
        time.sleep(1)

        # Step 4: Type "iPhone" in the search bar
        search_term = "iPhone"
        search_bar.clear()
        search_bar.send_keys(search_term)
        time.sleep(1)

        # Step 5: Click the search button (use Keys.ENTER instead)
        from selenium.webdriver.common.keys import Keys
        search_bar.send_keys(Keys.RETURN)
        time.sleep(3)

        # Step 6: Wait for search results page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-thumb")))
        time.sleep(2)

        # Step 7: Validate search results display products matching the search term
        search_results = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
        assert len(search_results) > 0, "No search results found"

        # Step 8: Validate each product has name, image, and price
        for product in search_results:
            # Validate product name exists and contains search term
            product_name = product.find_element(By.CSS_SELECTOR, "h4 a")
            assert product_name.is_displayed()
            assert search_term.lower() in product_name.text.lower(), f"Product '{product_name.text}' does not match search term"

            # Validate product image exists
            product_image = product.find_element(By.CSS_SELECTOR, "img")
            assert product_image.is_displayed()

            # Validate product price exists
            product_price = product.find_element(By.CSS_SELECTOR, ".price")
            assert product_price.is_displayed()

        print(f"TEST PASSED - Found {len(search_results)} products matching '{search_term}'")

    finally:
        # Step 9: Close browser
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    test_product_search()
