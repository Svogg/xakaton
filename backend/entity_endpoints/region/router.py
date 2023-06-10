from fastapi import APIRouter, Depends
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session
from backend.entity_endpoints.models import RegionModel

router = APIRouter()

region = RegionModel


@router.get('/regions')
async def find_regions(
        offset: int,
        session: AsyncSession = Depends(get_async_session)
):
    result = await region.find_all(
        offset=offset,
        session=session
    )
    return result if len(result) else {
        'data': 'Oops... Nothing to show you :('
    }


@router.get('/region/{id}')
async def find_one_region(
        region_id: str,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        result = await region.find_one(
            entity_id=region_id,
            session=session
        )
        return result
    except exc.NoResultFound:
        return {
            'data': 'Oops... Nothing to show you :('
        }
