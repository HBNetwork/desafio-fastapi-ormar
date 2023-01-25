from decouple import config


DATABASE_URL = config("DATABASE_URL", default="sqlite:///db.sql")
FORCE_ROLLBACK = config("FORCE_ROLLBACK", default=False, cast=bool)
