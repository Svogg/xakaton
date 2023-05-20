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
    
class Track(_Abstract, Base):
    __tablename__ = 'track'
    city = Column(String, ForeignKey('city.id'))
    region = Column(String, ForeignKey('reqion.id'))
    days_count = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)


class Region(_Abstract, Base):
    __tablename__ = 'region'
    title = Column(String, nullable=False)
    price_hotel = Column(Integer, nullable=False)


class Route(_Abstract, Base):
    __tablename__ = 'route'
    title = Column(String, nullable=False)
    time = Column(String, nullable=False)
    is_can_buy = Column(Boolean, nullable=False)
    region = Column(String, ForeignKey('reqion.id'))


class Hotel(_Abstract, Base):
    __tablename__ = 'hotel'
    address = title = Column(String, nullable=False)
    geo_data = Column(ARRAY(Float), nullable=True)
    city = Column(String, ForeignKey('city.id'))
    title = Column(String, nullable=False)



Base.metadata.create_all(engine)

