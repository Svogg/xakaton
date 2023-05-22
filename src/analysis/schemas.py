from datetime import datetime

from pydantic import BaseModel

from decimal import Decimal


class AbstractSchema(object):
    id: str

    class Config:
        orm_mode = True


class CitySchema(AbstractSchema, BaseModel):
    city_name: str
    rating: int
    timezone: str


class EventsAbstractSchema(AbstractSchema, object):
    start: datetime
    end: datetime
    price: Decimal


class EventSchema(AbstractSchema, EventsAbstractSchema, BaseModel):
    pass


class ExcursionSchema(AbstractSchema, EventsAbstractSchema, BaseModel):
    pass


class RestaurantSchema(AbstractSchema, BaseModel):
    name: str
    kitchen_type: str
    mean_price: float
