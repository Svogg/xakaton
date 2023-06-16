from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_async_session
from entity_endpoints.models import RestaurantModel

router = APIRouter()


@router.get('/restaurants')
async def get_all_restaurants(session: AsyncSession = Depends(get_async_session)):
    query = select(RestaurantModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/restaurant/{id}')
async def get_one_restaurant(id: str, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(RestaurantModel).filter_by(id=id))
    return result.scalars().all()
