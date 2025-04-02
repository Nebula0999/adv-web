import requests
from django.conf import settings

class ExternalAPIService:
    def __init__(self):
        self.base_url = settings.EXTERNAL_API_CONFIG['BASE_URL']
        self.api_key = settings.EXTERNAL_API_CONFIG['API_KEY']
        self.timeout = settings.EXTERNAL_API_CONFIG['TIMEOUT']

    def get_data(self, endpoint, params=None):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }
        url = f'{self.base_url}/{endpoint}'
        response = requests.get(url, headers=headers, params=params, timeout=self.timeout)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()

    def post_data(self, endpoint, data):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }
        url = f'{self.base_url}/{endpoint}'
        response = requests.post(url, headers=headers, json=data, timeout=self.timeout)
        response.raise_for_status()
        return response.json()