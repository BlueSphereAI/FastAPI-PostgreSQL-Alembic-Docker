from typing import List
from uuid import UUID
from pydantic import BaseModel, EmailStr

class ReviewResponse(BaseModel):
    rating: int
    comment: str

class FacilityResponse(BaseModel):
    facility_id: UUID
    name: str
    location: str
    credentials: dict
    contact_email: EmailStr
    reviews: List[ReviewResponse] 