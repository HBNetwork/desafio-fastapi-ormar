import sqlalchemy

from api.db import metadata


def configurar_banco(database_url):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)


if __name__ == "__main__":
    from api.config import DATABASE_URL
    configurar_banco(DATABASE_URL)
