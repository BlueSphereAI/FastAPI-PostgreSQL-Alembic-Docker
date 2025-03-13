from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, Body, Query
from sqlmodel.ext.asyncio.session import AsyncSession

from app.dependencies.database import get_session
from app.database.appointment.service import AppointmentService
from app.database.user.service import UserService
from app.database.appointment.model import Appointment, AppointmentStatus
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate, AppointmentResponse

router = APIRouter()

@router.get("", response_model=List[AppointmentResponse])
async def get_appointments(
    status: Optional[str] = Query(None, description="Filter appointments by status"),
    db: AsyncSession = Depends(get_session),
):
    """
    Get all appointments, optionally filtered by status.
    """
    appointment_service = AppointmentService(db)
    
    # Validate status if provided
    if status and status not in [AppointmentStatus.SCHEDULED, AppointmentStatus.COMPLETED, AppointmentStatus.CANCELLED]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid status. Must be one of: {AppointmentStatus.SCHEDULED}, {AppointmentStatus.COMPLETED}, {AppointmentStatus.CANCELLED}",
        )
    
    appointments = await appointment_service.get_all(status)
    return appointments

@router.post("", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
async def create_appointment(
    appointment_data: AppointmentCreate = Body(
        ...,
        example={
            "trainer_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "client_id": "3fa85f64-5717-4562-b3fc-2c963f66afa7",
            "appointment_time": "2023-04-01T14:00:00Z"
        }
    ),
    db: AsyncSession = Depends(get_session),
):
    """
    Create a new appointment.
    """
    appointment_service = AppointmentService(db)
    user_service = UserService(db)
    
    # Check if trainer exists
    trainer = await user_service.get_by_uuid(appointment_data.trainer_id)
    if not trainer or trainer.user_type != "trainer":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trainer not found",
        )
    
    # Check if client exists
    client = await user_service.get_by_uuid(appointment_data.client_id)
    if not client or client.user_type != "client":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Client not found",
        )
    
    # Create appointment
    appointment = Appointment(
        trainer_id=appointment_data.trainer_id,
        client_id=appointment_data.client_id,
        appointment_time=appointment_data.appointment_time,
        status=AppointmentStatus.SCHEDULED,
    )
    
    await appointment_service.create(appointment)
    return appointment

@router.put("/{appointment_id}", response_model=AppointmentResponse)
async def update_appointment_status(
    appointment_id: UUID,
    appointment_data: AppointmentUpdate = Body(
        ...,
        example={
            "status": "Completed"
        }
    ),
    db: AsyncSession = Depends(get_session),
):
    """
    Update appointment status.
    """
    appointment_service = AppointmentService(db)
    
    # Check if appointment exists
    appointment = await appointment_service.get_by_uuid(appointment_id)
    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found",
        )
    
    # Validate status
    if appointment_data.status not in [AppointmentStatus.SCHEDULED, AppointmentStatus.COMPLETED, AppointmentStatus.CANCELLED]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid status. Must be one of: {AppointmentStatus.SCHEDULED}, {AppointmentStatus.COMPLETED}, {AppointmentStatus.CANCELLED}",
        )
    
    # Update appointment
    await appointment_service.update(appointment, status=appointment_data.status)
    
    return appointment

@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_appointment(
    appointment_id: UUID,
    db: AsyncSession = Depends(get_session),
):
    """
    Delete an appointment.
    """
    appointment_service = AppointmentService(db)
    
    # Check if appointment exists
    appointment = await appointment_service.get_by_uuid(appointment_id)
    if not appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found",
        )
    
    # Delete appointment
    await appointment_service.delete(appointment)
    
    return None 