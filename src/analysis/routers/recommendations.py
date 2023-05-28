from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.analysis.services.analytics import recommend_event
from xakaton.src.database import get_async_session
from src.analysis.models import HotelModel, RestaurantModel, ExcursionModel, EventModel

router = APIRouter()


@router.get('/recommendations/{user_id}')
async def get_recommendations(user_id, session: AsyncSession = Depends(get_async_session)):
    rec = recommend_event(user_id)
    buf = []
    res = []
    for id in rec:
        buf.append(await session.execute(select(HotelModel).filter_by(id=id)))
        buf.append(await session.execute(select(RestaurantModel).filter_by(id=id)))
        buf.append(await session.execute(select(ExcursionModel).filter_by(id=id)))
        buf.append(await session.execute(select(EventModel).filter_by(id=id)))
    for item in buf:
        ans = item.scalars().all()
        if ans:
            res.append(ans)
    return [i for i in res]
