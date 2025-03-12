from fastapi import APIRouter

from app.api.v1.endpoints import auth, compounds, simulations, reports

api_router = APIRouter()

# Include all API routers
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(compounds.router, prefix="/compounds", tags=["compounds"])
api_router.include_router(simulations.router, prefix="/simulations", tags=["simulations"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"]) 