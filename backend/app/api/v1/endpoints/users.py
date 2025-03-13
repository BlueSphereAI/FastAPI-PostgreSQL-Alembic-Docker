from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlmodel.ext.asyncio.session import AsyncSession

from app.dependencies.database import get_session
from app.database.user.service import UserService
from app.database.user.model import User
from app.schemas.user import UserCreate, UserUpdate, UserResponse

router = APIRouter()

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_session),
):
    """
    Get user details by ID.
    """
    user_service = UserService(db)
    user = await user_service.get_by_uuid(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate = Body(
        ...,
        example={
            "username": "johndoe",
            "email": "john.doe@example.com",
            "password": "securepassword",
            "first_name": "John",
            "last_name": "Doe",
            "user_type": "client"
        }
    ),
    db: AsyncSession = Depends(get_session),
):
    """
    Create a new user.
    """
    user_service = UserService(db)
    
    # Check if username already exists
    existing_user = await user_service.get_by_username(user_data.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already taken",
        )
    
    # Check if email already exists
    existing_user = await user_service.get_by_email(user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already taken",
        )
    
    # Create new user
    user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=User.create_password_hash(user_data.password),
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        user_type=user_data.user_type,
    )
    
    await user_service.create(user)
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: UUID,
    user_data: UserUpdate = Body(
        ...,
        example={
            "email": "new.email@example.com",
            "first_name": "John",
            "last_name": "Smith"
        }
    ),
    db: AsyncSession = Depends(get_session),
):
    """
    Update user details.
    """
    user_service = UserService(db)
    user = await user_service.get_by_uuid(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    # Check if email is being updated and already exists
    if user_data.email and user_data.email != user.email:
        existing_user = await user_service.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already taken",
            )
    
    # Update user
    update_data = user_data.model_dump(exclude_unset=True)
    await user_service.update(user, **update_data)
    
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_session),
):
    """
    Delete a user.
    """
    user_service = UserService(db)
    user = await user_service.get_by_uuid(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    await user_service.delete(user)
    return None 