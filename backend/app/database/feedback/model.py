from typing import Optional
from uuid import UUID
from sqlmodel import Field, SQLModel

from app.database.base.model import BaseModel, TimeStampMixin

class Feedback(BaseModel, TimeStampMixin, table=True):
    """Feedback model"""
    appointment_id: UUID = Field(foreign_key="appointment.uuid")
    rating: int = Field(ge=1, le=5)  # Rating from 1 to 5
    comments: Optional[str] = None 