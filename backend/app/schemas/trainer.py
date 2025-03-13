from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field

class TrainerBase(BaseModel):
    """Base schema for trainer"""
    biography: Optional[str] = None
    certifications: Optional[str] = None
    hourly_rate: Optional[float] = None
    specialties: Optional[str] = None
    location: Optional[str] = None

class TrainerCreate(TrainerBase):
    """Schema for creating a trainer"""
    user_id: UUID

class TrainerUpdate(TrainerBase):
    """Schema for updating a trainer"""
    pass

class TrainerResponse(TrainerBase):
    """Schema for trainer response"""
    uuid: UUID
    user_id: UUID

    class Config:
        from_attributes = True 