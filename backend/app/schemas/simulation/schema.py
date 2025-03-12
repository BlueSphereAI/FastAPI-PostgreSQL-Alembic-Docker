from typing import Dict, Any
from uuid import UUID

from pydantic import BaseModel


class SimulationStartRequest(BaseModel):
    """
    Simulation start request schema
    """
    compound_id: UUID
    
    class Config:
        json_schema_extra = {
            "example": {
                "compound_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }
        }


class SimulationStartResponse(BaseModel):
    """
    Simulation start response schema
    """
    simulation_id: UUID
    status: str 