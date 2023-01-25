from fastapi import FastAPI

from api.db import database
from api.rotas import root_router


app = FastAPI()

app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


@app.get("/")
def get_root():
    return {"mensagem": "api"}


app.include_router(root_router, prefix="")
