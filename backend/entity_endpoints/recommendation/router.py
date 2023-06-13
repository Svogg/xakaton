from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated
from database import get_async_session
from services.analytics import recommend_event, most_favour
from entity_endpoints.models import HotelModel, RestaurantModel, ExcursionModel, EventModel, DataMlModel
from identity_endpoints.logic import get_current_active_user
from identity_endpoints.schemas import UserInDB

router = APIRouter()


@router.get('/recommendations/{current_user}')
async def get_recommendations(
        username: str,
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
        buf, res = [], []
        for i in data_list:
            for entity in (HotelModel, RestaurantModel, ExcursionModel, EventModel):
                buf.append(await session.execute(select(entity).filter_by(id=i)))

        for item in buf:
            ans = item.scalars().first()
            if ans:
                res.append(ans)
            if len(res) > 9:
                break
        if username != current_user.username:
            raise HTTPException(status_code=403, detail="Don't have permission")
        return res


@router.post('/add_to_favour/{username}/{item_id}')
async def add_to_favour(
        username: str,
        current_user: Annotated[UserInDB, Depends(get_current_active_user)],
        item_id, session: AsyncSession = Depends(get_async_session)):
    if current_user:

        if username != current_user.username:
            raise HTTPException(status_code=403, detail="Don't have permission")
        id_row = select(DataMlModel)
        result = await session.execute(id_row)
        stmt = insert(DataMlModel).values(id=len(result.scalars().all()), item_id=item_id,
                                          username=current_user.username, bought=1)
        await session.execute(stmt)
        await session.commit()
        return {
            'status': 'success'
        }
