import requests
import json


class EventsService:
    @classmethod
    def get_events(cls, host: str, port: str):
        endpoint = "/api/events/"
        url = host + ':' + port + endpoint
        return requests.get(url)

    @classmethod
    def add_event(cls, host: str, port: str, data: json):
        headers = {
            "Content-type": "application/json",
        }
        endpoint = "/api/events/"
        url = host + ':' + port + endpoint
        return requests.post(url=url, data=data, headers=headers)
