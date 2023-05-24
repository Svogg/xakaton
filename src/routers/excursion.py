from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from xakaton.src.models import ExcursionModel
from xakaton.src.database import get_async_session

router = APIRouter()


@router.get('/excursions')
async def get_all_excursions(session: AsyncSession = Depends(get_async_session)):
    query = select(ExcursionModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/excursion/{id}')
async def get_one_excursion(id: str, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(ExcursionModel).filter_by(id=id))
    return result.scalars().all()
