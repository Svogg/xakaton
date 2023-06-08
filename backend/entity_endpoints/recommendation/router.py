from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.analytics import recommend_event, most_favour
from typing_extensions import Annotated
from backend.database import get_async_session
from backend.entity_endpoints.models import HotelModel, RestaurantModel, ExcursionModel, EventModel, DataMlModel
from backend.identity_endpoints.logic import get_current_active_user
from backend.identity_endpoints.schemas import UserInDB

router = APIRouter()


@router.get('/recommendations/{id}')
async def get_recommendations(
        current_user: Annotated[UserInDB, Depends(get_current_active_user)],
        session: AsyncSession = Depends(get_async_session)
):
    if current_user:
        data = await session.execute(select(DataMlModel))
        result = data.scalars().all()
        new_res = [
            dict(
                item_id=res.item_id,
                username=res.username,
                bought=res.bought
            ) for res in result
        ]
        most_val = most_favour(new_res)
        rec = await recommend_event(list_dict=new_res, username=current_user.username)
        data_list = []
        for el in rec:
            data_list.append(
                (await session.execute(select(DataMlModel).filter_by(id=el))).scalars().all()[0].item_id
            )
        for el in most_val:
            if el not in data_list:
                data_list.append(el)
        buf = []
        res = []
        for i in data_list:
            buf.append(await session.execute(select(HotelModel).filter_by(id=i)))
            buf.append(await session.execute(select(RestaurantModel).filter_by(id=i)))
            buf.append(await session.execute(select(ExcursionModel).filter_by(id=i)))
            buf.append(await session.execute(select(EventModel).filter_by(id=i)))

        for item in buf:
            ans = item.scalars().all()
            if ans:
                res.append(ans)
            if len(ans) > 9:
                break
        return res


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
