from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import Field, SQLModel

from app.database.base.model import BaseModel, TimeStampMixin


class User(BaseModel, TimeStampMixin, table=True):
    """
    User model for authentication
    """
    username: str = Field(unique=True, index=True)
    password_hash: str
    last_login: Optional[datetime] = Field(default=None, nullable=True)


class UserCreate(SQLModel):
    """
    Schema for user creation
    """
    username: str
    password: str


class UserRead(SQLModel):
    """
    Schema for user response
    """
    uuid: UUID
    username: str
    created_at: datetime
    last_login: Optional[datetime] = None 