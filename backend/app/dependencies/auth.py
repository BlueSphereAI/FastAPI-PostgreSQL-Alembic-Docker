from typing import Optional
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.user.model import User
from app.database.user.service import UserService
from app.dependencies.database import get_session
from app.util.security.jwt import verify_token

# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme), db_session: AsyncSession = Depends(get_session)
) -> User:
    """
    Get the current authenticated user
    """
    # Verify the token
    token_data = verify_token(token)
    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Get the user from the database
    user_service = UserService(db_session)
    user = await user_service.get_user_by_id(token_data.user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


async def get_optional_current_user(
    token: Optional[str] = Depends(oauth2_scheme), db_session: AsyncSession = Depends(get_session)
) -> Optional[User]:
    """
    Get the current authenticated user, or None if not authenticated
    """
    if token is None:
        return None

    # Verify the token
    token_data = verify_token(token)
    if token_data is None:
        return None

    # Get the user from the database
    user_service = UserService(db_session)
    user = await user_service.get_user_by_id(token_data.user_id)

    return user 