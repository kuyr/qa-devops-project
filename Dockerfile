FROM --platform=linux/arm64 python:3.10-slim

# Install required tools and dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    file \
    chromium \
    chromium-driver \
    libnss3 \
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

# Verify ChromeDriver installation
RUN which chromedriver && \
    chromedriver --version || echo "ChromeDriver version check failed"

# Verify Chromium installation
RUN which chromium && \
    chromium --version || echo "Chromium version check failed"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run tests with verbose output
CMD echo "ChromeDriver Path: $(which chromedriver)" && \
    echo "ChromeDriver Version: $(chromedriver --version || echo 'Cannot get version')" && \
    echo "Chromium Path: $(which chromium)" && \
    echo "Chromium Version: $(chromium --version || echo 'Cannot get version')" && \
    pytest tests/scripts/ --html=report.html -v