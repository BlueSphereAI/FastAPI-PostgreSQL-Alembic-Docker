from typing import Optional, List
from uuid import UUID

from sqlmodel import Field, Relationship

from app.database.base.model import BaseModel, TimeStampMixin


class Facility(BaseModel, TimeStampMixin, table=True):
    """
    Facility Model
    
    Attributes:
        name (str): Name of the medical facility
        location (str): Location of the facility
        certifications (str): Certification details of the facility
        doctor_info (str): Information about the doctors
        patient_reviews (str): Patient reviews and feedback
    """
    
    name: str = Field(index=True)
    location: str = Field(index=True)
    certifications: str
    doctor_info: str
    patient_reviews: str

    # Relationships
    price_comparisons: List["PriceComparison"] = Relationship(back_populates="facility") 