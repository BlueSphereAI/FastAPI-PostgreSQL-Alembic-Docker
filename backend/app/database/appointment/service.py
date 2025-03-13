from typing import List, Optional
from uuid import UUID
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.appointment.model import Appointment, AppointmentStatus

class AppointmentService(BaseService):
    """Appointment service"""

    async def get_by_uuid(self, uuid: UUID) -> Optional[Appointment]:
        """Get an appointment by UUID"""
        query = select(Appointment).where(Appointment.uuid == uuid)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_all(self, status: Optional[str] = None) -> List[Appointment]:
        """Get all appointments, optionally filtered by status"""
        query = select(Appointment)
        if status:
            query = query.where(Appointment.status == status)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def get_by_trainer_id(self, trainer_id: UUID) -> List[Appointment]:
        """Get appointments by trainer ID"""
        query = select(Appointment).where(Appointment.trainer_id == trainer_id)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def get_by_client_id(self, client_id: UUID) -> List[Appointment]:
        """Get appointments by client ID"""
        query = select(Appointment).where(Appointment.client_id == client_id)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def create(self, appointment: Appointment) -> Appointment:
        """Create a new appointment"""
        await appointment.save(self.db_session)
        return appointment

    async def update(self, appointment: Appointment, **kwargs) -> Appointment:
        """Update an appointment"""
        await appointment.update(self.db_session, **kwargs)
        return appointment

    async def delete(self, appointment: Appointment) -> None:
        """Delete an appointment"""
        await appointment.delete(self.db_session) 