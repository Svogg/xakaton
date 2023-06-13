from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from entity_endpoints.models import RestaurantModel

router = APIRouter()

restaurant = RestaurantModel


@router.get('/restaurants')
async def get_all_restaurants(session: AsyncSession = Depends(get_async_session)):
    return await restaurant.find_all(session)


@router.get('/restaurant/{id}')
async def get_one_restaurant(restaurant_id: str, session: AsyncSession = Depends(get_async_session)):
    return await restaurant.find_one(restaurant_id, session)
