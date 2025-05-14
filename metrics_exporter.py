# from prometheus_client import Counter, Gauge, start_http_server
# import time
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Define metrics
# TEST_COUNTER = Counter('qa_tests_total', 'Total number of tests run')
# TEST_SUCCESS = Counter('qa_tests_passed', 'Number of tests passed')
# TEST_FAILURE = Counter('qa_tests_failed', 'Number of tests failed')
# TEST_DURATION = Gauge('qa_test_duration_seconds', 'Test duration in seconds')

# # Start the metrics server
# def start_metrics_server(port=9464):
#     """Start the metrics server on the specified port"""
#     try:
#         start_http_server(port, addr='0.0.0.0')
#         logger.info(f"Metrics server started on port {port}")
        
#         # Initialize with some values for testing
#         TEST_COUNTER.inc(3)
#         TEST_SUCCESS.inc(2)
#         TEST_FAILURE.inc(1)
#         TEST_DURATION.set(1.5)
        
#         # Keep the server running
#         while True:
#             time.sleep(1)
#     except Exception as e:
#         logger.error(f"Failed to start metrics server: {e}")

# if __name__ == "__main__":
#     start_metrics_server()
# File: metrics_exporter.py
from prometheus_client import Counter, Gauge, start_http_server
import threading
import time
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define metrics
TEST_COUNTER = Counter('qa_tests_total', 'Total number of tests run')
TEST_SUCCESS = Counter('qa_tests_passed', 'Number of tests passed')
TEST_FAILURE = Counter('qa_tests_failed', 'Number of tests failed')
TEST_DURATION = Gauge('qa_test_duration_seconds', 'Test duration in seconds')

# Initialize with example values
# TEST_COUNTER.inc(10)
# TEST_SUCCESS.inc(9)
# TEST_FAILURE.inc(1)
# TEST_DURATION.set(6)

if __name__ == "__main__":
    # Start the metrics server
    logger.info("Starting metrics server on port 9464...")
    start_http_server(9464, addr='0.0.0.0')
    logger.info("Metrics server started!")

    # Keep the script running
    while True:
        logger.info("Metrics server is running...")
        time.sleep(60)