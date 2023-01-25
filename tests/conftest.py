import os
from fastapi.testclient import TestClient
import pytest


os.environ["DATABASE_URL"] = "sqlite:///testedb.sqlite"
os.environ["FORCE_ROLLBACK"] = "True"

from api.__main__ import app
from api.config import DATABASE_URL
from api.cria_tabelas import configurar_banco


@pytest.fixture(scope="function")
def client():
    configurar_banco(DATABASE_URL)
    with TestClient(app) as c:
        yield c
