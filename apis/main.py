from unittest import async_case
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def puchet():
    return "i am arbaz"
