import uvicorn
from fastapi import FastAPI
from models import Request, Response
from services import get_data, make_response
from config import SERVICE_HOST, SERVICE_PORT


app = FastAPI(title='HW_Application')


@app.post(
    '/post',
    description='Facts about animals',
    response_model=Request,
)
async def an(test: Request):
    return ...


if __name__ == "__main__":
    uvicorn.run(app=app, host=SERVICE_HOST, port=SERVICE_PORT)
