from passlib.context import CryptContext
from pydantic import EmailStr
from sqlmodel import Field

from app.database.base.model import BaseModel, TimeStampMixin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel, TimeStampMixin, table=True):
    username: str = Field(unique=True, index=True)
    email: EmailStr = Field(unique=True, index=True)
    password_hash: str = Field()

    def set_password(self, password: str):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash) 