from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field

class FeedbackBase(BaseModel):
    """Base schema for feedback"""
    appointment_id: UUID
    rating: int = Field(ge=1, le=5)
    comments: Optional[str] = None

class FeedbackCreate(FeedbackBase):
    """Schema for creating feedback"""
    pass

class FeedbackResponse(FeedbackBase):
    """Schema for feedback response"""
    uuid: UUID
    created_at: datetime

    class Config:
        from_attributes = True 