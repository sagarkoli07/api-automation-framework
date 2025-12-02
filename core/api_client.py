
import requests
from config.config import BASE_URL

class APIClient:
    def get(self, endpoint: str, params=None):
        url = f"{BASE_URL}/{endpoint}"
        return requests.get(url, params=params)
