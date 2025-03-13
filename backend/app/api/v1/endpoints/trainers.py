from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlmodel.ext.asyncio.session import AsyncSession

from app.dependencies.database import get_session
from app.database.trainer.service import TrainerService
from app.database.user.service import UserService
from app.database.trainer.model import Trainer
from app.schemas.trainer import TrainerCreate, TrainerUpdate, TrainerResponse

router = APIRouter()

@router.get("/{user_id}", response_model=TrainerResponse)
async def get_trainer(
    user_id: UUID,
    db: AsyncSession = Depends(get_session),
):
    """
    Get trainer profile by user ID.
    """
    trainer_service = TrainerService(db)
    user_service = UserService(db)
    
    # Check if user exists
    user = await user_service.get_by_uuid(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    # Check if user is a trainer
    if user.user_type != "trainer":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is not a trainer",
        )
    
    # Get trainer profile
    trainer = await trainer_service.get_by_user_id(user_id)
    if not trainer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trainer profile not found",
        )
    
    return trainer

@router.put("/{user_id}", response_model=TrainerResponse)
async def update_trainer(
    user_id: UUID,
    trainer_data: TrainerUpdate = Body(
        ...,
        example={
            "biography": "Certified personal trainer with 5 years of experience.",
            "certifications": "NASM CPT, ACE Group Fitness",
            "hourly_rate": 50.0,
            "specialties": "Weight Loss, Strength Training",
            "location": "New York, NY"
        }
    ),
    db: AsyncSession = Depends(get_session),
):
    """
    Update trainer profile.
    """
    trainer_service = TrainerService(db)
    user_service = UserService(db)
    
    # Check if user exists
    user = await user_service.get_by_uuid(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    # Check if user is a trainer
    if user.user_type != "trainer":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is not a trainer",
        )
    
    # Get trainer profile
    trainer = await trainer_service.get_by_user_id(user_id)
    
    # If trainer profile doesn't exist, create it
    if not trainer:
        trainer = Trainer(user_id=user_id)
        await trainer_service.create(trainer)
    
    # Update trainer profile
    update_data = trainer_data.model_dump(exclude_unset=True)
    await trainer_service.update(trainer, **update_data)
    
    return trainer 