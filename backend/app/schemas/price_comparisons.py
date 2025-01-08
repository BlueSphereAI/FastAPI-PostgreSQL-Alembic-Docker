from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class PriceComparisonBase(BaseModel):
    """Base schema for price comparison data"""
    procedure_id: UUID
    facility_id: UUID
    country_id: int
    us_price: float = Field(gt=0)
    international_price: float = Field(gt=0)
    travel_cost: float = Field(ge=0)


class PriceComparisonCreate(PriceComparisonBase):
    """Schema for creating a new price comparison"""
    pass


class PriceComparisonUpdate(BaseModel):
    """Schema for updating a price comparison"""
    us_price: Optional[float] = Field(None, gt=0)
    international_price: Optional[float] = Field(None, gt=0)
    travel_cost: Optional[float] = Field(None, ge=0)


class PriceComparisonResponse(PriceComparisonBase):
    """Schema for price comparison response"""
    uuid: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 