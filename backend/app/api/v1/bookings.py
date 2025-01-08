from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.bookings.service import BookingService
from app.schemas.bookings import BookingCreate, BookingResponse, BookingUpdate
from app.dependencies.database import get_session

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"]
)


@router.get("", response_model=List[BookingResponse])
async def get_bookings(
    user_id: Optional[UUID] = None,
    db: AsyncSession = Depends(get_session)
) -> List[BookingResponse]:
    """
    Get all bookings.
    If user_id is provided, returns only bookings for that user.
    """
    service = BookingService(db)
    if user_id:
        bookings = await service.get_user_bookings(user_id)
    else:
        bookings = await service.get_all()
    return bookings


@router.get("/{booking_id}", response_model=BookingResponse)
async def get_booking(
    booking_id: UUID,
    db: AsyncSession = Depends(get_session)
) -> BookingResponse:
    """Get a specific booking by ID"""
    service = BookingService(db)
    booking = await service.get_by_id(booking_id)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    return booking


@router.post("", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(
    booking: BookingCreate,
    db: AsyncSession = Depends(get_session)
) -> BookingResponse:
    """Create a new booking"""
    service = BookingService(db)
    new_booking = await service.create(
        user_id=booking.user_id,
        facility_id=booking.facility_id,
        procedure_id=booking.procedure_id,
        itinerary=booking.itinerary,
        status=booking.status
    )
    return new_booking


@router.put("/{booking_id}", response_model=BookingResponse)
async def update_booking(
    booking_id: UUID,
    booking: BookingUpdate,
    db: AsyncSession = Depends(get_session)
) -> BookingResponse:
    """Update a booking"""
    service = BookingService(db)
    updated_booking = await service.update(
        uuid=booking_id,
        itinerary=booking.itinerary,
        status=booking.status
    )
    if not updated_booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )
    return updated_booking


@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_booking(
    booking_id: UUID,
    db: AsyncSession = Depends(get_session)
) -> None:
    """Delete a booking"""
    service = BookingService(db)
    deleted = await service.delete(booking_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        ) 