from unittest import async_case
from fastapi import FastAPI, Request

app = FastAPI()


@app.get('/')
async def puchet():
    return "i am arbaz"


@app.post('/{puchi}')
def puchi(puchi: int):
    return {puchi}
