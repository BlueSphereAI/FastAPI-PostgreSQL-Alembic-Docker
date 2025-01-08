from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.price_comparisons.service import PriceComparisonService
from app.schemas.price_comparisons import (
    PriceComparisonCreate,
    PriceComparisonResponse,
    PriceComparisonUpdate
)
from app.dependencies.database import get_session

router = APIRouter(
    prefix="/price_comparisons",
    tags=["price_comparisons"]
)


@router.get("", response_model=List[PriceComparisonResponse])
async def get_price_comparisons(
    db: AsyncSession = Depends(get_session)
) -> List[PriceComparisonResponse]:
    """Get all price comparisons"""
    service = PriceComparisonService(db)
    comparisons = await service.get_all()
    return comparisons


@router.get("/{comparison_id}", response_model=PriceComparisonResponse)
async def get_price_comparison(
    comparison_id: UUID,
    db: AsyncSession = Depends(get_session)
) -> PriceComparisonResponse:
    """Get a specific price comparison by ID"""
    service = PriceComparisonService(db)
    comparison = await service.get_by_id(comparison_id)
    if not comparison:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Price comparison not found"
        )
    return comparison


@router.post("", response_model=PriceComparisonResponse, status_code=status.HTTP_201_CREATED)
async def create_price_comparison(
    comparison: PriceComparisonCreate,
    db: AsyncSession = Depends(get_session)
) -> PriceComparisonResponse:
    """Create a new price comparison"""
    service = PriceComparisonService(db)
    new_comparison = await service.create(
        procedure_id=comparison.procedure_id,
        facility_id=comparison.facility_id,
        country_id=comparison.country_id,
        us_price=comparison.us_price,
        international_price=comparison.international_price,
        travel_cost=comparison.travel_cost
    )
    return new_comparison


@router.put("/{comparison_id}", response_model=PriceComparisonResponse)
async def update_price_comparison(
    comparison_id: UUID,
    comparison: PriceComparisonUpdate,
    db: AsyncSession = Depends(get_session)
) -> PriceComparisonResponse:
    """Update a price comparison"""
    service = PriceComparisonService(db)
    updated_comparison = await service.update(
        uuid=comparison_id,
        us_price=comparison.us_price,
        international_price=comparison.international_price,
        travel_cost=comparison.travel_cost
    )
    if not updated_comparison:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Price comparison not found"
        )
    return updated_comparison


@router.delete("/{comparison_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_price_comparison(
    comparison_id: UUID,
    db: AsyncSession = Depends(get_session)
) -> None:
    """Delete a price comparison"""
    service = PriceComparisonService(db)
    deleted = await service.delete(comparison_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Price comparison not found"
        ) 