from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session
from backend.entity_endpoints.models import RegionModel

router = APIRouter()

region = RegionModel


@router.get('/regions')
async def find_regions(session: AsyncSession = Depends(get_async_session)):
    return await region.find_all(session)


@router.get('/region/{id}')
async def find_one_region(region_id: str, session: AsyncSession = Depends(get_async_session)):
    return await region.find_one(region_id, session)
