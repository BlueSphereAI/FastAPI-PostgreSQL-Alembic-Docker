from datetime import datetime
from typing import Optional, List
from uuid import UUID

from sqlmodel import Field, SQLModel, Relationship

from app.database.base.model import BaseModel, TimeStampMixin


class Compound(BaseModel, TimeStampMixin, table=True):
    """
    Compound model for storing chemical compound information
    """
    user_id: UUID = Field(foreign_key="user.uuid", index=True)
    chemical_structure: str
    
    # Relationships
    simulations: List["Simulation"] = Relationship(back_populates="compound")
    repurposing_suggestions: List["RepurposingSuggestion"] = Relationship(back_populates="compound")
    reports: List["Report"] = Relationship(back_populates="compound")


class CompoundCreate(SQLModel):
    """
    Schema for compound creation
    """
    chemical_structure: str
    user_id: UUID


class CompoundRead(SQLModel):
    """
    Schema for compound response
    """
    uuid: UUID
    user_id: UUID
    chemical_structure: str
    created_at: Optional[str] = None 