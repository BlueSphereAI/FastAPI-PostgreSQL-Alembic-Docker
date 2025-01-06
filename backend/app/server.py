from fastapi import Depends, FastAPI

# Create the FastAPI app
app = FastAPI()

# Index route
@app.get("/")
async def index():
    return {"message": "Master Server API"}
