from typing import List, Optional
from pydantic import EmailStr
from sqlmodel import Field, JSON

from app.database.base.model import BaseModel, TimeStampMixin

class Review(BaseModel):
    rating: int = Field(ge=1, le=5)  # Rating between 1 and 5
    comment: str

class Facility(BaseModel, TimeStampMixin, table=True):
    name: str = Field(index=True)
    location: str = Field(index=True)
    credentials: dict = Field(sa_type=JSON)
    contact_email: EmailStr
    reviews: Optional[List[Review]] = Field(default=[], sa_type=JSON) 