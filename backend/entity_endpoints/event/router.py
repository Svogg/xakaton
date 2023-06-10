from fastapi import APIRouter, Depends
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session
from backend.entity_endpoints.models import EventModel

router = APIRouter()

event = EventModel


@router.get('/events')
async def find_events(
        offset: int,
        session: AsyncSession = Depends(get_async_session)
):
    result = await event.find_all(
        offset=offset,
        session=session
    )
    return result if len(result) else {
        'data': 'Oops... Nothing to show you :('
    }


@router.get('/event/{id}')
async def find_one_event(
        event_id: str,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        result = await event.find_one(
            entity_id=event_id,
            session=session
        )
        return result
    except exc.NoResultFound:
        return {
            'data': 'Oops... Nothing to show you :('
        }
