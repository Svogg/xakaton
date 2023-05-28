from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status, Security
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.identity_services.schemas import TokenDataSchema, UserSchema, TokenSchema, UserInDB
from src.identity_services.logic import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, \
    get_current_active_user, get_current_user

router = APIRouter()


@router.post("/token", response_model=TokenSchema)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: AsyncSession = Depends(get_async_session)
):
    user = await authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=UserInDB)
async def read_users_me(
    current_user: Annotated[UserInDB, Depends()]
):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[UserInDB, Security(get_current_active_user, scopes=["items"])]
):
    return [{"item_id": "Foo", "owner": current_user.username}]
