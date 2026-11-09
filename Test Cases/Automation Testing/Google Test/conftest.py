import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Opens Chrome before each test 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)   # wait up to 10s for any element to appear
    driver.maximize_window()     # full screen so you can see everything
    
    yield driver                 # hand the browser to the test
    
    # Closes Chrome after each test
    driver.quit()