import aiohttp
from models import CatsFactsResponse, DogsFactsResponse, ResponseInfo

CATS_URL = 'https://meowfacts.herokuapp.com/'
DOGS_URL = 'http://dog-api.kinduff.com/api/facts'


async def get_facts(url: str, params: dict = None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, params=params, timeout=5) as response:
            response = await response.json()
    return response


async def get_cats_facts(facts_number: int = None) -> CatsFactsResponse:
    params = None
    if facts_number:
        params = {'count': facts_number}
    response = await get_facts(CATS_URL, params)
    return CatsFactsResponse(**response)


async def get_dogs_facts(facts_number: int = None) -> DogsFactsResponse:
    params = None
    if facts_number:
        params = {'number': facts_number}
    response = await get_facts(DOGS_URL, params)
    return DogsFactsResponse(**response)


facts_about_animals = {
    'cats': get_cats_facts,
    'dogs': get_dogs_facts
}


async def process_request(request: dict):
    result = {}
    for animal, facts_num in request.items():
        result[animal] = await facts_about_animals.get(animal)(facts_num)
    return result


def make_response(data: dict) -> ResponseInfo:
    result = {
        'cats': data.get('cats').data,
        'dogs': data.get('dogs').facts
    }
    return ResponseInfo(**result)
