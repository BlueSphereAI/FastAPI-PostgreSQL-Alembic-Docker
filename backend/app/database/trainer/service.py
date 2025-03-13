from typing import List, Optional
from uuid import UUID
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.trainer.model import Trainer

class TrainerService(BaseService):
    """Trainer service"""

    async def get_by_uuid(self, uuid: UUID) -> Optional[Trainer]:
        """Get a trainer by UUID"""
        query = select(Trainer).where(Trainer.uuid == uuid)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_user_id(self, user_id: UUID) -> Optional[Trainer]:
        """Get a trainer by user ID"""
        query = select(Trainer).where(Trainer.user_id == user_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def create(self, trainer: Trainer) -> Trainer:
        """Create a new trainer"""
        await trainer.save(self.db_session)
        return trainer

    async def update(self, trainer: Trainer, **kwargs) -> Trainer:
        """Update a trainer"""
        await trainer.update(self.db_session, **kwargs)
        return trainer

    async def delete(self, trainer: Trainer) -> None:
        """Delete a trainer"""
        await trainer.delete(self.db_session) 