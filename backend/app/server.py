from fastapi import Depends, FastAPI

from app.api.v1.api import api_router

# Create the FastAPI app
app = FastAPI(
    title="Fitness Trainer Booking API",
    description="API for booking fitness trainers",
    version="1.0.0",
)

# Register API routes
app.include_router(api_router, prefix="/api")

# Index route
@app.get("/")
async def index():
    return {"message": "Fitness Trainer Booking API"}
