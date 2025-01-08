from typing import Optional, List
from uuid import UUID

from sqlmodel import Field, Relationship

from app.database.base.model import BaseModel, TimeStampMixin


class Procedure(BaseModel, TimeStampMixin, table=True):
    """
    Procedure Model
    
    Attributes:
        name (str): Name of the medical procedure
        description (str): Detailed description of the procedure
    """
    
    name: str = Field(index=True)
    description: str

    # Relationships
    price_comparisons: List["PriceComparison"] = Relationship(back_populates="procedure")
    bookings: List["Booking"] = Relationship(back_populates="procedure") 