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

# Verify ChromeDriver installation and set up the path
RUN which chromedriver && \
    chromedriver --version || true && \
    find /usr -name "chromedriver" | head -1

# Make sure we use the correct ChromeDriver path
RUN CHROMEDRIVER_PATH=$(find /usr -name "chromedriver" | head -1) && \
    if [ -n "$CHROMEDRIVER_PATH" ]; then \
        echo "Found ChromeDriver at $CHROMEDRIVER_PATH"; \
        ln -sf $CHROMEDRIVER_PATH /usr/bin/chromedriver; \
        chmod +x /usr/bin/chromedriver; \
    else \
        echo "ChromeDriver not found in /usr"; \
        exit 1; \
    fi

# Verify Chromium
RUN which chromium && \
    chromium --version || true

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Print debug info when the container starts
CMD echo "ChromeDriver Path: $(which chromedriver)" && \
    echo "ChromeDriver Version: $(chromedriver --version || echo 'Cannot get version')" && \
    echo "Chromium Path: $(which chromium)" && \
    echo "Chromium Version: $(chromium --version || echo 'Cannot get version')" && \
    pytest tests/scripts/ --html=report.html