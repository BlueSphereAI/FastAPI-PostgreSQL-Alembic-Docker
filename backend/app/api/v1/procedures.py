from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.procedure.service import ProcedureService
from app.schemas.procedure import ProcedureResponse
from app.dependencies.database import get_session

router = APIRouter(prefix="/procedures", tags=["procedures"])

@router.get("", response_model=List[ProcedureResponse])
async def list_procedures(
    category: Optional[str] = None,
    name: Optional[str] = None,
    db_session: AsyncSession = Depends(get_session)
) -> List[ProcedureResponse]:
    procedure_service = ProcedureService(db_session)
    procedures = await procedure_service.get_procedures(
        category=category,
        name=name
    )
    
    return [
        ProcedureResponse(
            procedure_id=proc.uuid,
            name=proc.name,
            description=proc.description,
            category=proc.category,
            us_price=proc.us_price
        ) for proc in procedures
    ] 