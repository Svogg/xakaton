from sqlalchemy import (
    Column, ForeignKey, Integer, String, Boolean, Float, ARRAY
)
from sqlalchemy.dialects.postgresql import DATE

from create_schemas import Base, engine


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


# class Hotel(_GeoAbstract, Base):            в работе
#     __tablename__ = 'hotel'
#     address = Column(String, nullable=True)


class Event(_Abstract, _EventsAbstract, Base):
    __tablename__ = 'event'


class Excursion(_GeoAbstract, _EventsAbstract, Base):
    __tablename__ = 'excursion'


class Restaurant(_GeoAbstract, _CityAbstract, Base):
    __tablename__ = 'restaurant'
    name = Column(String, nullable=True)
    kitchen_type = Column(ARRAY(String), nullable=True)
    mean_price = Column(Float, nullable=True)


Base.metadata.create_all(engine)
