from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from xakaton.src.models import CityModel
from xakaton.src.database import get_async_session

router = APIRouter()


@router.get('/cities')
async def get_all_cities(session: AsyncSession = Depends(get_async_session)):
    query = select(CityModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/city/{id}')
async def get_one_city(id: str, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(CityModel).filter_by(id=id))
    return result.scalars().all()
