from datetime import datetime
from typing import List

from pydantic import BaseModel

from decimal import Decimal


class CitySchema(BaseModel):
    id: str
    city_name: str
    rating: int
    timezone: str


class EventSchema(BaseModel):
    id: str
    start: datetime
    end: datetime
    price: Decimal


class ExcursionSchema(BaseModel):
    id: str
    start: datetime
    end: datetime
    price: Decimal


class RestaurantSchema(BaseModel):
    id: str
    name: str
    kitchen_type: List[str]
    mean_price: float
