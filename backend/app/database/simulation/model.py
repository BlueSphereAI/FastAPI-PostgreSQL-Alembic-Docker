from typing import Optional, List, Dict, Any
from uuid import UUID

from sqlmodel import Field, SQLModel, Relationship, JSON

from app.database.base.model import BaseModel, TimeStampMixin


class Simulation(BaseModel, TimeStampMixin, table=True):
    """
    Simulation model for storing AI simulation results
    """
    compound_id: UUID = Field(foreign_key="compound.uuid", index=True)
    simulation_result: Dict[str, Any] = Field(sa_type=JSON, default={})
    status: str
    
    # Relationships
    compound: "Compound" = Relationship(back_populates="simulations")
    binding_affinities: List["BindingAffinity"] = Relationship(back_populates="simulation")


class SimulationCreate(SQLModel):
    """
    Schema for simulation creation
    """
    compound_id: UUID
    status: str = "pending"


class SimulationRead(SQLModel):
    """
    Schema for simulation response
    """
    uuid: UUID
    compound_id: UUID
    simulation_result: Optional[Dict[str, Any]] = None
    status: str
    created_at: Optional[str] = None 