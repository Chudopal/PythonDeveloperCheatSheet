from enum import Enum
from pydantic import BaseModel
from typing import Tuple, Union


class Request(BaseModel):
    fields: tuple[str, ...]


class CatsResponse(BaseModel):
    ...


class DogsResponse(BaseModel):
    ...


class Response(BaseModel):
    data: tuple[str, ...]
