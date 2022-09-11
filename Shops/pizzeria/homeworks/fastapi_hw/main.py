from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from models import RequestInfo, ResponseInfo
from services import process_request
import uvicorn

app = FastAPI(title='Funny facts about Cats and Dogs')


@app.post(
    '/info',
    description='Get funny facts about Cats nd Dogs',
)
async def get_info(request: RequestInfo) -> dict:
    try:
        data = await process_request(request=request.dict())
    except Exception as error:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=error.__class__.__name__,
        )
    return ResponseInfo(**data).dict(exclude_none=True)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host='127.0.0.1',
        port=8000
    )
