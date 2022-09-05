from pydantic import BaseModel, ValidationError, validator
from typing import Optional


class RequestInfo(BaseModel):
    cats: int
    dogs: int

    @validator('cats', 'dogs')
    def num_of_facts(cls, num):
        if num > 5:
            raise ValidationError('Too many facts you want to know')
        return num


class DogsFactsResponse(BaseModel):
    facts: tuple[str, ...]
    success: bool


class CatsFactsResponse(BaseModel):
    data: tuple[str, ...]


class ResponseInfo(BaseModel):
    cats: tuple[str, ...]
    dogs: tuple[str, ...]
