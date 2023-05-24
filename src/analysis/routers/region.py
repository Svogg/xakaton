from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.analysis.models import RegionModel
from src.database import get_async_session

router = APIRouter()


@router.get('/regions')
async def get_all_regions(session: AsyncSession = Depends(get_async_session)):
    query = select(RegionModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/region/{id}')
async def get_one_region(id: str, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(RegionModel).filter_by(id=id))
    return result.scalars().all()
