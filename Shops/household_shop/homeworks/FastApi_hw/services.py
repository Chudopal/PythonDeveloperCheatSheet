import aiohttp
from typing import Union
from config import CATS_URL, DOGS_URL
from models import Request, Response, CurrencyInfo, WeatherReaponse


async def get_data(requset: Request) -> Response:
    ...


async def make_response(service_name: str) -> Union[tuple[CurrencyInfo, ...], WeatherReaponse]:
    ...