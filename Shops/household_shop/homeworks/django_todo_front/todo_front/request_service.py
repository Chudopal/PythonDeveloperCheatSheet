import requests


class ConnectService:
    def __init__(self, url) -> None:
        self.url = url
    
    def get_all_events(self):
        return requests.get(url=self.url).json()

    def add_event(self, data):
        headers = {"Content-type": "application/json"}
        return requests.post(url=self.url, data=data, headers=headers)

    def get_event_detail(self):
        return requests.get(url=self.url).json()
