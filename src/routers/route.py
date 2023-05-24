from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from xakaton.src.models import RouteModel
from xakaton.src.database import get_async_session

router = APIRouter()


@router.get('/routes')
async def get_all_routes(session: AsyncSession = Depends(get_async_session)):
    query = select(RouteModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/route/{id}')
async def get_one_route(id: str, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(RouteModel).filter_by(id=id))
    return result.scalars().all()
