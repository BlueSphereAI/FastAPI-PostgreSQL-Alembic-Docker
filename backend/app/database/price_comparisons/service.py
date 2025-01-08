from typing import List, Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.price_comparisons.model import PriceComparison


class PriceComparisonService(BaseService):
    """
    Service for handling PriceComparison-related operations
    """
    
    async def create(
        self,
        procedure_id: UUID,
        facility_id: UUID,
        country_id: int,
        us_price: float,
        international_price: float,
        travel_cost: float
    ) -> PriceComparison:
        """Create a new price comparison"""
        comparison = PriceComparison(
            procedure_id=procedure_id,
            facility_id=facility_id,
            country_id=country_id,
            us_price=us_price,
            international_price=international_price,
            travel_cost=travel_cost
        )
        await comparison.save(self.db_session)
        return comparison
    
    async def get_by_id(self, uuid: UUID) -> Optional[PriceComparison]:
        """Get a price comparison by its ID"""
        query = select(PriceComparison).where(PriceComparison.uuid == uuid)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()
    
    async def get_all(self) -> List[PriceComparison]:
        """Get all price comparisons"""
        query = select(PriceComparison)
        result = await self.db_session.execute(query)
        return result.scalars().all()
    
    async def update(
        self,
        uuid: UUID,
        us_price: Optional[float] = None,
        international_price: Optional[float] = None,
        travel_cost: Optional[float] = None
    ) -> Optional[PriceComparison]:
        """Update a price comparison"""
        comparison = await self.get_by_id(uuid)
        if not comparison:
            return None
            
        update_data = {}
        if us_price is not None:
            update_data["us_price"] = us_price
        if international_price is not None:
            update_data["international_price"] = international_price
        if travel_cost is not None:
            update_data["travel_cost"] = travel_cost
            
        await comparison.update(self.db_session, **update_data)
        return comparison
    
    async def delete(self, uuid: UUID) -> bool:
        """Delete a price comparison"""
        comparison = await self.get_by_id(uuid)
        if not comparison:
            return False
            
        await comparison.delete(self.db_session)
        return True 