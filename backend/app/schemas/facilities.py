from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class FacilityBase(BaseModel):
    """Base schema for facility data"""
    name: str
    location: str
    certifications: str
    doctor_info: str
    patient_reviews: str


class FacilityCreate(FacilityBase):
    """Schema for creating a new facility"""
    pass


class FacilityUpdate(BaseModel):
    """Schema for updating a facility"""
    name: Optional[str] = None
    location: Optional[str] = None
    certifications: Optional[str] = None
    doctor_info: Optional[str] = None
    patient_reviews: Optional[str] = None


class FacilityResponse(FacilityBase):
    """Schema for facility response"""
    uuid: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 