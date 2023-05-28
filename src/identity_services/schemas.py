from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    email: str | None
    disabled: bool | None


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    toke_username: str | None = None
    scopes: list[str] = []


class UserInDB(UserSchema):
    hashed_password: str
