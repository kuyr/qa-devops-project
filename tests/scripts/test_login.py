# File: tests/scripts/test_login_pom.py
import pytest
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from ..pages.login_page import LoginPage
from ..pages.base_page import BasePage
from ..pages.registration_page import RegistrationPage


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def chrome_driver():
    # Set up Chrome options
    options = Options()
    options.binary_location = "/usr/bin/chromium"
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    # Create service with explicit path to ChromeDriver
    service = Service(executable_path="/usr/bin/chromedriver")
    
    # Create the driver
    driver = None
    try:
        driver = webdriver.Chrome(service=service, options=options)
        logger.info("WebDriver started successfully")
        yield driver
    except Exception as e:
        logger.error(f"Error starting WebDriver: {e}")
        raise
    finally:
        if driver:
            driver.quit()

@pytest.mark.smoke
def test_login_success(chrome_driver):
    """Test successful login using Page Object Model"""
    login_page = LoginPage(chrome_driver)
    
    # Get the URL from environment variable or use default
    test_url = os.getenv("TEST_URL", "http://webapp")
    
    # Perform login
    login_page.navigate_to(test_url).login("testuser", "password")
    
    # Verify message
    message_text, message_class = login_page.get_message()
    
    assert "Login successful" in message_text
    assert "success" in message_class

@pytest.mark.smoke
def test_login_failure(chrome_driver):
    """Test failed login using Page Object Model"""
    login_page = LoginPage(chrome_driver)
    
    # Get the URL from environment variable or use default
    test_url = os.getenv("TEST_URL", "http://webapp")
    
    # Perform login with wrong credentials
    login_page.navigate_to(test_url).login("wronguser", "wrongpass")
    
    # Verify message
    message_text, message_class = login_page.get_message()
    
    assert "Invalid username or password" in message_text
    assert "error" in message_class

@pytest.mark.regression
def test_registration(chrome_driver):
    """Test registration form using Page Object Model"""
    registration_page = RegistrationPage(chrome_driver)
    
    # Get the URL from environment variable or use default
    test_url = os.getenv("TEST_URL", "http://webapp")
    
    # Perform registration
    registration_page.navigate_to(test_url).register(
        username="newuser",
        email="newuser@example.com",
        password="securepassword",
        confirm_password="securepassword"
    )
    
    # Verify message
    message_text, message_class = registration_page.get_message()
    
    assert "Registration successful" in message_text
    assert "newuser" in message_text
    assert "success" in message_class

@pytest.mark.parametrize("username,password,expected_message,expected_class", [
    ("testuser", "password", "Login successful", "success"),
    ("wronguser", "wrongpass", "Invalid username or password", "error"),
    (" ", " ", "Invalid username or password", "error"),
])
def test_login_scenarios(chrome_driver, username, password, expected_message, expected_class):
    """Test multiple login scenarios using parametrization"""
    login_page = LoginPage(chrome_driver)
    
    # Get the URL from environment variable or use default
    test_url = os.getenv("TEST_URL", "http://webapp")
    
    # Perform login
    login_page.navigate_to(test_url).login(username, password)
        # Verify message
    message_text, message_class = login_page.get_message()
    
    assert expected_message in message_text
    assert expected_class in message_class