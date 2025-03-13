from typing import List, Optional
from uuid import UUID
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.availability.model import Availability

class AvailabilityService(BaseService):
    """Availability service"""

    async def get_by_uuid(self, uuid: UUID) -> Optional[Availability]:
        """Get availability by UUID"""
        query = select(Availability).where(Availability.uuid == uuid)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_trainer_id(self, trainer_id: UUID) -> List[Availability]:
        """Get availability by trainer ID"""
        query = select(Availability).where(Availability.trainer_id == trainer_id)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def create(self, availability: Availability) -> Availability:
        """Create new availability"""
        await availability.save(self.db_session)
        return availability

    async def update(self, availability: Availability, **kwargs) -> Availability:
        """Update availability"""
        await availability.update(self.db_session, **kwargs)
        return availability

    async def delete(self, availability: Availability) -> None:
        """Delete availability"""
        await availability.delete(self.db_session)
        
    async def delete_by_trainer_id(self, trainer_id: UUID) -> None:
        """Delete all availability slots for a trainer"""
        query = select(Availability).where(Availability.trainer_id == trainer_id)
        result = await self.db_session.execute(query)
        availabilities = result.scalars().all()
        
        for availability in availabilities:
            await availability.delete(self.db_session) 