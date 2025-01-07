from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database.base.service import BaseService
from app.database.user.model import User

class UserService(BaseService):
    async def create_user(self, username: str, email: str, password: str) -> User:
        user = User(username=username, email=email)
        user.set_password(password)
        await user.save(self.db_session)
        return user

    async def get_user_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_user_by_username(self, username: str) -> User | None:
        query = select(User).where(User.username == username)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none() 