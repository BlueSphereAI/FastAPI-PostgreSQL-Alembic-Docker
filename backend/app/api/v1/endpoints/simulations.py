from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.binding_affinity.service import BindingAffinityService
from app.database.compound.service import CompoundService
from app.database.repurposing_suggestion.service import RepurposingSuggestionService
from app.database.simulation.service import SimulationService
from app.database.user.model import User
from app.dependencies.auth import get_current_user
from app.dependencies.database import get_session
from app.schemas.simulation import SimulationStartRequest, SimulationStartResponse

router = APIRouter()


@router.post("/start", response_model=SimulationStartResponse)
async def start_simulation(
    simulation_data: SimulationStartRequest,
    current_user: User = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_session),
):
    """
    Start a new simulation for a compound
    """
    # Check if the compound exists and belongs to the current user
    compound_service = CompoundService(db_session)
    compound = await compound_service.get_compound_by_id(simulation_data.compound_id)
    
    if compound is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Compound not found",
        )
    
    if compound.user_id != current_user.uuid:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this compound",
        )
    
    # Create a new simulation
    simulation_service = SimulationService(db_session)
    simulation = await simulation_service.create_simulation(compound.uuid)
    
    # Run the simulation
    simulation = await simulation_service.run_simulation(simulation)
    
    # Create binding affinity data
    binding_affinity_service = BindingAffinityService(db_session)
    binding_affinity = await binding_affinity_service.create_binding_affinity(
        simulation_id=simulation.uuid,
        before_affinity=simulation.simulation_result["binding_affinity"]["before"],
        after_affinity=simulation.simulation_result["binding_affinity"]["after"],
    )
    
    # Create repurposing suggestions
    repurposing_suggestion_service = RepurposingSuggestionService(db_session)
    await repurposing_suggestion_service.create_mock_suggestions(compound.uuid)
    
    return {
        "simulation_id": simulation.uuid,
        "status": simulation.status,
    } 