from typing import List, Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.bookings.model import Booking, BookingStatus


class BookingService(BaseService):
    """
    Service for handling Booking-related operations
    """
    
    async def create(
        self,
        user_id: UUID,
        facility_id: UUID,
        procedure_id: UUID,
        itinerary: str,
        status: BookingStatus = BookingStatus.PENDING
    ) -> Booking:
        """Create a new booking"""
        booking = Booking(
            user_id=user_id,
            facility_id=facility_id,
            procedure_id=procedure_id,
            itinerary=itinerary,
            status=status
        )
        await booking.save(self.db_session)
        return booking
    
    async def get_by_id(self, uuid: UUID) -> Optional[Booking]:
        """Get a booking by its ID"""
        query = select(Booking).where(Booking.uuid == uuid)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()
    
    async def get_all(self) -> List[Booking]:
        """Get all bookings"""
        query = select(Booking)
        result = await self.db_session.execute(query)
        return result.scalars().all()
    
    async def get_user_bookings(self, user_id: UUID) -> List[Booking]:
        """Get all bookings for a specific user"""
        query = select(Booking).where(Booking.user_id == user_id)
        result = await self.db_session.execute(query)
        return result.scalars().all()
    
    async def update(
        self,
        uuid: UUID,
        itinerary: Optional[str] = None,
        status: Optional[BookingStatus] = None
    ) -> Optional[Booking]:
        """Update a booking"""
        booking = await self.get_by_id(uuid)
        if not booking:
            return None
            
        update_data = {}
        if itinerary is not None:
            update_data["itinerary"] = itinerary
        if status is not None:
            update_data["status"] = status
            
        await booking.update(self.db_session, **update_data)
        return booking
    
    async def delete(self, uuid: UUID) -> bool:
        """Delete a booking"""
        booking = await self.get_by_id(uuid)
        if not booking:
            return False
            
        await booking.delete(self.db_session)
        return True 