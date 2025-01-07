from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.user.service import UserService
from app.schemas.user import UserCreate, UserResponse
from app.dependencies.database import get_session

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserResponse, status_code=201)
async def register_user(
    user_data: UserCreate,
    db_session: AsyncSession = Depends(get_session)
) -> UserResponse:
    user_service = UserService(db_session)
    
    # Check if user already exists
    if await user_service.get_user_by_email(user_data.email):
        raise HTTPException(
            status_code=422,
            detail="User with this email already exists"
        )
    
    if await user_service.get_user_by_username(user_data.username):
        raise HTTPException(
            status_code=422,
            detail="User with this username already exists"
        )
    
    # Create new user
    user = await user_service.create_user(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password
    )
    
    return UserResponse(
        msg="User created successfully",
        user_id=user.uuid
    ) 