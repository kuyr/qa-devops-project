# metrics_exporter.py
from prometheus_client import Counter, Gauge, start_http_server, CollectorRegistry
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a custom registry to avoid duplicates
REGISTRY = CollectorRegistry()

# Define metrics
TEST_COUNTER = Counter('qa_tests_total', 'Total number of tests run', registry=REGISTRY)
TEST_SUCCESS = Counter('qa_tests_passed', 'Number of tests passed', registry=REGISTRY)
TEST_FAILURE = Counter('qa_tests_failed', 'Number of tests failed', registry=REGISTRY)
TEST_DURATION = Gauge('qa_test_duration_seconds', 'Test duration in seconds', registry=REGISTRY)
TEST_LOGIN_ATTEMPTS = Counter('qa_login_attempts_total', 'Total login attempts', ['status'], registry=REGISTRY)



if __name__ == "__main__":
    # Start the metrics server
    logger.info("Starting metrics server on port 9464...")
    start_http_server(9464, addr='0.0.0.0', registry=REGISTRY)
    logger.info("Metrics server started!")

    # Keep the script running
    while True:
        logger.info("Metrics server is running...")
        time.sleep(60)



# # File: tests/metrics_exporter.py

# from prometheus_client import Counter, Gauge, start_http_server
# import threading
# import logging
# import os

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Define metrics
# TEST_COUNTER = Counter('qa_tests_total', 'Total number of tests run')
# TEST_SUCCESS = Counter('qa_tests_passed', 'Number of tests passed')
# TEST_FAILURE = Counter('qa_tests_failed', 'Number of tests failed')
# TEST_DURATION = Gauge('qa_test_duration_seconds', 'Test duration in seconds')
# TEST_LOGIN_ATTEMPTS = Counter('qa_login_attempts_total', 'Total login attempts', ['status'])

# # check before starting the server
# _server_started = False

# def start_metrics_server(port=9464):
#     """Start the metrics server on the specified port"""
#     global _server_started
#     if _server_started:
#         return
    
#     try:
#         start_http_server(port)
#         logger.info(f"Metrics server started on port {port}")
#         _server_started = True
#     except Exception as e:
#         logger.error(f"Failed to start metrics server: {e}")

# # Only start server if this file is imported directly
# if not os.environ.get('PYTEST_XDIST_WORKER'):
#     threading.Thread(target=start_metrics_server, daemon=True).start()
