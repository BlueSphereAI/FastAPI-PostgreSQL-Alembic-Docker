from typing import Optional, ClassVar
from uuid import UUID
from datetime import datetime
from sqlmodel import Field, SQLModel

from app.database.base.model import BaseModel, TimeStampMixin

class AppointmentStatus(SQLModel, table=False):
    """Appointment status enum"""
    SCHEDULED: ClassVar[str] = "Scheduled"
    COMPLETED: ClassVar[str] = "Completed"
    CANCELLED: ClassVar[str] = "Cancelled"

class Appointment(BaseModel, TimeStampMixin, table=True):
    """Appointment model"""
    trainer_id: UUID = Field(foreign_key="user.uuid")
    client_id: UUID = Field(foreign_key="user.uuid")
    appointment_time: datetime
    status: str = Field(default=AppointmentStatus.SCHEDULED) 