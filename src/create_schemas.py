from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from database import DATABASE_URL

metadata = MetaData()

engine = create_engine(
    DATABASE_URL
)

Session = sessionmaker(engine)


def get_session():
    with Session() as session:
        yield session


class Base(DeclarativeBase):
    pass


Base.metadata.create_all(engine)
