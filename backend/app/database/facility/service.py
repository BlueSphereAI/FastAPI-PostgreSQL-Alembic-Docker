from uuid import UUID
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.facility.model import Facility

class FacilityService(BaseService):
    async def get_facility_by_id(self, facility_id: UUID) -> Facility | None:
        query = select(Facility).where(Facility.uuid == facility_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none() 