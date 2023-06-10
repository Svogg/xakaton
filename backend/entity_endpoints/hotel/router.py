from fastapi import APIRouter, Depends
from sqlalchemy import select, exc
from sqlalchemy.ext.asyncio import AsyncSession
from backend.entity_endpoints.models import HotelModel
from backend.database import get_async_session

router = APIRouter()
hotel = HotelModel


@router.get('/hotels')
async def find_hotels(
        offset: int,
        session: AsyncSession = Depends(get_async_session)
):
    result = await hotel.find_all(
        offset=offset,
        session=session
    )
    return result if len(result) else {
        'data': 'Oops... Nothing to show you :('
    }


@router.get('/hotel/{id}')
async def find_one_hotel(
        hotel_id: str,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        result = await hotel.find_one(
            entity_id=hotel_id,
            session=session
        )
        return result
    except exc.NoResultFound:
        return {
            'data': 'Oops... Nothing to show you :('
        }
