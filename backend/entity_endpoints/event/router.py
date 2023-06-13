from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from entity_endpoints.models import EventModel

router = APIRouter()

event = EventModel


@router.get('/events')
async def find_events(
        offset: int,
        start: Annotated[str, None] = None,
        end: Annotated[str, None] = None,
        duration: Annotated[str, None] = None,
        session: AsyncSession = Depends(get_async_session)
):
    return await event.find_all(offset=offset, session=session)


@router.get('/event/{id}')
async def find_one_event(
        event_id: str,
        session: AsyncSession = Depends(get_async_session)
):
    return await event.find_one(event_id, session)
