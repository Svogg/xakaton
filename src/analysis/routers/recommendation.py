from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.analytics import recommend_event
from typing_extensions import Annotated
from xakaton.src.database import get_async_session
from src.analysis.models import HotelModel, RestaurantModel, ExcursionModel, EventModel, DataMlModel
from xakaton.src.identity_services.logic import get_current_active_user
from xakaton.src.identity_services.schemas import UserInDB

router = APIRouter()


@router.get('/recommendations/{user_id}')
async def get_recommendations(current_user: Annotated[UserInDB, Depends(get_current_active_user)],
                              session: AsyncSession = Depends(get_async_session)):
    if current_user:
        query = await session.execute(select(DataMlModel))
        data = [[i.item_id, i.username, i.bought] for i in query.scalars().all()]
        # print(data)
        rec = await recommend_event(current_user.username, data)
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


@router.post('/add_to_favour/{username}')
async def add_to_favour(current_user: Annotated[UserInDB, Depends(get_current_active_user)],
                        item_id, session: AsyncSession = Depends(get_async_session)):
    if current_user:
        id_row = select(DataMlModel)
        result = await session.execute(id_row)
        stmt = insert(DataMlModel).values(id=len(result.scalars().all()), item_id=item_id,
                                          username=current_user.username, bought=1)
        await session.execute(stmt)
        await session.commit()
        return {
            'status': 'success'
        }
