from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session
from backend.entity_endpoints.models import ExcursionModel

router = APIRouter()

excursion = ExcursionModel


@router.get('/excursions')
async def find_excursions(session: AsyncSession = Depends(get_async_session)):
    return await excursion.find_all(session)


@router.get('/excursion/{id}')
async def find_one_excursion(excursion_id: str, session: AsyncSession = Depends(get_async_session)):
    return await excursion.find_one(excursion_id, session)
