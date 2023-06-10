from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated

from backend.database import get_async_session
from backend.entity_endpoints.models import HotelModel, RestaurantModel, ExcursionModel, EventModel, DataMlModel
from backend.identity_endpoints.logic import get_current_active_user
from backend.identity_endpoints.schemas import UserInDB
from backend.services.analytics import recommend_event, most_favour

router = APIRouter()


@router.get('/recommendations/{username}')
async def get_recommendations(
        username: str,
        current_user: Annotated[UserInDB, Depends(get_current_active_user)],
        recommendation_filter: str | None = None,
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
            buf_dict = {}
            for entity in (HotelModel, RestaurantModel, ExcursionModel, EventModel):
                element = await session.execute(select(entity).filter_by(id=i))
                buf_dict.update({entity.__tablename__: element.scalars().first()})
            buf.append(buf_dict)

        result = []
        for entity in buf:
            obj = []
            for k, v in entity.items():
                ans = {k: v if v else 'empty'}
                if len(list(ans.values())):
                    obj.append(ans)

            result.append(obj)
            if len(result) > 9:
                break

        if username != current_user.username:
            raise HTTPException(status_code=403, detail="Unauthorized")

        if recommendation_filter is None:
            return result
        return [[item for item in pack if item.get(recommendation_filter)][0] for pack in result]


@router.post('/add_to_favour/{username}/{item_id}')
async def add_to_favour(
        username: str,
        current_user: Annotated[UserInDB, Depends(get_current_active_user)],
        item_id, session: AsyncSession = Depends(get_async_session)):
    if current_user:

        if username != current_user.username:
            raise HTTPException(status_code=403, detail="Unauthorized")
        id_row = select(DataMlModel)
        result = await session.execute(id_row)
        stmt = insert(DataMlModel).values(
            id=len(result.scalars().all()),
            item_id=item_id,
            username=current_user.username, bought=1
        )
        await session.execute(stmt)
        await session.commit()
        return {
            'status': 'success'
        }
