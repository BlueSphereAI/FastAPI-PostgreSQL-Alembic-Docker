from typing import List, Optional
from uuid import UUID
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.user.model import User

class UserService(BaseService):
    """User service"""

    async def get_by_uuid(self, uuid: UUID) -> Optional[User]:
        """Get a user by UUID"""
        query = select(User).where(User.uuid == uuid)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_username(self, username: str) -> Optional[User]:
        """Get a user by username"""
        query = select(User).where(User.username == username)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[User]:
        """Get a user by email"""
        query = select(User).where(User.email == email)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def create(self, user: User) -> User:
        """Create a new user"""
        await user.save(self.db_session)
        return user

    async def update(self, user: User, **kwargs) -> User:
        """Update a user"""
        await user.update(self.db_session, **kwargs)
        return user

    async def delete(self, user: User) -> None:
        """Delete a user"""
        await user.delete(self.db_session) 