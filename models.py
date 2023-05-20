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


class CityAbstract(object):
    city_id = Column(String, ForeignKey('city.id'))
    geo_data_id = Column(String, ForeignKey('geo_data.id'))


class EventsAbstract(CityAbstract, object):
    start = Column(DATE, nullable=False)
    end = Column(DATE, nullable=False)
    price = Column(Float, nullable=True)


class Event(Abstract, EventsAbstract, Base):
    __tablename__ = 'event'


class Excursion(Abstract, EventsAbstract, Base):
    __tablename__ = 'excursion'


class Restaurant(Abstract, CityAbstract, Base):
    __tablename__ = 'restaurant'
    name = Column(String, nullable=False)
    kitchen_type = Column(String, nullable=False)
    mean_price = Column(Float, nullable=False)
