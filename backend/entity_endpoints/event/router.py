from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session
from backend.entity_endpoints.models import EventModel

router = APIRouter()

event = EventModel


@router.get('/events')
async def find_events(session: AsyncSession = Depends(get_async_session)):
    return await event.find_all(session)


@router.get('/event/{id}')
async def find_one_event(event_id: str, session: AsyncSession = Depends(get_async_session)):
    return await event.find_one(event_id, session)
