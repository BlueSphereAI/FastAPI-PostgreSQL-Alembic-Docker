from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import Field, SQLModel, Relationship

from app.database.base.model import BaseModel, TimeStampMixin


class BindingAffinity(BaseModel, TimeStampMixin, table=True):
    """
    Binding Affinity model for storing binding affinity data
    """
    simulation_id: UUID = Field(foreign_key="simulation.uuid", index=True)
    before_affinity: float
    after_affinity: float
    
    # Relationships
    simulation: "Simulation" = Relationship(back_populates="binding_affinities")


class BindingAffinityCreate(SQLModel):
    """
    Schema for binding affinity creation
    """
    simulation_id: UUID
    before_affinity: float
    after_affinity: float


class BindingAffinityRead(SQLModel):
    """
    Schema for binding affinity response
    """
    uuid: UUID
    simulation_id: UUID
    before_affinity: float
    after_affinity: float
    created_at: Optional[str] = None 