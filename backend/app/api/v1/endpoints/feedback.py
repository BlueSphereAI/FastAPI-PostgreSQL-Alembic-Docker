from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlmodel.ext.asyncio.session import AsyncSession

from app.dependencies.database import get_session
from app.database.feedback.service import FeedbackService
from app.database.appointment.service import AppointmentService
from app.database.user.service import UserService
from app.database.feedback.model import Feedback
from app.database.appointment.model import AppointmentStatus
from app.schemas.feedback import FeedbackCreate, FeedbackResponse

router = APIRouter()

@router.get("/{trainer_id}", response_model=List[FeedbackResponse])
async def get_trainer_feedback(
    trainer_id: UUID,
    db: AsyncSession = Depends(get_session),
):
    """
    Get all feedback for a trainer.
    """
    feedback_service = FeedbackService(db)
    user_service = UserService(db)
    
    # Check if trainer exists
    trainer = await user_service.get_by_uuid(trainer_id)
    if not trainer or trainer.user_type != "trainer":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trainer not found",
        )
    
    # Get feedback
    feedback_list = await feedback_service.get_by_trainer_id(trainer_id)
    return feedback_list

@router.post("", response_model=FeedbackResponse, status_code=status.HTTP_201_CREATED)
async def create_feedback(
    feedback_data: FeedbackCreate = Body(
        ...,
        example={
            "appointment_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "rating": 5,
            "comments": "Great session! Very knowledgeable trainer."
        }
    ),
    db: AsyncSession = Depends(get_session),
):
    """
    Create feedback for an appointment.
    """
    feedback_service = FeedbackService(db)
    appointment_service = AppointmentService(db)
    
    # Check if appointment exists
    appointment = await appointment_service.get_by_uuid(feedback_data.appointment_id)
    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found",
        )
    
    # Check if appointment is completed
    if appointment.status != AppointmentStatus.COMPLETED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Feedback can only be provided for completed appointments",
        )
    
    # Check if feedback already exists for this appointment
    existing_feedback = await feedback_service.get_by_appointment_id(feedback_data.appointment_id)
    if existing_feedback:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Feedback already exists for this appointment",
        )
    
    # Create feedback
    feedback = Feedback(
        appointment_id=feedback_data.appointment_id,
        rating=feedback_data.rating,
        comments=feedback_data.comments,
    )
    
    await feedback_service.create(feedback)
    return feedback 