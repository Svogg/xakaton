from time import time
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import CityModel, EventModel, ExcursionModel, RestaurantModel, HotelModel, RegionModel, RouteModel, TrackModel
from ..database import get_async_session

router = APIRouter()


@router.get('/cities')
async def get_city(session: AsyncSession = Depends(get_async_session)):
    query = select(CityModel)
    start = time()
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/regions')
async def get_region(session: AsyncSession = Depends(get_async_session)):
    query = select(RegionModel)
    start = time()
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/events')
async def get_event(session: AsyncSession = Depends(get_async_session)):
    query = select(EventModel)
    start = time()
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/hotels')
async def get_hotel(session: AsyncSession = Depends(get_async_session)):
    query = select(HotelModel)
    start = time()
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/excursions')
async def get_excursion(session: AsyncSession = Depends(get_async_session)):
    query = select(ExcursionModel)
    start = time()
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/restaurants')
async def get_restaurant(session: AsyncSession = Depends(get_async_session)):
    query = select(RestaurantModel)
    start = time()
    result = await session.execute(query)
    return result.scalars().all()

@router.get('/routes')
async def get_route(session: AsyncSession = Depends(get_async_session)):
    query = select(RouteModel)
    start = time()
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/tracks')
async def get_track(session: AsyncSession = Depends(get_async_session)):
    query = select(TrackModel)
    start = time()
    result = await session.execute(query)
    return result.scalars().all()
