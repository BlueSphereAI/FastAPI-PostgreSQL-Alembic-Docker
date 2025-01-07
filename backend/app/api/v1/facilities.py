from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.facilities.service import FacilityService
from app.schemas.facilities import FacilityCreate, FacilityResponse, FacilityUpdate
from app.dependencies.database import get_session

router = APIRouter(
    prefix="/facilities",
    tags=["facilities"]
)


@router.get("", response_model=List[FacilityResponse])
async def get_facilities(
    db: AsyncSession = Depends(get_session)
) -> List[FacilityResponse]:
    """Get all facilities"""
    service = FacilityService(db)
    facilities = await service.get_all()
    return facilities


@router.get("/{facility_id}", response_model=FacilityResponse)
async def get_facility(
    facility_id: UUID,
    db: AsyncSession = Depends(get_session)
) -> FacilityResponse:
    """Get a specific facility by ID"""
    service = FacilityService(db)
    facility = await service.get_by_id(facility_id)
    if not facility:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Facility not found"
        )
    return facility


@router.post("", response_model=FacilityResponse, status_code=status.HTTP_201_CREATED)
async def create_facility(
    facility: FacilityCreate,
    db: AsyncSession = Depends(get_session)
) -> FacilityResponse:
    """Create a new facility"""
    service = FacilityService(db)
    new_facility = await service.create(
        name=facility.name,
        location=facility.location,
        certifications=facility.certifications,
        doctor_info=facility.doctor_info,
        patient_reviews=facility.patient_reviews
    )
    return new_facility


@router.put("/{facility_id}", response_model=FacilityResponse)
async def update_facility(
    facility_id: UUID,
    facility: FacilityUpdate,
    db: AsyncSession = Depends(get_session)
) -> FacilityResponse:
    """Update a facility"""
    service = FacilityService(db)
    updated_facility = await service.update(
        uuid=facility_id,
        name=facility.name,
        location=facility.location,
        certifications=facility.certifications,
        doctor_info=facility.doctor_info,
        patient_reviews=facility.patient_reviews
    )
    if not updated_facility:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Facility not found"
        )
    return updated_facility


@router.delete("/{facility_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_facility(
    facility_id: UUID,
    db: AsyncSession = Depends(get_session)
) -> None:
    """Delete a facility"""
    service = FacilityService(db)
    deleted = await service.delete(facility_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Facility not found"
        ) 