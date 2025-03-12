from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.user.model import User


class UserService(BaseService):
    """
    User service for user management
    """

    async def create_user(self, username: str, password_hash: str) -> User:
        """
        Create a new user
        """
        user = User(username=username, password_hash=password_hash)
        await user.save(self.db_session)
        return user

    async def get_user_by_id(self, user_id: UUID) -> Optional[User]:
        """
        Get user by ID
        """
        query = select(User).where(User.uuid == user_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_user_by_username(self, username: str) -> Optional[User]:
        """
        Get user by username
        """
        query = select(User).where(User.username == username)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def update_last_login(self, user: User) -> User:
        """
        Update user's last login timestamp
        """
        await user.update(self.db_session, last_login=datetime.now())
        return user 