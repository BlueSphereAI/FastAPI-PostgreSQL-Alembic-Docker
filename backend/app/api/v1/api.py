from fastapi import APIRouter

from app.api.v1.endpoints import users, trainers, appointments, feedback, availability

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(trainers.router, prefix="/trainers", tags=["trainers"])
api_router.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
api_router.include_router(feedback.router, prefix="/feedback", tags=["feedback"])
api_router.include_router(availability.router, prefix="/availability", tags=["availability"]) 