from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.binding_affinity.model import BindingAffinity
from app.database.binding_affinity.service import BindingAffinityService
from app.database.compound.model import Compound
from app.database.compound.service import CompoundService
from app.database.repurposing_suggestion.service import RepurposingSuggestionService
from app.database.simulation.service import SimulationService
from app.database.user.model import User
from app.dependencies.auth import get_current_user
from app.dependencies.database import get_session
from app.schemas.compound import (
    CompoundUploadRequest,
    CompoundUploadResponse,
    CompoundDetailResponse,
    BindingAffinityResponse,
    RepurposingSuggestionResponse,
)

router = APIRouter()


@router.post("/upload", response_model=CompoundUploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_compound(
    compound_data: CompoundUploadRequest,
    current_user: User = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_session),
):
    """
    Upload a new compound
    """
    # Create the compound
    compound_service = CompoundService(db_session)
    compound = await compound_service.create_compound(
        user_id=current_user.uuid,
        chemical_structure=compound_data.chemical_structure,
    )
    
    return {
        "message": "Compound uploaded successfully",
        "compound_id": compound.uuid,
    }


@router.get("/{compound_id}", response_model=CompoundDetailResponse)
async def get_compound(
    compound_id: UUID,
    current_user: User = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_session),
):
    """
    Get compound details
    """
    # Get the compound
    compound_service = CompoundService(db_session)
    compound = await compound_service.get_compound_by_id(compound_id)
    
    if compound is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Compound not found",
        )
    
    # Check if the compound belongs to the current user
    if compound.user_id != current_user.uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this compound",
        )
    
    # Get the simulation for the compound
    simulation_service = SimulationService(db_session)
    simulations = await simulation_service.get_simulations_by_compound(compound_id)
    
    # Get the binding affinity for the simulation
    binding_affinity_service = BindingAffinityService(db_session)
    binding_affinity = None
    
    if simulations:
        # Get the latest simulation
        latest_simulation = simulations[0]
        for simulation in simulations:
            if simulation.created_at > latest_simulation.created_at:
                latest_simulation = simulation
        
        # Get the binding affinity for the simulation
        binding_affinity_obj = await binding_affinity_service.get_binding_affinity_by_simulation(
            latest_simulation.uuid
        )
        
        if binding_affinity_obj:
            binding_affinity = BindingAffinityResponse(
                before_affinity=binding_affinity_obj.before_affinity,
                after_affinity=binding_affinity_obj.after_affinity,
            )
    
    # Get the repurposing suggestions for the compound
    repurposing_suggestion_service = RepurposingSuggestionService(db_session)
    repurposing_suggestions = await repurposing_suggestion_service.get_repurposing_suggestions_by_compound(
        compound_id
    )
    
    repurposing_suggestion_responses = [
        RepurposingSuggestionResponse(
            uuid=suggestion.uuid,
            therapeutic_area=suggestion.therapeutic_area,
            suggestion_details=suggestion.suggestion_details,
        )
        for suggestion in repurposing_suggestions
    ]
    
    return CompoundDetailResponse(
        uuid=compound.uuid,
        chemical_structure=compound.chemical_structure,
        upload_timestamp=compound.upload_timestamp,
        binding_affinity=binding_affinity,
        repurposing_suggestions=repurposing_suggestion_responses,
    ) 