import json
import random
from typing import Dict, Any, List, Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.simulation.model import Simulation


class SimulationService(BaseService):
    """
    Simulation service for simulation management
    """

    async def create_simulation(self, compound_id: UUID) -> Simulation:
        """
        Create a new simulation
        """
        simulation = Simulation(
            compound_id=compound_id,
            status="pending",
        )
        await simulation.save(self.db_session)
        return simulation

    async def get_simulation_by_id(self, simulation_id: UUID) -> Optional[Simulation]:
        """
        Get simulation by ID
        """
        query = select(Simulation).where(Simulation.uuid == simulation_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_simulations_by_compound(self, compound_id: UUID) -> List[Simulation]:
        """
        Get all simulations for a compound
        """
        query = select(Simulation).where(Simulation.compound_id == compound_id)
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def update_simulation_status(self, simulation: Simulation, status: str) -> Simulation:
        """
        Update simulation status
        """
        await simulation.update(self.db_session, status=status)
        return simulation

    async def run_simulation(self, simulation: Simulation) -> Simulation:
        """
        Run a mock AI simulation
        """
        # Update status to running
        await self.update_simulation_status(simulation, "running")
        
        # Generate mock simulation results
        simulation_result = self._generate_mock_simulation_result()
        
        # Update simulation with results and completed status
        await simulation.update(
            self.db_session,
            simulation_result=simulation_result,
            status="completed"
        )
        
        return simulation
    
    def _generate_mock_simulation_result(self) -> Dict[str, Any]:
        """
        Generate mock simulation results
        """
        # Mock simulation result with random values
        return {
            "binding_affinity": {
                "before": round(random.uniform(0.1, 5.0), 2),
                "after": round(random.uniform(5.1, 10.0), 2),
                "improvement_percentage": round(random.uniform(30, 95), 2)
            },
            "molecular_properties": {
                "solubility": round(random.uniform(0.1, 1.0), 2),
                "stability": round(random.uniform(0.1, 1.0), 2),
                "toxicity": round(random.uniform(0.0, 0.5), 2)
            },
            "potential_targets": [
                {"name": "Target A", "confidence": round(random.uniform(0.7, 0.95), 2)},
                {"name": "Target B", "confidence": round(random.uniform(0.6, 0.85), 2)},
                {"name": "Target C", "confidence": round(random.uniform(0.5, 0.75), 2)}
            ]
        } 