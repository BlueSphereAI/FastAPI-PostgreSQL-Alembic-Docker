from typing import List, Optional
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.procedure.model import Procedure

class ProcedureService(BaseService):
    async def get_procedures(
        self,
        category: Optional[str] = None,
        name: Optional[str] = None
    ) -> List[Procedure]:
        query = select(Procedure)
        
        if category:
            query = query.where(Procedure.category == category)
        
        if name:
            query = query.where(Procedure.name.contains(name))
        
        result = await self.db_session.execute(query)
        return result.scalars().all() 