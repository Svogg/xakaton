from time import time
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.identity_services.logic import get_current_active_user
from src.identity_services.schemas import UserInDB
from src.analysis.models import CityModel
from src.database import get_async_session

router = APIRouter()


@router.get('/get_city')
async def get_city(
        current_user: Annotated[UserInDB, Depends(get_current_active_user)],
        session: AsyncSession = Depends(get_async_session),

):
    start = time()
    if current_user:
        stmt = select(CityModel)

        result = await session.execute(stmt)
        return {
            'time': time() - start,
            'data': result.scalars().all()
        }





