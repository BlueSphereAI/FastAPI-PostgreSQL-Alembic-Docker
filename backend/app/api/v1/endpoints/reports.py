from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.binding_affinity.service import BindingAffinityService
from app.database.compound.service import CompoundService
from app.database.report.service import ReportService
from app.database.repurposing_suggestion.service import RepurposingSuggestionService
from app.database.simulation.service import SimulationService
from app.database.user.model import User
from app.dependencies.auth import get_current_user
from app.dependencies.database import get_session
from app.util.pdf.generator import generate_report_pdf

router = APIRouter()


@router.get("/download/{compound_id}")
async def download_report(
    compound_id: UUID,
    current_user: User = Depends(get_current_user),
    db_session: AsyncSession = Depends(get_session),
):
    """
    Download a PDF report for a compound
    """
    # Check if the compound exists and belongs to the current user
    compound_service = CompoundService(db_session)
    compound = await compound_service.get_compound_by_id(compound_id)
    
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
    
    # Get the report from the database
    report_service = ReportService(db_session)
    report = await report_service.get_report_by_compound(compound_id)
    
    # If the report doesn't exist, generate it
    if report is None:
        # Get the simulation for the compound
        simulation_service = SimulationService(db_session)
        simulations = await simulation_service.get_simulations_by_compound(compound_id)
        
        if not simulations:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No simulation found for this compound",
            )
        
        # Get the latest simulation
        latest_simulation = simulations[0]
        for simulation in simulations:
            if simulation.created_at > latest_simulation.created_at:
                latest_simulation = simulation
        
        # Get the binding affinity for the simulation
        binding_affinity_service = BindingAffinityService(db_session)
        binding_affinity = await binding_affinity_service.get_binding_affinity_by_simulation(
            latest_simulation.uuid
        )
        
        if binding_affinity is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No binding affinity found for this simulation",
            )
        
        # Get the repurposing suggestions for the compound
        repurposing_suggestion_service = RepurposingSuggestionService(db_session)
        repurposing_suggestions = await repurposing_suggestion_service.get_repurposing_suggestions_by_compound(
            compound_id
        )
        
        # Generate the report
        report_content = generate_report_pdf(
            compound=compound,
            simulation=latest_simulation,
            binding_affinity=binding_affinity,
            repurposing_suggestions=repurposing_suggestions,
        )
        
        # Save the report to the database
        report = await report_service.create_report(
            compound_id=compound_id,
            content=report_content,
        )
    
    # Return the report as a PDF file
    return Response(
        content=report.content,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=report_{compound_id}.pdf",
        },
    ) 