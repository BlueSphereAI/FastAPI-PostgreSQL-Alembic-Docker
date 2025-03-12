from datetime import timedelta
from typing import Optional
from uuid import UUID

from fastapi import HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from app.config import get_settings
from app.database.user.model import User
from app.database.user.service import UserService
from app.util.security.jwt import create_access_token
from app.util.security.password import hash_password, verify_password

settings = get_settings()


class AuthService:
    """
    Authentication service
    """

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.user_service = UserService(db_session)

    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """
        Authenticate a user with username and password
        """
        # Get the user from the database
        user = await self.user_service.get_user_by_username(username)
        if user is None:
            return None

        # Verify the password
        if not verify_password(password, user.password_hash):
            return None

        # Update last login timestamp
        await self.user_service.update_last_login(user)

        return user

    async def create_user(self, username: str, password: str) -> User:
        """
        Create a new user
        """
        # Check if the username is already taken
        existing_user = await self.user_service.get_user_by_username(username)
        if existing_user is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered",
            )

        # Hash the password
        password_hash = hash_password(password)

        # Create the user
        user = await self.user_service.create_user(username, password_hash)

        return user

    def create_access_token(self, user_id: UUID) -> str:
        """
        Create a new access token for a user
        """
        expires_delta = timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        return create_access_token(user_id, expires_delta) 