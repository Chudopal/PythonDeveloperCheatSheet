import requests
import json


class EventsService:
    @classmethod
    def get_all_events(cls, host: str, port: str):
        endpoint = "/api/events/"
        url = host + ':' + port + endpoint
        return requests.get(url)

    @classmethod
    def get_event_details(cls, host: str, port: str, event_uuid: str):
        endpoint = "/api/events/"
        url = host + ':' + port + endpoint + event_uuid
        return requests.get(url)

    @classmethod
    def add_event(cls, host: str, port: str, data: json):
        headers = {
            "Content-type": "application/json",
        }
        endpoint = "/api/events/"
        url = host + ':' + port + endpoint
        return requests.post(url=url, data=data, headers=headers)
