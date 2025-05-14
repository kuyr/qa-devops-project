# tests/conftest.py

import pytest
import time


# Initialize metrics as None - will be set up once per test session
TEST_COUNTER = None
TEST_SUCCESS = None
TEST_FAILURE = None
TEST_DURATION = None

@pytest.fixture(scope="session", autouse=True)
def setup_metrics():
    """Set up metrics once per test session"""
    global TEST_COUNTER, TEST_SUCCESS, TEST_FAILURE, TEST_DURATION
    
    try:
        from metrics_exporter import TEST_COUNTER as tc, TEST_SUCCESS as ts, TEST_FAILURE as tf, TEST_DURATION as td
        TEST_COUNTER = tc
        TEST_SUCCESS = ts  
        TEST_FAILURE = tf
        TEST_DURATION = td
    except ImportError:
        # If metrics_exporter is not available, create dummy metrics
        from prometheus_client import Counter, Gauge
        TEST_COUNTER = Counter('qa_tests_total', 'Total number of tests run')
        TEST_SUCCESS = Counter('qa_tests_passed', 'Number of tests passed')
        TEST_FAILURE = Counter('qa_tests_failed', 'Number of tests failed')
        TEST_DURATION = Gauge('qa_test_duration_seconds', 'Test duration in seconds')

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Before each test starts"""
    item._start_time = time.time()

@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item):
    """After each test completes"""
    if hasattr(item, '_start_time'):
        duration = time.time() - item._start_time
        if TEST_DURATION:
            TEST_DURATION.set(duration)

@pytest.hookimpl(trylast=True)
def pytest_runtest_logreport(report):
    """Process test results"""
    if report.when == 'call':
        if TEST_COUNTER:
            TEST_COUNTER.inc()
        
        if report.passed and TEST_SUCCESS:
            TEST_SUCCESS.inc()
        elif report.failed and TEST_FAILURE:
            TEST_FAILURE.inc()




# import pytest
# import time
# import requests
# import os

# # URL of your metrics exporter
# METRICS_URL = os.getenv('METRICS_URL', 'http://metrics-exporter:9464')

# @pytest.hookimpl(tryfirst=True)
# def pytest_runtest_setup(item):
#     """Called before each test starts"""
#     # Store start time
#     item._start_time = time.time()

# @pytest.hookimpl(trylast=True)
# def pytest_runtest_teardown(item):
#     """Called after each test completes"""
#     # Calculate test duration
#     if hasattr(item, '_start_time'):
#         duration = time.time() - item._start_time
        
#         # Send duration metric to the exporter
#         try:
#             requests.get(f'{METRICS_URL}/metrics')  # Just to verify connection
#         except Exception as e:
#             print(f"Could not connect to metrics exporter: {e}")

# @pytest.hookimpl(trylast=True)
# def pytest_runtest_logreport(report):
#     """Process test results"""
#     if report.when == 'call':  # Only count the actual test execution
#         # Import here to avoid circular imports
#         from prometheus_client import Counter, Gauge
        
#         # Define metrics locally for this session
#         TEST_COUNTER = Counter('qa_tests_total', 'Total number of tests run')
#         TEST_SUCCESS = Counter('qa_tests_passed', 'Number of tests passed')
#         TEST_FAILURE = Counter('qa_tests_failed', 'Number of tests failed')
        
#         # Update counters based on test result
#         TEST_COUNTER.inc()
        
#         if report.passed:
#             TEST_SUCCESS.inc()
#         elif report.failed:
#             TEST_FAILURE.inc()














# # File: tests/conftest.py
# import pytest
# import time
# import sys
# sys.path.insert(0, '/app')
# from .metrics_exporter import TEST_COUNTER, TEST_SUCCESS, TEST_FAILURE, TEST_DURATION

# @pytest.hookimpl(tryfirst=True)
# def pytest_runtest_setup(item):
#     """Set up for each test"""
#     # Increment the total test counter
#     TEST_COUNTER.inc()
    
#     # Store start time
#     item._start_time = time.time()

# @pytest.hookimpl(trylast=True)
# def pytest_runtest_teardown(item):
#     """Tear down after each test"""
#     # Calculate test duration
#     if hasattr(item, '_start_time'):
#         duration = time.time() - item._start_time
#         TEST_DURATION.set(duration)

# @pytest.hookimpl(trylast=True)
# def pytest_runtest_protocol(item, nextitem):
#     """Called for each test"""
#     # This hook is part of pytest's execution flow
#     # Return None to proceed with normal execution
#     return None

# @pytest.hookimpl(trylast=True)
# def pytest_runtest_logreport(report):
#     """Process test reports"""
#     if report.when == 'call':  # Only count the actual test call
#         if report.passed:
#             TEST_SUCCESS.inc()
#         elif report.failed:
#             TEST_FAILURE.inc()


