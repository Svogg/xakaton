from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from entity_endpoints.models import HotelModel
from database import get_async_session

router = APIRouter()


@router.get('/hotels')
async def get_all_hotels(session: AsyncSession = Depends(get_async_session)):
    query = select(HotelModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/hotel/{id}')
async def get_one_hotel(id: str, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(HotelModel).filter_by(id=id))
    return result.scalars().all()
