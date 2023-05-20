from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase

from config import DB_DRIVER, DB_CONNECTOR, DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = "{}+{}://{}:{}@{}:{}/{}".format(
    DB_DRIVER, DB_CONNECTOR,
    DB_USER, DB_PASS,
    DB_HOST, DB_PORT,
    DB_NAME
)

metadata = MetaData()

engine = create_engine(
    DATABASE_URL
)


class Base(DeclarativeBase):
    pass


Base.metadata.create_all(engine)
