from datetime import timedelta, datetime
from typing import Annotated

from fastapi import HTTPException, Depends
from fastapi import status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.config import SECRET_KEY
from backend.database import get_async_session
from backend.identity_endpoints.models import UserModel
from backend.identity_endpoints.schemas import TokenDataSchema, UserInDB


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/identity/login",
)

SECRET_KEY = SECRET_KEY
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


async def get_user(
        username: str,
        password: str = None,
        token_data: str = None,
        session: AsyncSession = Depends(get_async_session)
):
    if not token_data:
        stmt = select(UserModel).filter_by(username=username)
        result = await session.execute(stmt)
        result_dict = result.scalars().all()[0].__dict__
        if result_dict:
            user_dict = {
                'username': result_dict.get('username'),
                'email': result_dict.get('email'),
                'disabled': result_dict.get('disabled'),
                'hashed_password': result_dict.get('hashed_password'),
            }

            return UserInDB(**user_dict)
    else:
        stmt = select(UserModel).filter_by(username=token_data)
        result = await session.execute(stmt)
        result_dict = result.scalars().all()[0].__dict__
        if result_dict:
            user_dict = {
                'username': result_dict.get('username'),
                'email': result_dict.get('email'),
                'disabled': result_dict.get('disabled'),
                'hashed_password': result_dict.get('hashed_password'),
            }

            return UserInDB(**user_dict)


async def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate_user(
        username: str,
        password: str,
        token: str = None,
        session: AsyncSession = Depends(get_async_session)):
    user = await get_user(username=username, token_data=token, session=session)
    if not user:
        return False
    if not await verify_password(password, user.hashed_password):
        return False
    return user


async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
        security_scopes: SecurityScopes,
        token: Annotated[str, Depends(oauth2_scheme)],
        session: AsyncSession = Depends(get_async_session)
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenDataSchema(username=username)
    except JWTError:
        raise credentials_exception
    user = await get_user(username=username, token_data=token_data.toke_username, session=session)
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user


async def get_current_active_user(
        current_user: Annotated[UserModel, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
