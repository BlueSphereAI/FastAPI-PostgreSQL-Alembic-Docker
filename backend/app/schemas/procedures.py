from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ProcedureBase(BaseModel):
    """Base schema for procedure data"""
    name: str
    description: str


class ProcedureCreate(ProcedureBase):
    """Schema for creating a new procedure"""
    pass


class ProcedureUpdate(BaseModel):
    """Schema for updating a procedure"""
    name: Optional[str] = None
    description: Optional[str] = None


class ProcedureResponse(ProcedureBase):
    """Schema for procedure response"""
    uuid: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 