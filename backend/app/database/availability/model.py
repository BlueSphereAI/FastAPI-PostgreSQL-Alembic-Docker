from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import Field, SQLModel

from app.database.base.model import BaseModel, TimeStampMixin

class Availability(BaseModel, TimeStampMixin, table=True):
    """Availability model"""
    trainer_id: UUID = Field(foreign_key="user.uuid")
    start_time: datetime
    end_time: datetime
    is_available: bool = True 