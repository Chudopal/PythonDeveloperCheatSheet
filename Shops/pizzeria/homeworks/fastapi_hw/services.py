import aiohttp
from models import CatsFactsResponse, DogsFactsResponse

CATS_URL = 'https://cat-fact.herokuapp.com/facts'
DOGS_URL = 'http://dog-api.kinduff.com/api/facts'

ANIMALS_CREDENTIALS = {
    'cats': {
        'url': 'https://cat-fact.herokuapp.com/facts',
        'param': 'count'
    },
    'dogs': {
        'url': 'http://dog-api.kinduff.com/api/facts',
        'param': 'number'
    },
}


# class CatsService:
#     def __init__(self, service_url: str, facts_number_param: str):
#         self.url = service_url
#         self.facts_number_param = facts_number_param
#
#     def get_facts(self, facts_number: int = None):
#         async with aiohttp.ClientSession() as session:
#             url = 'http://api.openweathermap.org/data/2.5/weather'
#             params = {'q': city, 'APPID': '1f39ad38400b62f2f70eaa91ef87e50a'}
#
#             async with session.get(url=url, params=params) as response:
#                 response = await response.json()
#         return response
#
#
# class DogsService:
#     def __init__(self, service_url: str):
#         self.url = service_url
def get_facts(url: str, params: dict = None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, params=params) as response:
            response = await response.json()
    return response


def get_cats_facts(facts_number: int = None) -> CatsFactsResponse:
    params = None
    if facts_number:
        params = {'count': facts_number}
    response = await get_facts(CATS_URL, params)
    return CatsFactsResponse(**response)


def get_dogs_facts(facts_number: int = None) -> DogsFactsResponse:
    params = None
    if facts_number:
        params = {'number': facts_number}
    response = await get_facts(DOGS_URL, params)
    return DogsFactsResponse(**response)


def process_request(request: dict):
    pass
