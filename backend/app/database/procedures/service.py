from typing import List, Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.procedures.model import Procedure


class ProcedureService(BaseService):
    """
    Service for handling Procedure-related operations
    """
    
    async def create(self, name: str, description: str) -> Procedure:
        """Create a new procedure"""
        procedure = Procedure(name=name, description=description)
        await procedure.save(self.db_session)
        return procedure
    
    async def get_by_id(self, uuid: UUID) -> Optional[Procedure]:
        """Get a procedure by its ID"""
        query = select(Procedure).where(Procedure.uuid == uuid)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()
    
    async def get_all(self) -> List[Procedure]:
        """Get all procedures"""
        query = select(Procedure)
        result = await self.db_session.execute(query)
        return result.scalars().all()
    
    async def update(self, uuid: UUID, name: Optional[str] = None, description: Optional[str] = None) -> Optional[Procedure]:
        """Update a procedure"""
        procedure = await self.get_by_id(uuid)
        if not procedure:
            return None
            
        update_data = {}
        if name is not None:
            update_data["name"] = name
        if description is not None:
            update_data["description"] = description
            
        await procedure.update(self.db_session, **update_data)
        return procedure
    
    async def delete(self, uuid: UUID) -> bool:
        """Delete a procedure"""
        procedure = await self.get_by_id(uuid)
        if not procedure:
            return False
            
        await procedure.delete(self.db_session)
        return True 