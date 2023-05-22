from datetime import datetime

from pydantic import BaseModel

from decimal import Decimal


class Abstract(object):
    id: int

    class Config:
        orm_mode = True


class GeoData(Abstract, BaseModel):
    center_distance: float
    coordinates_length: float
    coordinates_width: float


class Country(Abstract, BaseModel):
    country_name: str


class City(Abstract, BaseModel):
    city_name: str
    rating: int
    timezone: str
    geo_centre: str  # Надо подумать над типом данных
    geo_data_id: str
    country_id: str


class CityAbstract(object):
    city_id: str
    geo_data_id: str


class EventsAbstract(CityAbstract, object):
    start: datetime
    end: datetime
    price: Decimal


class Event(Abstract, EventsAbstract, BaseModel):
    pass


class Excursion(Abstract, EventsAbstract, BaseModel):
    pass


class Restaurant(Abstract, CityAbstract, BaseModel):
    name: str
    kitchen_type: str
    mean_price: float
