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
    duration: str
    price: Decimal


class ExcursionSchema(BaseModel):
    id: str
    start: datetime
    end: datetime
    duration: str
    price: Decimal


class RestaurantSchema(BaseModel):
    id: str
    name: str
    kitchen_type: List[str]
    mean_price: float


class HotelSchema(BaseModel):
    id: str
    address: str
    stars: str
    geo_data: List[str]
    title: str
    list_services: List[str]


class RegionSchema(BaseModel):
    id: str
    title: str
    price_hotel: int


class AirPlaneTicketSchema(BaseModel):
    city_id: str
    target_city: str
    flight_start: datetime
    flight_end: datetime
    flight_price: float
    airline_name: str


class UserSchema(BaseModel):
    id: str
    email: str
    phone_number: str


class UserAnalyticsSchema(BaseModel):
    session: int
    user_id: str
    target_region: str
    current_city: str
    target_city: str
    airplane_ticket_to: str
    airplane_ticket_back: str
    target_hotel: str
    target_restaurant: str
    target_excursion: str
    bought: bool
