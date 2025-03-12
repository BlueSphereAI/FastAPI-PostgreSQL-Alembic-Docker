from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class CompoundUploadRequest(BaseModel):
    """
    Compound upload request schema
    """
    chemical_structure: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "chemical_structure": "CC(=O)OC1=CC=CC=C1C(=O)O"
            }
        }


class CompoundUploadResponse(BaseModel):
    """
    Compound upload response schema
    """
    message: str
    compound_id: UUID


class BindingAffinityResponse(BaseModel):
    """
    Binding affinity response schema
    """
    before_affinity: float
    after_affinity: float


class RepurposingSuggestionResponse(BaseModel):
    """
    Repurposing suggestion response schema
    """
    uuid: UUID
    therapeutic_area: str
    suggestion_details: str


class CompoundDetailResponse(BaseModel):
    """
    Compound detail response schema
    """
    uuid: UUID
    chemical_structure: str
    upload_timestamp: datetime
    binding_affinity: Optional[BindingAffinityResponse] = None
    repurposing_suggestions: List[RepurposingSuggestionResponse] = [] 