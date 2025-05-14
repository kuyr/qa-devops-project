.PHONY: build run test clean

# Build the Docker image
build:
	docker build -t qa-tests .

# Build with no cache
build-clean:
	docker build -t qa-tests . --no-cache

# Run the tests
run:
	docker run --rm qa-tests

# Run bash in the container for debugging
debug:
	docker run --rm -it qa-tests bash

# Remove unused Docker resources
clean:
	docker system prune -f

# Run tests with Docker Compose
compose-up:
	docker compose up --build -d

# Tear down Docker Compose environment
compose-down:
	docker compose down

# Check versions of Chrome and ChromeDriver
check-versions:
	docker run --rm qa-tests sh -c "chromium --version && chromedriver --version"

# Run a simple test to verify the setup
verify:
	docker run --rm qa-tests sh -c "python -c \"from selenium import webdriver; from selenium.webdriver.chrome.service import Service; from selenium.webdriver.chrome.options import Options; options = Options(); options.binary_location = '/usr/bin/chromium'; options.add_argument('--headless=new'); options.add_argument('--no-sandbox'); service = Service(executable_path='/usr/bin/chromedriver'); driver = webdriver.Chrome(service=service, options=options); print('WebDriver created successfully!'); driver.get('https://github.com'); print(f'Page title: {driver.title}'); driver.quit()\""


# Run tests with pytest
test:
	docker run --rm --network qa-devops-project_qa-network -e TEST_URL=http://webapp qa-devops-project-qa-tests pytest tests/scripts/test_login.py -v