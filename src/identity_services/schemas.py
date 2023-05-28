from pydantic import BaseModel, SecretStr


class UserSchema(BaseModel):
    username: str
    email: str | None
    disabled: bool | None


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    username: str | None = None


class UserInDB(UserSchema):
    hashed_password: SecretStr
