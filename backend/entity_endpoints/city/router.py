from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session
from backend.entity_endpoints.models import CityModel

router = APIRouter()

city = CityModel


@router.get('/city')
async def find_cities(
        session: AsyncSession = Depends(get_async_session)
):
    return await city.find_all(session)


@router.get('/city/{id}')
async def find_one_city(
        city_id: str,
        session: AsyncSession = Depends(get_async_session)
):
    return await city.find_one(city_id, session)
