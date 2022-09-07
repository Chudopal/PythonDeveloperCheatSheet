from pydantic import BaseModel, ValidationError, validator


class RequestInfo(BaseModel):
    cats: int
    dogs: int

    @validator('*')
    def num_of_facts(cls, value):
        if value > 5:
            raise ValidationError('Too many facts you want to know')
        elif value <= 0:
            raise ValidationError('Facts number can`t be less or equal zero')
        return value


class DogsFactsResponse(BaseModel):
    facts: tuple[str, ...]
    success: bool


class CatsFactsResponse(BaseModel):
    data: tuple[str, ...]


class ResponseInfo(BaseModel):
    cats: tuple[str, ...]
    dogs: tuple[str, ...]
