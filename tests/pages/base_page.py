# File: tests/pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        self.driver = driver
        
    def wait_for_element(self, locator, timeout=10):
        """Wait for element to be visible and return it"""
        logger.info(f"Waiting for element: {locator}")
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def find_element(self, locator):
        """Find element and return it"""
        logger.info(f"Finding element: {locator}")
        return self.driver.find_element(*locator)
        
    def click_element(self, locator):
        """Click on element"""
        logger.info(f"Clicking element: {locator}")
        self.find_element(locator).click()
        
    def enter_text(self, locator, text):
        """Enter text into element"""
        logger.info(f"Entering text '{text}' in element: {locator}")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)