from typing import List, Optional
from uuid import UUID
from sqlmodel import select, join
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.feedback.model import Feedback
from app.database.appointment.model import Appointment

class FeedbackService(BaseService):
    """Feedback service"""

    async def get_by_uuid(self, uuid: UUID) -> Optional[Feedback]:
        """Get feedback by UUID"""
        query = select(Feedback).where(Feedback.uuid == uuid)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_appointment_id(self, appointment_id: UUID) -> Optional[Feedback]:
        """Get feedback by appointment ID"""
        query = select(Feedback).where(Feedback.appointment_id == appointment_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_trainer_id(self, trainer_id: UUID) -> List[Feedback]:
        """Get feedback by trainer ID"""
        query = select(Feedback).join(Appointment).where(Appointment.trainer_id == trainer_id)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def create(self, feedback: Feedback) -> Feedback:
        """Create new feedback"""
        await feedback.save(self.db_session)
        return feedback

    async def update(self, feedback: Feedback, **kwargs) -> Feedback:
        """Update feedback"""
        await feedback.update(self.db_session, **kwargs)
        return feedback

    async def delete(self, feedback: Feedback) -> None:
        """Delete feedback"""
        await feedback.delete(self.db_session) 