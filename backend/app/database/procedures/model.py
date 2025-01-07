from typing import Optional
from uuid import UUID

from sqlmodel import Field

from app.database.base.model import BaseModel, TimeStampMixin


class Procedure(BaseModel, TimeStampMixin, table=True):
    """
    Procedure Model
    
    Attributes:
        name (str): Name of the medical procedure
        description (str): Detailed description of the procedure
    """
    
    name: str = Field(index=True)
    description: str 