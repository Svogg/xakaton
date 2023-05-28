from fastapi import APIRouter
from fastapi import Depends
from pydantic import SecretStr
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import count

from src.identity_services.logic import pwd_context
from src.identity_services.models import UserModel
from src.identity_services.schemas import UserSchema
from src.database import get_async_session

router = APIRouter()


@router.post("/register", response_model=UserSchema)
async def register(
        username: str,
        email: str,
        hashed_password: SecretStr,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        user = UserSchema(username=username, email=email, hashed_password=hashed_password)

        id_row = select(UserModel)
        result = await session.execute(id_row)
        query = insert(UserModel).values(
            id=len(result.scalars().all()),
            username=user.username,
            email=user.email,
            hashed_password=pwd_context.hash(user.hashed_password.get_secret_value()),
            disabled=False
        ).on_conflict_do_nothing()
        await session.execute(query)
        await session.commit()
        return dict(**user.dict())
    except IntegrityError as e:
        await session.rollback()
        return {
            'status': e
        }
