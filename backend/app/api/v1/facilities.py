from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.facility.service import FacilityService
from app.schemas.facility import FacilityResponse, ReviewResponse
from app.dependencies.database import get_session

router = APIRouter(prefix="/facilities", tags=["facilities"])

@router.get("/{facility_id}", response_model=FacilityResponse)
async def get_facility(
    facility_id: UUID,
    db_session: AsyncSession = Depends(get_session)
) -> FacilityResponse:
    facility_service = FacilityService(db_session)
    facility = await facility_service.get_facility_by_id(facility_id)
    
    if not facility:
        raise HTTPException(
            status_code=404,
            detail="Facility not found"
        )
    
    return FacilityResponse(
        facility_id=facility.uuid,
        name=facility.name,
        location=facility.location,
        credentials=facility.credentials,
        contact_email=facility.contact_email,
        reviews=[
            ReviewResponse(
                rating=review.rating,
                comment=review.comment
            ) for review in facility.reviews
        ]
    ) 