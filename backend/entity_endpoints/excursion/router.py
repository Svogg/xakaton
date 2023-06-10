from fastapi import APIRouter, Depends
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session
from backend.entity_endpoints.models import ExcursionModel

router = APIRouter()

excursion = ExcursionModel


@router.get('/excursions')
async def find_excursions(
        offset: int,
        session: AsyncSession = Depends(get_async_session)
):
    result = await excursion.find_all(
        offset=offset,
        session=session
    )
    return result if len(result) else {
        'data': 'Oops... Nothing to show you :('
    }


@router.get('/excursion/{id}')
async def find_one_excursion(
        excursion_id: str,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        result = await excursion.find_one(
            entity_id=excursion_id,
            session=session
        )
        return result
    except exc.NoResultFound:
        return {
            'data': 'Oops... Nothing to show you :('
        }
