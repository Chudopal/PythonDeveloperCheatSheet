import requests
from .models import Event

class ConnectService:
    def __init__(self, url) -> None:
        self.url = url
    
    def get_data(self):
        return requests.get(url=self.url).json()

    def post_data(self):
        return requests.post(url=self.url, json=Event.json())
