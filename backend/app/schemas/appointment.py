from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field

class AppointmentBase(BaseModel):
    """Base schema for appointment"""
    trainer_id: UUID
    client_id: UUID
    appointment_time: datetime

class AppointmentCreate(AppointmentBase):
    """Schema for creating an appointment"""
    pass

class AppointmentUpdate(BaseModel):
    """Schema for updating an appointment"""
    status: str

class AppointmentResponse(AppointmentBase):
    """Schema for appointment response"""
    uuid: UUID
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 