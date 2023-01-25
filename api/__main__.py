import asyncio
import os
from asyncio.log import logger


from fastapi import FastAPI
from api.rotas import root_router
from api.db import database, metadata

app = FastAPI()

async def connect_db():
    try:
        await database.connect()
    except Exception as e:
        logger.error("connect db error, res is  {}".format(e))
        await asyncio.sleep(3)
        asyncio.ensure_future(connect_db())


if os.environ.get("TEST_DATABASE") != "true":
    app.add_event_handler("startup", connect_db)


@app.get("/")
def get_root():
    return {"mensagem": "api"}


app.include_router(root_router, prefix="")
