from typing import List, Optional
from uuid import UUID
from sqlmodel import Field, SQLModel, Relationship

from app.database.base.model import BaseModel, TimeStampMixin
from app.database.user.model import User

class Trainer(BaseModel, TimeStampMixin, table=True):
    """Trainer model"""
    user_id: UUID = Field(foreign_key="user.uuid", unique=True)
    biography: Optional[str] = None
    certifications: Optional[str] = None
    hourly_rate: Optional[float] = None
    specialties: Optional[str] = None  # Stored as comma-separated values
    location: Optional[str] = None 