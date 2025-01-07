from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel

class ProcedureResponse(BaseModel):
    procedure_id: UUID
    name: str
    description: str
    category: str
    us_price: Decimal 