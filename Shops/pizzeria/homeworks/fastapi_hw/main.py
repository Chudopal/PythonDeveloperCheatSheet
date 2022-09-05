from fastapi import FastAPI
from models import RequestInfo, ResponseInfo

app = FastAPI(title='Funny facts about Cats and Dogs')


@app.post(
    '/info',
    description='Get funny facts about Cats nd Dogs',
)
async def get_info(request: RequestInfo) -> ResponseInfo:
    pass
