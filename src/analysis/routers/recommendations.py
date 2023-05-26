from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.analysis.services.analytics import recommend_event
from src.database import get_async_session
from src.analysis.models import UserModel

router = APIRouter()


@router.get('/recommendations')
async def get_recommendations(id, session: AsyncSession = Depends(get_async_session)):
    """параметр id принадлежит авторизованному пользователю"""
    recommends = await recommend_event(id)  # список id рекомендуемых объектов
    result = 0
    return result.scalars().all()
