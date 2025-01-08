from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.database.bookings.model import BookingStatus


class BookingBase(BaseModel):
    """Base schema for booking data"""
    user_id: UUID
    facility_id: UUID
    procedure_id: UUID
    itinerary: str
    status: BookingStatus = BookingStatus.PENDING


class BookingCreate(BookingBase):
    """Schema for creating a new booking"""
    pass


class BookingUpdate(BaseModel):
    """Schema for updating a booking"""
    itinerary: Optional[str] = None
    status: Optional[BookingStatus] = None


class BookingResponse(BookingBase):
    """Schema for booking response"""
    uuid: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 