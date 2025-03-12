from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import LargeBinary
from sqlmodel import Field, SQLModel, Relationship

from app.database.base.model import BaseModel, TimeStampMixin


class Report(BaseModel, TimeStampMixin, table=True):
    """
    Report model for storing PDF reports
    """
    compound_id: UUID = Field(foreign_key="compound.uuid", index=True)
    content: bytes = Field(sa_type=LargeBinary)
    
    # Relationships
    compound: "Compound" = Relationship(back_populates="reports")


class ReportCreate(SQLModel):
    """
    Schema for report creation
    """
    compound_id: UUID
    content: bytes


class ReportRead(SQLModel):
    """
    Schema for report response
    """
    uuid: UUID
    compound_id: UUID
    created_at: Optional[str] = None 