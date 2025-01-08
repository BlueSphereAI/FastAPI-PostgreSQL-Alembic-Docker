from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.procedures import router as procedures_router
from app.api.v1.facilities import router as facilities_router
from app.api.v1.price_comparisons import router as price_comparisons_router
from app.api.v1.bookings import router as bookings_router

# Create the FastAPI app
app = FastAPI(title="MediGlobal Connect API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(procedures_router, prefix="/api")
app.include_router(facilities_router, prefix="/api")
app.include_router(price_comparisons_router, prefix="/api")
app.include_router(bookings_router, prefix="/api")

# Index route
@app.get("/")
async def index():
    return {"message": "MediGlobal Connect API"}
