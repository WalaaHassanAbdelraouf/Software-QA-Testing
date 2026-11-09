from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Test Suite: Google Search Bar


class TestGoogleSearch:

    # test case 1: checking if the search returns results
    def test_search_returns_results(self, driver):

        # 1. Open Google
        driver.get("https://www.google.com")

        # 2. Find the search box by its name attribute
        search_box = driver.find_element(By.NAME, "q")

        # 3. Type the search query
        search_box.send_keys("Selenium automation testing")
        
        time.sleep(5)
        
        # 4. Press Enter
        search_box.send_keys(Keys.RETURN)

        # 5. Pause 2 seconds to observe the results on screen
        time.sleep(10)

        # 6. Check the results section exists on the page
        results = driver.find_element(By.ID, "search")
        assert results.is_displayed(), "Results did not appear!"

        # 7. If we reach this line then, test passed
        print("Test 1 passed, results appeared on page")


    # test case 2: checking if the page title matches the query
    def test_page_title_matches_query(self, driver):

        # 1. Open Google
        driver.get("https://www.google.com")

        # 2. Find the search box
        search_box = driver.find_element(By.NAME, "q")

        # 3. Type a different query
        search_box.send_keys("Python programming")
        
        time.sleep(5)

        # 4. Press Enter
        search_box.send_keys(Keys.RETURN)

        # 5. Pause 2 seconds to observe the page title changing
        time.sleep(10)

        # 6. Check that the browser tab title contains our search word
        assert "Python" in driver.title, "Title did not match the search query!"

        # 7. Print the actual title so you can see it in the terminal
        print(f"Test 2 passed, page title is: '{driver.title}'")