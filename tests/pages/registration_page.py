# File: tests/pages/registration_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging

logger = logging.getLogger(__name__)

class RegistrationPage(BasePage):
    """Page object for registration page"""
    
    # Element locators
    USERNAME_INPUT = (By.ID, "reg-username")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "reg-password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "confirm-password")
    REGISTER_BUTTON = (By.ID, "register-button")
    MESSAGE = (By.ID, "reg-message")
    
    def navigate_to(self, url="http://webapp"):
        """Navigate to registration page"""
        logger.info(f"Navigating to registration page: {url}")
        self.driver.get(url)
        return self
    
    def register(self, username, email, password, confirm_password):
        """Register with provided information"""
        logger.info(f"Attempting registration for username: {username}")
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.enter_text(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click_element(self.REGISTER_BUTTON)
        return self
    
    def get_message(self):
        """Get message text and class after registration attempt"""
        message_element = self.wait_for_element(self.MESSAGE)
        text = message_element.text
        class_name = message_element.get_attribute("class")
        logger.info(f"Registration message: '{text}', class: '{class_name}'")
        return text, class_name