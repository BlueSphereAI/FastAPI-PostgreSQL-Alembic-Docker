from typing import List, Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.binding_affinity.model import BindingAffinity


class BindingAffinityService(BaseService):
    """
    Binding Affinity service for binding affinity management
    """

    async def create_binding_affinity(
        self, simulation_id: UUID, before_affinity: float, after_affinity: float
    ) -> BindingAffinity:
        """
        Create a new binding affinity record
        """
        binding_affinity = BindingAffinity(
            simulation_id=simulation_id,
            before_affinity=before_affinity,
            after_affinity=after_affinity
        )
        await binding_affinity.save(self.db_session)
        return binding_affinity

    async def get_binding_affinity_by_id(self, binding_id: UUID) -> Optional[BindingAffinity]:
        """
        Get binding affinity by ID
        """
        query = select(BindingAffinity).where(BindingAffinity.uuid == binding_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_binding_affinity_by_simulation(self, simulation_id: UUID) -> Optional[BindingAffinity]:
        """
        Get binding affinity by simulation ID
        """
        query = select(BindingAffinity).where(BindingAffinity.simulation_id == simulation_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none() 