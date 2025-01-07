from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.procedures.service import ProcedureService
from app.schemas.procedures import ProcedureCreate, ProcedureResponse, ProcedureUpdate
from app.dependencies.database import get_session

router = APIRouter(
    prefix="/procedures",
    tags=["procedures"]
)


@router.get("", response_model=List[ProcedureResponse])
async def get_procedures(
    db: AsyncSession = Depends(get_session)
) -> List[ProcedureResponse]:
    """Get all procedures"""
    service = ProcedureService(db)
    procedures = await service.get_all()
    return procedures


@router.get("/{procedure_id}", response_model=ProcedureResponse)
async def get_procedure(
    procedure_id: UUID,
    db: AsyncSession = Depends(get_session)
) -> ProcedureResponse:
    """Get a specific procedure by ID"""
    service = ProcedureService(db)
    procedure = await service.get_by_id(procedure_id)
    if not procedure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Procedure not found"
        )
    return procedure


@router.post("", response_model=ProcedureResponse, status_code=status.HTTP_201_CREATED)
async def create_procedure(
    procedure: ProcedureCreate,
    db: AsyncSession = Depends(get_session)
) -> ProcedureResponse:
    """Create a new procedure"""
    service = ProcedureService(db)
    new_procedure = await service.create(
        name=procedure.name,
        description=procedure.description
    )
    return new_procedure


@router.put("/{procedure_id}", response_model=ProcedureResponse)
async def update_procedure(
    procedure_id: UUID,
    procedure: ProcedureUpdate,
    db: AsyncSession = Depends(get_session)
) -> ProcedureResponse:
    """Update a procedure"""
    service = ProcedureService(db)
    updated_procedure = await service.update(
        uuid=procedure_id,
        name=procedure.name,
        description=procedure.description
    )
    if not updated_procedure:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Procedure not found"
        )
    return updated_procedure


@router.delete("/{procedure_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_procedure(
    procedure_id: UUID,
    db: AsyncSession = Depends(get_session)
) -> None:
    """Delete a procedure"""
    service = ProcedureService(db)
    deleted = await service.delete(procedure_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Procedure not found"
        ) 