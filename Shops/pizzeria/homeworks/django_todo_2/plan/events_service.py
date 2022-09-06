import requests
import json


class EventsService:

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = str(port)

    def get_all_events(self):
        endpoint = "/api/events/"
        url = self.host + ':' + self.port + endpoint
        print("URL:", url)
        return requests.get(url)

    def get_event_details(self, event_uuid: str):
        endpoint = "/api/events/"
        url = self.host + ':' + self.port + endpoint + event_uuid
        return requests.get(url)

    def add_event(self, data: json):
        headers = {"Content-type": "application/json"}
        endpoint = "/api/events/"
        url = self.host + ':' + self.port + endpoint
        return requests.post(url=url, data=data, headers=headers)
