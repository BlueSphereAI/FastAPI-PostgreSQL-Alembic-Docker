from typing import Optional, ClassVar
from uuid import UUID
from sqlmodel import Field, SQLModel
from passlib.context import CryptContext

from app.database.base.model import BaseModel, TimeStampMixin

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserType(SQLModel, table=False):
    """User type enum"""
    TRAINER: ClassVar[str] = "trainer"
    CLIENT: ClassVar[str] = "client"

class User(BaseModel, TimeStampMixin, table=True):
    """User model"""
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    password_hash: str
    first_name: str
    last_name: str
    user_type: str  # Either 'trainer' or 'client'

    @classmethod
    def create_password_hash(cls, password: str) -> str:
        """Create a password hash"""
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str) -> bool:
        """Verify a password against the hash"""
        return pwd_context.verify(plain_password, self.password_hash) 