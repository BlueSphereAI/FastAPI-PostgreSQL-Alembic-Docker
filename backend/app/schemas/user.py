from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    """Base schema for user"""
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    user_type: str

class UserCreate(UserBase):
    """Schema for creating a user"""
    password: str

class UserUpdate(BaseModel):
    """Schema for updating a user"""
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserResponse(UserBase):
    """Schema for user response"""
    uuid: UUID

    class Config:
        from_attributes = True 