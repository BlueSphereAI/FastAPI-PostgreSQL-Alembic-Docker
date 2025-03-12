from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import Field, SQLModel, Relationship

from app.database.base.model import BaseModel, TimeStampMixin


class RepurposingSuggestion(BaseModel, TimeStampMixin, table=True):
    """
    Repurposing Suggestion model for storing drug repurposing suggestions
    """
    compound_id: UUID = Field(foreign_key="compound.uuid", index=True)
    therapeutic_area: str
    suggestion_details: str
    
    # Relationships
    compound: "Compound" = Relationship(back_populates="repurposing_suggestions")


class RepurposingSuggestionCreate(SQLModel):
    """
    Schema for repurposing suggestion creation
    """
    compound_id: UUID
    therapeutic_area: str
    suggestion_details: str


class RepurposingSuggestionRead(SQLModel):
    """
    Schema for repurposing suggestion response
    """
    uuid: UUID
    compound_id: UUID
    therapeutic_area: str
    suggestion_details: str
    created_at: Optional[str] = None 