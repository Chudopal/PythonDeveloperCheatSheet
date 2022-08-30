import requests


class ConnectService:
    def __init__(self, url) -> None:
        self.url = url
        self.headers = {"Content-type": "application/json"}

    def get_list_events(self):
        return requests.get(url=self.url).json()

    def add_event(self, data):
        return requests.post(url=self.url, data=data, headers=self.headers)

    def get_event_detail(self):
        return requests.get(url=self.url).json()

    def delete_event(self):
        return requests.delete(url=self.url)

    def update_event(self, data):
        return requests.put(url=self.url, data=data, headers=self.headers)
