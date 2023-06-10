from fastapi import APIRouter, Depends
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session
from backend.entity_endpoints.models import RestaurantModel

router = APIRouter()

restaurant = RestaurantModel


@router.get('/restaurants')
async def get_all_restaurants(
        offset: int,
        session: AsyncSession = Depends(get_async_session)
):
    result = await restaurant.find_all(
        offset=offset,
        session=session
    )
    return result if len(result) else {
        'data': 'Oops... Nothing to show you :('
    }


@router.get('/restaurant/{id}')
async def get_one_restaurant(
        restaurant_id: str,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        result = await restaurant.find_one(
            entity_id=restaurant_id,
            session=session
        )
        return result
    except exc.NoResultFound:
        return {
            'data': 'Oops... Nothing to show you :('
        }
