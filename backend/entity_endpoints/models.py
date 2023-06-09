from typing import Optional, Annotated

from sqlalchemy import Column, ForeignKey, Integer, String, Float, ARRAY, Boolean, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import Base
from backend.identity_endpoints.models import UserModel


class CityModel(Base):
    __tablename__ = 'city'
    id = Column(String, primary_key=True)
    geo_data = Column(ARRAY(Float), nullable=True)
    city_name = Column(String, nullable=False)
    rating = Column(Integer, nullable=True)
    timezone = Column(String, nullable=True)

    @classmethod
    async def find_all(
            cls,
            session: AsyncSession,
            offset: int,
            rating: Annotated[float, None] = None,
            limit: int = 10,
    ):
        stmt = select(cls).filter(text('city.rating > {}'.format(rating)))
        stmt = stmt.offset(offset).limit(limit)
        print(stmt)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_one(
            cls,
            session: AsyncSession,
            *args
    ):
        stmt = select(cls).filter(*args)
        result = await session.execute(stmt)
        return result.scalars().one()


class AirPlaneTicketModel(Base):
    __tablename__ = 'airplane_ticket'
    id = Column(String, primary_key=True)
    city_id = Column(String, ForeignKey('city.id'))
    geo_data = Column(ARRAY(Float), nullable=True)
    target_city = Column(String, ForeignKey('city.id'), nullable=False)
    flight_start = Column(String, nullable=False)
    flight_end = Column(String, nullable=False)
    flight_price = Column(Float, nullable=False)
    airline_name = Column(String, nullable=False)

    @classmethod
    async def find_all(
            cls,
            session: AsyncSession,
            offset: int,
            limit: int = 10,
    ):
        stmt = select(cls).filter()
        stmt = stmt.offset(offset).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_one(
            cls,
            session: AsyncSession,
            *args
    ):
        stmt = select(cls).filter(*args)
        result = await session.execute(stmt)
        return result.scalars().one()


class EventModel(Base):
    __tablename__ = 'event'
    id = Column(String, primary_key=True)
    city_id = Column(String, ForeignKey('city.id'))
    start = Column(String, nullable=True)
    end = Column(String, nullable=True)
    duration = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    bought_count = Column(Integer, nullable=True)

    @classmethod
    async def find_all(
            cls,
            session: AsyncSession,
            offset: int,
            limit: int = 10,
    ):
        stmt = select(cls).filter()
        stmt = stmt.offset(offset).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_one(
            cls,
            session: AsyncSession,
            *args
    ):
        stmt = select(cls).filter(*args)
        result = await session.execute(stmt)
        return result.scalars().one()


class ExcursionModel(Base):
    __tablename__ = 'excursion'
    id = Column(String, primary_key=True)
    city_id = Column(String, ForeignKey('city.id'))
    geo_data = Column(ARRAY(Float), nullable=True)
    start = Column(String, nullable=True)
    end = Column(String, nullable=True)
    duration = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    bought_count = Column(Integer, nullable=True)

    @classmethod
    async def find_all(
            cls,
            session: AsyncSession,
            offset: int,
            limit: int = 10,
    ):
        stmt = select(cls).filter()
        stmt = stmt.offset(offset).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_one(
            cls,
            session: AsyncSession,
            *args
    ):
        stmt = select(cls).filter(*args)
        result = await session.execute(stmt)
        return result.scalars().one()


class RestaurantModel(Base):
    __tablename__ = 'restaurant'
    id = Column(String, primary_key=True)
    city_id = Column(String, ForeignKey('city.id'))
    geo_data = Column(ARRAY(Float), nullable=True)
    name = Column(String, nullable=True)
    kitchen_type = Column(ARRAY(String), nullable=True)
    mean_price = Column(Float, nullable=True)
    bought_count = Column(Integer, nullable=True)

    @classmethod
    async def find_all(
            cls,
            session: AsyncSession,
            offset: int,
            limit: int = 10,
    ):
        stmt = select(cls).filter()
        stmt = stmt.offset(offset).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_one(
            cls,
            session: AsyncSession,
            *args
    ):
        stmt = select(cls).filter(*args)
        result = await session.execute(stmt)
        return result.scalars().one()


class RegionModel(Base):
    __tablename__ = 'region'
    id = Column(String, primary_key=True)
    title = Column(String, nullable=True)
    price_hotel = Column(Integer, nullable=True)

    @classmethod
    async def find_all(
            cls,
            session: AsyncSession,
            offset: int,
            limit: int = 10,
    ):
        stmt = select(cls).filter()
        stmt = stmt.offset(offset).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_one(
            cls,
            session: AsyncSession,
            *args
    ):
        stmt = select(cls).filter(*args)
        result = await session.execute(stmt)
        return result.scalars().one()


class HotelModel(Base):
    __tablename__ = 'hotel'
    id = Column(String, primary_key=True)
    city_id = Column(String, ForeignKey('city.id'), nullable=True)
    address = Column(String, nullable=True)
    stars = Column(String, nullable=True)
    geo_data = Column(ARRAY(Float), nullable=True)
    title = Column(String, nullable=True)
    list_services = Column(ARRAY(String), nullable=True)
    bought_count = Column(Integer, nullable=True)

    @classmethod
    async def find_all(
            cls,
            session: AsyncSession,
            offset: int,
            limit: int = 10,
    ):
        stmt = select(cls).filter()
        stmt = stmt.offset(offset).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_one(
            cls,
            session: AsyncSession,
            *args
    ):
        stmt = select(cls).filter(*args)
        result = await session.execute(stmt)
        return result.scalars().one()


class DBUserModel(UserModel):
    ...


class UserAnalyticsModel(Base):
    __tablename__ = 'analytics'
    session = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    target_region = Column(String, ForeignKey('region.id'), nullable=True)
    current_city = Column(String, ForeignKey('city.id'), nullable=True)
    target_city = Column(String, ForeignKey('city.id'), nullable=True)
    airplane_ticket_to = Column(String, ForeignKey('airplane_ticket.id'), nullable=True)
    airplane_ticket_back = Column(String, ForeignKey('airplane_ticket.id'), nullable=True)
    target_hotel = Column(String, ForeignKey('hotel.id'), nullable=True)
    target_restaurant = Column(String, ForeignKey('restaurant.id'), nullable=True)
    target_excursion = Column(String, ForeignKey('excursion.id'), nullable=True)
    bought = Column(Boolean, nullable=False)

    @classmethod
    async def find_all(
            cls,
            session: AsyncSession,
            offset: int,
            limit: int = 10,
    ):
        stmt = select(cls).filter()
        stmt = stmt.offset(offset).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_one(
            cls,
            session: AsyncSession,
            *args
    ):
        stmt = select(cls).filter(*args)
        result = await session.execute(stmt)
        return result.scalars().one()


class DataMlModel(Base):
    __tablename__ = 'mldata'
    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(String, nullable=True)
    username = Column(String, nullable=True)
    bought = Column(Integer, nullable=False)