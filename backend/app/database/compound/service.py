from typing import List, Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.compound.model import Compound


class CompoundService(BaseService):
    """
    Compound service for compound management
    """

    async def create_compound(self, user_id: UUID, chemical_structure: str) -> Compound:
        """
        Create a new compound
        """
        compound = Compound(user_id=user_id, chemical_structure=chemical_structure)
        await compound.save(self.db_session)
        return compound

    async def get_compound_by_id(self, compound_id: UUID) -> Optional[Compound]:
        """
        Get compound by ID
        """
        query = select(Compound).where(Compound.uuid == compound_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_compounds_by_user(self, user_id: UUID) -> List[Compound]:
        """
        Get all compounds for a user
        """
        query = select(Compound).where(Compound.user_id == user_id)
        result = await self.db_session.execute(query)
        return result.scalars().all() 