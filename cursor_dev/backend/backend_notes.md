# Backend Implementation Notes

## Project Structure
- The project follows a FastAPI, PostgreSQL, SQLAlchemy, Alembic, and Docker architecture
- Database models are created in separate directories under `app/database/`
- API endpoints are organized in `app/api/v1/endpoints/`
- Authentication is handled using JWT tokens

## Dependencies
- FastAPI for API framework
- SQLModel for database models
- Alembic for database migrations
- Passlib with bcrypt for password hashing
- Python-jose for JWT token handling
- Pydantic with email for data validation

## Database Connection
- Database URL: `postgresql+asyncpg://fastapi:fastapi@localhost:5432/postgres`
- Using asyncpg for async database operations

## Implementation Notes
- All database models inherit from BaseModel
- All services inherit from BaseService
- API endpoints use dependency injection for services
- Authentication is implemented using OAuth2 with JWT tokens
- Password hashing is done using bcrypt
