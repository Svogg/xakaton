from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from xakaton.src.models import TrackModel
from xakaton.src.database import get_async_session

router = APIRouter()


@router.get('/tracks')
async def get_all_tracks(session: AsyncSession = Depends(get_async_session)):
    query = select(TrackModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/track/{id}')
async def get_one_track(id: str, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(TrackModel).filter_by(id=id))
    return result.scalars().all()
