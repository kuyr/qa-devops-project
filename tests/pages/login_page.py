# File: tests/pages/login_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging
from ..metrics_exporter import TEST_LOGIN_ATTEMPTS

logger = logging.getLogger(__name__)


# Try to import metrics, but don't fail if not available
try:
    from metrics_exporter import TEST_LOGIN_ATTEMPTS
except ImportError:
    TEST_LOGIN_ATTEMPTS = None



class LoginPage(BasePage):
    """Page object for login page"""
    
    # Element locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    MESSAGE = (By.ID, "message")
    
    def navigate_to(self, url="http://webapp"):
        """Navigate to login page"""
        logger.info(f"Navigating to login page: {url}")
        self.driver.get(url)
        return self
    
    def login(self, username, password):
        """Login with provided credentials"""
        logger.info(f"Attempting login with username: {username}")
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

        # Wait for message and record metrics
        message_element = self.wait_for_element(self.MESSAGE)
        message_class = message_element.get_attribute("class")
        
        if TEST_LOGIN_ATTEMPTS:
        # Record login attempt in metrics
            if "success" in message_class:
                TEST_LOGIN_ATTEMPTS.labels(status="success").inc()
            else:
                TEST_LOGIN_ATTEMPTS.labels(status="failure").inc()

        return self
    
    def get_message(self):
        """Get message text and class after login attempt"""
        message_element = self.wait_for_element(self.MESSAGE)
        text = message_element.text
        class_name = message_element.get_attribute("class")
        logger.info(f"Login message: '{text}', class: '{class_name}'")
        return text, class_name