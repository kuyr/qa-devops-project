# tests/metrics_client.py
import requests
import os

class MetricsClient:
    def __init__(self):
        self.metrics_url = os.getenv('METRICS_URL', 'http://metrics-exporter:9464')
    
    def increment_counter(self, metric_name, value=1):
        """Send metric update to the metrics exporter"""
        try:
            # This is a simplified approach - in real scenarios, you'd use
            # a proper metrics gateway or shared storage
            requests.post(f'{self.metrics_url}/update', 
                         json={'metric': metric_name, 'value': value})
        except Exception as e:
            print(f"Failed to update metric {metric_name}: {e}")
    
    def set_gauge(self, metric_name, value):
        """Set gauge value"""
        try:
            requests.post(f'{self.metrics_url}/gauge', 
                         json={'metric': metric_name, 'value': value})
        except Exception as e:
            print(f"Failed to set gauge {metric_name}: {e}")