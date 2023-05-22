from sqlalchemy import (
    Column, ForeignKey, Integer, String, Float, ARRAY
)

from src.database import Base, engine


# class


class _Abstract(object):
    id = Column(String, primary_key=True)


class _CityAbstract(object):
    city_id = Column(String, ForeignKey('city.id'), nullable=True)


class _GeoAbstract(_Abstract):
    geo_data = Column(ARRAY(Float), nullable=True)


class _EventsAbstract(_CityAbstract):
    start = Column(String, nullable=False)
    end = Column(String, nullable=False)
    price = Column(Float, nullable=True)


class City(_GeoAbstract, Base):
    __tablename__ = 'city'
    city_name = Column(String, nullable=False)
    rating = Column(Integer, nullable=True)
    timezone = Column(String, nullable=True)


class Event(_Abstract, _EventsAbstract, Base):
    __tablename__ = 'event'


class Excursion(_Abstract, _EventsAbstract, Base):
    __tablename__ = 'excursion'


class Restaurant(_GeoAbstract, _CityAbstract, Base):
    __tablename__ = 'restaurant'
    name = Column(String, nullable=True)
    kitchen_type = Column(ARRAY(String), nullable=True)
    mean_price = Column(Float, nullable=True)


class Track(_Abstract, Base, _CityAbstract):
    __tablename__ = 'track'
    region = Column(String, ForeignKey('region.id'))
    days_count = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=True)


class Region(_Abstract, Base):
    __tablename__ = 'region'
    title = Column(String, nullable=True)
    price_hotel = Column(Integer, nullable=True)


class Route(_Abstract, Base, _CityAbstract):
    __tablename__ = 'route'
    title = Column(String, nullable=True)
    time = Column(String, nullable=True)


class Hotel(_Abstract, Base, _CityAbstract):
    __tablename__ = 'hotel'
    address = title = Column(String, nullable=True)
    geo_data = Column(ARRAY(Float), nullable=True)
    title = Column(String, nullable=True)


class UserAnalytics(Base):
    __tablename__ = 'analytics'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('user.id'))
    key = Column(String, nullable=False)
    time = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(String, primary_key=True)
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)


Base.metadata.create_all(engine)
