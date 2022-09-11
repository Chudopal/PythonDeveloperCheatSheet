import aiohttp
from typing import Optional
from models import CatsFactsResponse, DogsFactsResponse, TranslateResponse

CATS_URL = 'https://meowfacts.herokuapp.com/'
DOGS_URL = 'http://dog-api.kinduff.com/api/facts'
TRANSLATION_URL = 'https://libretranslate.de/translate'


async def get_data_from_api(url: str, params: Optional[dict], method: str):
    async with aiohttp.ClientSession() as session:
        if method == 'get':
            async with session.get(url=url, params=params, timeout=5) as response:
                response = await response.json()
        elif method == 'post':
            async with session.post(url=url, json=params, timeout=5) as response:
                response = await response.json()
    return response


async def prepare_data_to_translation(animal_facts: tuple[str, ...], source: str, target: str):
    result = []
    for fact in animal_facts:
        params = {
            'q': fact,
            'source': source,
            'target': target,
            'format': 'text',
        }
        translated_response = await get_data_from_api(url=TRANSLATION_URL, params=params, method='post')
        result.append(TranslateResponse(**translated_response).translated_text)
    return result


async def get_cats_facts(facts_number: Optional[int]) -> tuple:
    params = None
    if facts_number:
        params = {'count': facts_number}
    response = await get_data_from_api(CATS_URL, params, method='get')
    return CatsFactsResponse(**response).data


async def get_dogs_facts(facts_number: Optional[int]) -> tuple:
    params = None
    if facts_number:
        params = {'number': facts_number}
    response = await get_data_from_api(DOGS_URL, params, method='get')
    return DogsFactsResponse(**response).facts


facts_about_animals = {
    'cats': get_cats_facts,
    'dogs': get_dogs_facts
}


async def process_request(request: dict):
    result = {}
    for animal, facts_num in request.items():
        if facts_num is not None:
            result[animal] = await prepare_data_to_translation(
                await facts_about_animals.get(animal)(facts_num),
                source='en',
                target='ru',
            )
    return result
