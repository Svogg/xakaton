from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.identity_services.logic import pwd_context
from src.identity_services.models import UserModel
from src.identity_services.schemas import UserInDB

router = APIRouter()


@router.post("/register", response_model=UserInDB)
async def register(
        username: str,
        email: str,
        hashed_password: str,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        id_row = select(UserModel)
        result = await session.execute(id_row)
        query = insert(UserModel).values(
            id=len(result.scalars().all()),
            username=username,
            email=email,
            hashed_password=pwd_context.hash(hashed_password),
            disabled=False
        ).on_conflict_do_nothing()
        user = UserInDB(username=username, email=email, hashed_password='***********************')
        await session.execute(query)
        await session.commit()
        return dict(**user.dict())
    except IntegrityError as e:
        await session.rollback()
        return {
            'status': e
        }
