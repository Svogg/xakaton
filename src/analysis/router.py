import json

from src.database import get_async_session
from fastapi import APIRouter, Depends
from psycopg2 import errors
from sqlalchemy import exc
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.analysis.models import CityModel, EventModel, ExcursionModel, RestaurantModel, HotelModel, RegionModel, RouteModel, TrackModel
from src.analysis.schemas import CitySchema, EventSchema, ExcursionSchema, RestaurantSchema

router = APIRouter()



