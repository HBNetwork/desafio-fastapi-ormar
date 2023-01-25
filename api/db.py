import databases
import sqlalchemy

from api.config import DATABASE_URL, TEST_DATABASE


database = databases.Database(DATABASE_URL, force_rollback=TEST_DATABASE)
metadata = sqlalchemy.MetaData()
