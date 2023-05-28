from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.identity_services.logic import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from src.identity_services.schemas import TokenSchema

router = APIRouter()


@router.post("/token", response_model=TokenSchema)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: AsyncSession = Depends(get_async_session)
):
    user = await authenticate_user(
        username=form_data.username, password=form_data.password, session=session)
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
