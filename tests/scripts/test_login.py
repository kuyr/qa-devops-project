from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
import os
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def chrome_driver():
    # Debug info
    try:
        chromium_path = subprocess.check_output(["which", "chromium"]).decode().strip()
        chromedriver_path = subprocess.check_output(["which", "chromedriver"]).decode().strip()
        logger.info(f"Chromium path: {chromium_path}")
        logger.info(f"ChromeDriver path: {chromedriver_path}")
    except Exception as e:
        logger.error(f"Error finding paths: {e}")
    
    # Set up Chrome options
    options = Options()
    options.binary_location = "/usr/bin/chromium"
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    
    # Create service with explicit path to ChromeDriver
    service = Service(executable_path="/usr/bin/chromedriver")
    
    # Create the driver
    driver = None
    try:
        # Use explicit service with chromedriver path
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
    logger.info("Starting GitHub homepage test")
    chrome_driver.get("https://github.com")
    logger.info(f"Page title: {chrome_driver.title}")
    assert "GitHub" in chrome_driver.title

def test_python_org(chrome_driver):
    logger.info("Starting Python.org test")
    chrome_driver.get("https://www.python.org")
    logger.info(f"Page title: {chrome_driver.title}")
    assert "Python" in chrome_driver.title