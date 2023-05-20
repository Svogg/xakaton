from sqlalchemy import (
    Column, ForeignKey, Integer, String, Boolean, Float
)
from sqlalchemy.dialects.postgresql import DATE

from create_schemas import Base


# class


class Abstract(object):
    id = Column(String, primary_key=True)


class GeoData(Abstract, Base):
    __tablename__ = 'geo_data'
    center_distance = Column(Float)
    coordinates_length = Column(Float, nullable=False)
    coordinates_width = Column(Float, nullable=False)


class Country(Abstract, Base):
    __tablename__ = 'country'
    country_name = Column(String, nullable=False)


class City(Abstract, Base):
    __tablename__ = 'city'
    city_name = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    timezone = Column(String, nullable=False)
    geo_centre = Column(String, nullable=False)  # Надо подумать над типом данных
    geo_data_id = Column(String, ForeignKey('geo_data.id'))
    country_id = Column(String, ForeignKey('country.id'))


class EventsAbstract(object):
    city_id = Column(String, ForeignKey('city.id'))
    geo_data_id = Column(String, ForeignKey('geo_data.id'))
    event_start = Column(DATE, nullable=False)
    event_end = Column(DATE, nullable=False)
    event_price = Column(Float, nullable=True)


class Event(Abstract, EventsAbstract, Base):
    __tablename__ = 'event'
    event_price = Column(Float, nullable=True)


class Excursion(Abstract, EventsAbstract, Base):
    __tablename__ = 'excursion'
