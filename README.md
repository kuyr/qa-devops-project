# QA DevOps Automation Project
**Goal:** Dockerized test automation with CI/CD.  

## 🛠️ Tech Stack  
- Python + Pytest (or JavaScript/WebdriverIO if you prefer)  
- GitHub Actions  
- Docker  

## 📂 Project Structure 
```
qa-devops-project/
├── Dockerfile                      # Docker configuration test container
├── Makefile                        # Make commands for common operations
├── docker-compose.yml              # Multi-container setup
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
│
├── .github/                        # GitHub configuration
│   └── workflows/
│       └── selenium-tests.yml      # GitHub Actions workflow
│
├── tests/                          # Test files
│   └── scripts/
│       └── test_login.py           # Selenium test file
│
├── test-app/                       # Test application
│   └── index.html                  # Web application for testing
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── app.js
│
├── prometheus/                     # Prometheus configuration
│   └── prometheus.yml              # Prometheus config file
│
└── reports/                        # Test reports (generated)
    └── report.html                 # HTML test report

#### **5. Commit and push:**
```bash
git add .
git commit -m "Initial setup: Folders, dummy test, README"
git push origin main

## 🚀 Quick Start
```bash
# Run all tests
docker run qa-tests

# Get HTML report
mkdir -p reports && docker run -v $(pwd)/reports:/app/reports qa-tests

# DevOps QA Automation Framework

A comprehensive framework that combines QA automation with DevOps practices, designed to demonstrate the integration of testing, CI/CD, monitoring, and infrastructure management.

## Features

- **Containerized Tests**: Selenium tests running in Docker containers
- **Multi-Container Environment**: Using Docker Compose for test applications and services
- **CI/CD Integration**: GitHub Actions workflows for continuous testing
- **Monitoring**: Prometheus and Grafana for observability
- **Cross-Platform**: ARM64 compatible for M1/M2 Mac environments

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Git (for version control)
- Make (optional, for using the Makefile)

### Setup and Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/qa-devops-project.git
   cd qa-devops-project
   ```

2. Build the test container:
   ```bash
   make build
   # or
   docker build -t qa-tests .
   ```

3. Run the tests:
   ```bash
   make run
   # or
   docker run --rm qa-tests
   ```

4. Run with Docker Compose (includes test app and monitoring):
   ```bash
   make compose-up
   # or
   docker-compose up
   ```

### Testing the Setup

Verify that everything is working:

```bash
make verify
# or
docker run --rm qa-tests sh -c "python -c \"from selenium import webdriver; from selenium.webdriver.chrome.service import Service; from selenium.webdriver.chrome.options import Options; options = Options(); options.binary_location = '/usr/bin/chromium'; options.add_argument('--headless=new'); options.add_argument('--no-sandbox'); service = Service(executable_path='/usr/bin/chromedriver'); driver = webdriver.Chrome(service=service, options=options); print('WebDriver created successfully!'); driver.get('https://github.com'); print(f'Page title: {driver.title}'); driver.quit()\""
```

## Project Structure

```
qa-devops-project/
├── Dockerfile                  # Docker configuration
├── Makefile                    # Common commands
├── docker-compose.yml          # Multi-container setup
├── tests/scripts/              # Test scripts
├── test-app/                   # Test application
└── prometheus/                 # Monitoring configuration
```

## Using the Makefile

The project includes a Makefile with common commands:

- `make build`: Build the Docker image
- `make run`: Run the tests
- `make debug`: Open a shell in the container for debugging
- `make compose-up`: Start the full environment with Docker Compose
- `make compose-down`: Stop the Docker Compose environment
- `make check-versions`: Check Chrome and ChromeDriver versions
- `make verify`: Run a simple test to verify the setup

## Accessing Services

When running with Docker Compose:

- **Test Application**: http://localhost:8080
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (admin/admin)

## GitHub Actions Integration

The project includes a GitHub Actions workflow that runs the tests on every push to the main branch. Test reports are uploaded as artifacts for review.

## Troubleshooting

If you encounter issues:

1. Check that ChromeDriver and Chromium versions match:
   ```bash
   make check-versions
   ```

2. Debug inside the container:
   ```bash
   make debug
   ```

3. For ARM64-specific issues (M1/M2 Macs), ensure the Dockerfile has the correct platform specification and paths.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

This project is part of a DevOps QA skills demonstration, showcasing the integration of QA automation with modern DevOps practices.