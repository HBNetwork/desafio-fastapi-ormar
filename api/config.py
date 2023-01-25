import os

from fastapi import FastAPI


def get_db_uri(*, user, password, host, db):
    return f'postgresql://{user}:{password}@{host}:5432/{db}'


# TODO: Refatorar para usar variaveis de ambiente

DATABASE_URL = get_db_uri(
    user='postgres',
    password='qwerty123456',
    host='localhost',
    db="desafio_cadhab",
)

DATABASE_URL = "sqlite:///db.sqlite"

if os.environ.get("TEST_DATABASE") == "true":
    DATABASE_URL = 'sqlite:///testedb.sqlite'

TEST_DATABASE = os.getenv('TEST_DATABASE', 'false') in ('true', 'yes')
