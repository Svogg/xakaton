from typing import Optional, Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from entity_endpoints.models import CityModel

router = APIRouter()

city = CityModel


@router.get('/city')
async def find_cities(
        offset: int,
        rating: Annotated[float, None] = None,
        session: AsyncSession = Depends(get_async_session)
):
    if rating is not None:
        result = await city.find_all(
            offset=offset,
            rating=rating,
            session=session,

        )
        if len(result):
            return result
        else:
            return {
                'data': 'Oops... Nothing to show you :('
            }
    else:
        result = await city.find_all(
            offset=offset,
            session=session
        )
        if len(result):
            return result
        else:
            return {
                'data': 'Oops... Nothing to show you :('
            }


@router.get('/city/{id}')
async def find_one_city(
        city_id: str,
        session: AsyncSession = Depends(get_async_session)
):
    result = await city.find_one(
        id=city_id,
        session=session
    )
    if len(result):
        return result
    else:
        return {
            'data': 'Oops... Nothing to show you :('
        }
