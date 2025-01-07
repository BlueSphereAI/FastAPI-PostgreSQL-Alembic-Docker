from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.users import router as user_router
from app.api.v1.procedures import router as procedure_router

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
app.include_router(user_router, prefix="/api/v1")
app.include_router(procedure_router, prefix="/api/v1")

# Index route
@app.get("/")
async def index():
    return {"message": "MediGlobal Connect API"}
