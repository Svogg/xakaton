from fastapi import APIRouter, Depends
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session
from backend.entity_endpoints.models import CityModel

router = APIRouter()

city = CityModel


@router.get('/city')
async def find_cities(
        offset: int,
        session: AsyncSession = Depends(get_async_session)
):
    result = await city.find_all(
        offset=offset,
        session=session
    )
    return result if len(result) else {
        'data': 'Oops... Nothing to show you :('
    }


@router.get('/city/{id}')
async def find_one_city(
        city_id: str,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        result = await city.find_one(
            entity_id=city_id,
            session=session
        )
        return result
    except exc.NoResultFound:
        return {
            'data': 'Oops... Nothing to show you :('
        }
