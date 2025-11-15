import requests
from config.config import Config

class APIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.timeout = Config.TIMEOUT

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, timeout=self.timeout)
        return response
    
    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data, timeout=self.timeout)
        return response
    
    def put(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, json=data, timeout=self.timeout)
        return response
    
    def patch(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.patch(url, json=data, timeout=self.timeout)
        return response
    
    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url, timeout=self.timeout)
        return response
