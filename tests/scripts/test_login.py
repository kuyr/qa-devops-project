from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os
import logging

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

def test_github_homepage(chrome_driver):
    """Test that GitHub homepage loads correctly."""
    logger.info("Starting GitHub homepage test")
    chrome_driver.get("https://github.com")
    logger.info(f"Page title: {chrome_driver.title}")
    assert "GitHub" in chrome_driver.title

def test_python_org(chrome_driver):
    """Test that Python.org loads correctly."""
    logger.info("Starting Python.org test")
    chrome_driver.get("https://www.python.org")
    logger.info(f"Page title: {chrome_driver.title}")
    assert "Python" in chrome_driver.title

def test_login_success(chrome_driver):
    """Test successful login on our test application."""
    # Get the URL from environment variable or use default
    test_url = os.getenv("TEST_URL", "http://webapp")
    logger.info(f"Starting login test on {test_url}")
    
    chrome_driver.get(f"{test_url}")
    logger.info(f"Page title: {chrome_driver.title}")
    
    # Fill in login form with correct credentials
    username = chrome_driver.find_element(By.ID, "username")
    password = chrome_driver.find_element(By.ID, "password")
    login_button = chrome_driver.find_element(By.ID, "login-button")
    
    username.send_keys("testuser")
    password.send_keys("password")
    login_button.click()
    
    # Wait for success message to appear
    WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    
    message = chrome_driver.find_element(By.ID, "message")
    logger.info(f"Login message: {message.text}")
    
    # Verify message is success
    assert "Login successful" in message.text
    assert "success" in message.get_attribute("class")

def test_login_failure(chrome_driver):
    """Test failed login on our test application."""
    # Get the URL from environment variable or use default
    test_url = os.getenv("TEST_URL", "http://webapp")
    logger.info(f"Starting failed login test on {test_url}")
    
    chrome_driver.get(f"{test_url}")
    
    # Fill in login form with incorrect credentials
    username = chrome_driver.find_element(By.ID, "username")
    password = chrome_driver.find_element(By.ID, "password")
    login_button = chrome_driver.find_element(By.ID, "login-button")
    
    username.send_keys("wronguser")
    password.send_keys("wrongpass")
    login_button.click()
    
    # Wait for error message to appear
    WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    
    message = chrome_driver.find_element(By.ID, "message")
    logger.info(f"Login message: {message.text}")
    
    # Verify message is error
    assert "Invalid username or password" in message.text
    assert "error" in message.get_attribute("class")

def test_registration_form(chrome_driver):
    """Test the registration form on our test application."""
    # Get the URL from environment variable or use default
    test_url = os.getenv("TEST_URL", "http://webapp")
    logger.info(f"Starting registration test on {test_url}")
    
    chrome_driver.get(f"{test_url}")
    
    # Fill in registration form
    username = chrome_driver.find_element(By.ID, "reg-username")
    email = chrome_driver.find_element(By.ID, "email")
    password = chrome_driver.find_element(By.ID, "reg-password")
    confirm_password = chrome_driver.find_element(By.ID, "confirm-password")
    register_button = chrome_driver.find_element(By.ID, "register-button")
    
    username.send_keys("newuser")
    email.send_keys("newuser@example.com")
    password.send_keys("securepassword")
    confirm_password.send_keys("securepassword")
    register_button.click()
    
    # Wait for success message to appear
    WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.ID, "reg-message"))
    )
    
    message = chrome_driver.find_element(By.ID, "reg-message")
    logger.info(f"Registration message: {message.text}")
    
    # Verify message is success
    assert "Registration successful" in message.text
    assert "newuser" in message.text
    assert "success" in message.get_attribute("class")