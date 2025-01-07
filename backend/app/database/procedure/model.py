from decimal import Decimal
from sqlmodel import Field

from app.database.base.model import BaseModel, CreatedAtOnlyTimeStampMixin

class Procedure(BaseModel, CreatedAtOnlyTimeStampMixin, table=True):
    name: str = Field(index=True)
    description: str
    category: str = Field(index=True)
    us_price: Decimal = Field(decimal_places=2) 