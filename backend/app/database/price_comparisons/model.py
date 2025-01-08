from typing import Optional
from uuid import UUID

from sqlmodel import Field, Relationship

from app.database.base.model import BaseModel, TimeStampMixin
from app.database.procedures.model import Procedure
from app.database.facilities.model import Facility


class PriceComparison(BaseModel, TimeStampMixin, table=True):
    """
    PriceComparison Model
    
    Attributes:
        procedure_id (UUID): ID of the related procedure
        facility_id (UUID): ID of the related facility
        country_id (int): ID of the country
        us_price (float): Price in US dollars
        international_price (float): Price in international facility
        travel_cost (float): Estimated travel cost
    """
    
    procedure_id: UUID = Field(foreign_key="procedure.uuid")
    facility_id: UUID = Field(foreign_key="facility.uuid")
    country_id: int = Field(index=True)
    us_price: float
    international_price: float
    travel_cost: float

    # Relationships
    procedure: Optional[Procedure] = Relationship(back_populates="price_comparisons")
    facility: Optional[Facility] = Relationship(back_populates="price_comparisons") 