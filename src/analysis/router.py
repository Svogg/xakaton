from time import time

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.analysis.models import CityModel
from src.database import get_async_session

router = APIRouter()


@router.get('/get_city')
async def get_city(session: AsyncSession = Depends(get_async_session)):
    stmt = select(CityModel)
    start = time()
    result = await session.execute(stmt)
    return {
        'time': time() - start,
        'data': result.scalars().all()
    }





