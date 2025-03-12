from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router

# Create the FastAPI app
app = FastAPI(
    title="AI-Driven Drug Repurposing Platform API",
    description="API for the AI-Driven Drug Repurposing Platform",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api")

# Index route
@app.get("/")
async def index():
    return {"message": "AI-Driven Drug Repurposing Platform API"}
