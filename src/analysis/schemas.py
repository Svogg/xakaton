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


class HotelSchema(BaseModel):
    id: str
    address: str
    geo_data: List[str]
    title: str


class RouteSchema(BaseModel):
    id: str
    title: str
    time: str


class RegionSchema(BaseModel):
    id: str
    title: str
    price_hotel: int


class TrackSchema(BaseModel):
    id: str
    region: str
    days_count: int
    description: str
    price: int
