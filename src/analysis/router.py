from typing import List
from time import time
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.analysis.models import CityModel
from src.database import get_async_session

router = APIRouter()


@router.get('/get_city')
async def get_city(session: AsyncSession = Depends(get_async_session)):
    query = select(CityModel)
    start = time()
    result = await session.execute(query)
    return {
        'time': time() - start,
        'data': result.scalars().all()
    }





