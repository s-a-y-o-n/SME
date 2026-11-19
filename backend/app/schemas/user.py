
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Literal
from datetime import datetime


class UserCreate(BaseModel):

    full_name: str = Field(
        min_length=2,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128
    )


class UserResponse(BaseModel):

    id: int
    full_name: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):

    access_token: str
    token_type: str = "bearer"


class LoginResponse(BaseModel):

    access_token: str
    token_type: str = "bearer"
    user: UserResponse
