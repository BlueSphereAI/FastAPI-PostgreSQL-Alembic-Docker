from typing import Optional, List
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field

class AvailabilityBase(BaseModel):
    """Base schema for availability"""
    start_time: datetime
    end_time: datetime
    is_available: bool = True

class AvailabilityCreate(AvailabilityBase):
    """Schema for creating availability"""
    trainer_id: UUID

class AvailabilityResponse(AvailabilityBase):
    """Schema for availability response"""
    uuid: UUID
    trainer_id: UUID

    class Config:
        from_attributes = True

class AvailabilitySlot(BaseModel):
    """Schema for availability slot"""
    start_time: datetime
    end_time: datetime
    is_available: bool

class AvailabilityUpdate(BaseModel):
    """Schema for updating availability"""
    availability_slots: List[AvailabilitySlot] 