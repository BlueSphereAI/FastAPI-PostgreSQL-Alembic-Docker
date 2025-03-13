from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlmodel.ext.asyncio.session import AsyncSession

from app.dependencies.database import get_session
from app.database.availability.service import AvailabilityService
from app.database.user.service import UserService
from app.database.availability.model import Availability
from app.schemas.availability import AvailabilityResponse, AvailabilityUpdate, AvailabilityCreate

router = APIRouter()

@router.get("/{trainer_id}", response_model=List[AvailabilityResponse])
async def get_trainer_availability(
    trainer_id: UUID,
    db: AsyncSession = Depends(get_session),
):
    """
    Get availability slots for a trainer.
    """
    availability_service = AvailabilityService(db)
    user_service = UserService(db)
    
    # Check if trainer exists
    trainer = await user_service.get_by_uuid(trainer_id)
    if not trainer or trainer.user_type != "trainer":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trainer not found",
        )
    
    # Get availability
    availability_list = await availability_service.get_by_trainer_id(trainer_id)
    return availability_list

@router.put("/{trainer_id}", response_model=List[AvailabilityResponse])
async def update_trainer_availability(
    trainer_id: UUID,
    availability_data: AvailabilityUpdate = Body(
        ...,
        example={
            "availability_slots": [
                {
                    "start_time": "2023-04-01T09:00:00Z",
                    "end_time": "2023-04-01T10:00:00Z",
                    "is_available": True
                },
                {
                    "start_time": "2023-04-01T10:00:00Z",
                    "end_time": "2023-04-01T11:00:00Z",
                    "is_available": True
                }
            ]
        }
    ),
    db: AsyncSession = Depends(get_session),
):
    """
    Update availability slots for a trainer.
    """
    availability_service = AvailabilityService(db)
    user_service = UserService(db)
    
    # Check if trainer exists
    trainer = await user_service.get_by_uuid(trainer_id)
    if not trainer or trainer.user_type != "trainer":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trainer not found",
        )
    
    # Delete existing availability slots
    await availability_service.delete_by_trainer_id(trainer_id)
    
    # Create new availability slots
    new_availability_list = []
    for slot in availability_data.availability_slots:
        availability = Availability(
            trainer_id=trainer_id,
            start_time=slot.start_time,
            end_time=slot.end_time,
            is_available=slot.is_available,
        )
        await availability_service.create(availability)
        new_availability_list.append(availability)
    
    return new_availability_list 