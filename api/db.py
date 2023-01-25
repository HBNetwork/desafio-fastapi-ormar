import databases
import sqlalchemy

from api.config import DATABASE_URL, FORCE_ROLLBACK


database = databases.Database(DATABASE_URL, force_rollback=FORCE_ROLLBACK)
metadata = sqlalchemy.MetaData()
