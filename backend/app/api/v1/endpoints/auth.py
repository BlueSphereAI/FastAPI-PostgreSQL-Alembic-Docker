from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel.ext.asyncio.session import AsyncSession

from app.dependencies.database import get_session
from app.schemas.auth import Token, LoginRequest, SignupRequest
from app.services.auth import AuthService

router = APIRouter()


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db_session: AsyncSession = Depends(get_session),
):
    """
    Authenticate a user and return a JWT token
    """
    auth_service = AuthService(db_session)
    
    # Authenticate the user
    user = await auth_service.authenticate_user(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token = auth_service.create_access_token(user.uuid)
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup", response_model=Token, status_code=status.HTTP_201_CREATED)
async def signup(
    signup_data: SignupRequest,
    db_session: AsyncSession = Depends(get_session),
):
    """
    Create a new user and return a JWT token
    """
    auth_service = AuthService(db_session)
    
    # Create the user
    user = await auth_service.create_user(signup_data.username, signup_data.password)
    
    # Create access token
    access_token = auth_service.create_access_token(user.uuid)
    
    return {"access_token": access_token, "token_type": "bearer"} 