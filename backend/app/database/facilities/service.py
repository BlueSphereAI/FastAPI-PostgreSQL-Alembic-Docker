from typing import List, Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.facilities.model import Facility


class FacilityService(BaseService):
    """
    Service for handling Facility-related operations
    """
    
    async def create(
        self,
        name: str,
        location: str,
        certifications: str,
        doctor_info: str,
        patient_reviews: str
    ) -> Facility:
        """Create a new facility"""
        facility = Facility(
            name=name,
            location=location,
            certifications=certifications,
            doctor_info=doctor_info,
            patient_reviews=patient_reviews
        )
        await facility.save(self.db_session)
        return facility
    
    async def get_by_id(self, uuid: UUID) -> Optional[Facility]:
        """Get a facility by its ID"""
        query = select(Facility).where(Facility.uuid == uuid)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()
    
    async def get_all(self) -> List[Facility]:
        """Get all facilities"""
        query = select(Facility)
        result = await self.db_session.execute(query)
        return result.scalars().all()
    
    async def update(
        self,
        uuid: UUID,
        name: Optional[str] = None,
        location: Optional[str] = None,
        certifications: Optional[str] = None,
        doctor_info: Optional[str] = None,
        patient_reviews: Optional[str] = None
    ) -> Optional[Facility]:
        """Update a facility"""
        facility = await self.get_by_id(uuid)
        if not facility:
            return None
            
        update_data = {}
        if name is not None:
            update_data["name"] = name
        if location is not None:
            update_data["location"] = location
        if certifications is not None:
            update_data["certifications"] = certifications
        if doctor_info is not None:
            update_data["doctor_info"] = doctor_info
        if patient_reviews is not None:
            update_data["patient_reviews"] = patient_reviews
            
        await facility.update(self.db_session, **update_data)
        return facility
    
    async def delete(self, uuid: UUID) -> bool:
        """Delete a facility"""
        facility = await self.get_by_id(uuid)
        if not facility:
            return False
            
        await facility.delete(self.db_session)
        return True 