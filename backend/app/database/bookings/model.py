from typing import Optional
from uuid import UUID
from enum import Enum

from sqlmodel import Field, Relationship

from app.database.base.model import BaseModel, TimeStampMixin
from app.database.procedures.model import Procedure
from app.database.facilities.model import Facility


class BookingStatus(str, Enum):
    """Enum for booking status"""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class Booking(BaseModel, TimeStampMixin, table=True):
    """
    Booking Model
    
    Attributes:
        user_id (UUID): ID of the user making the booking
        facility_id (UUID): ID of the selected facility
        procedure_id (UUID): ID of the selected procedure
        itinerary (str): Travel and accommodation details
        status (BookingStatus): Current status of the booking
    """
    
    user_id: UUID = Field(index=True)
    facility_id: UUID = Field(foreign_key="facility.uuid")
    procedure_id: UUID = Field(foreign_key="procedure.uuid")
    itinerary: str
    status: BookingStatus = Field(default=BookingStatus.PENDING)

    # Relationships
    facility: Optional[Facility] = Relationship(back_populates="bookings")
    procedure: Optional[Procedure] = Relationship(back_populates="bookings") 