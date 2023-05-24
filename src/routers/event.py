from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from xakaton.src.models import EventModel
from xakaton.src.database import get_async_session

router = APIRouter()


@router.get('/events')
async def get_all_events(session: AsyncSession = Depends(get_async_session)):
    query = select(EventModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/event/{id}')
async def get_one_event(id: str, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(EventModel).filter_by(id=id))
    return result.scalars().all()
