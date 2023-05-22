from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool

from config import DB_DRIVER, ASYNC_DB_CONNECTOR, DB_CONNECTOR, DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = "{}+{}://{}:{}@{}:{}/{}".format(
    DB_DRIVER, ASYNC_DB_CONNECTOR,
    DB_USER, DB_PASS,
    DB_HOST, DB_PORT,
    DB_NAME
)


class Base(DeclarativeBase):
    pass


metadata = MetaData()

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
