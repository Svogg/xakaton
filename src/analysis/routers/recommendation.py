from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.analytics import recommend_event
from typing_extensions import Annotated
from src.database import get_async_session
from src.analysis.models import HotelModel, RestaurantModel, ExcursionModel, EventModel, DataMlModel
from src.identity_services.logic import get_current_active_user
from src.identity_services.schemas import UserInDB

router = APIRouter()


@router.get('/recommendations/{id}')
async def get_recommendations(current_user: Annotated[UserInDB, Depends(get_current_active_user)],
                              session: AsyncSession = Depends(get_async_session)):
    if current_user:
        last_choice = select(DataMlModel).filter_by(username=current_user.username).order_by(DataMlModel.id.desc())
        new_data = await session.execute(last_choice)
        item_id = new_data.scalars().all()[0].item_id
        data = await session.execute(select(DataMlModel))
        result = data.scalars().all()
        new_res = [
            dict(
                item_id=res.item_id,
                username=res.username,
                bought=res.bought
            ) for res in result
        ]
        rec = await recommend_event(list_dict=new_res, username=current_user.username, item_id=item_id)
        data_list = []
        for el in rec:
            data_list.append(
            (
                await session.execute(select(DataMlModel).filter_by(id=el))
            ).scalars().all()[0].item_id
            )
        buf = []
        res = []

        for id in data_list:
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
