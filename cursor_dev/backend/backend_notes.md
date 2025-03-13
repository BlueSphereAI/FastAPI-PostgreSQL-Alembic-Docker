# Backend Development Notes

## Project Structure
- The project follows a structured approach with FastAPI, PostgreSQL, SQLAlchemy, Alembic, and Docker.
- The backend directory contains the main application code.
- The app directory contains the API endpoints, database models, and services.

## Important Dependencies
- FastAPI: Web framework for building APIs
- SQLModel: ORM for database operations
- Alembic: Database migration tool
- Pydantic: Data validation and settings management
- AsyncPG: Asynchronous PostgreSQL driver

## Database Connection
- The database connection URL is stored in the `.env.local` file.
- The connection URL is: `postgresql+asyncpg://fastapi:fastapi@localhost:5432/postgres`

## Base Models
- BaseModel: Base model for all database models with common fields like UUID.
- TimeStampMixin: Adds created_at and updated_at fields to models.
- CreatedAtOnlyTimeStampMixin: Adds only created_at field to models.

## Implementation Notes
- All imports should be absolute, not relative.
- New models should be created in separate directories under app/database with model.py and service.py files.
- API endpoints should be organized by resource in app/api/v1/endpoints.
- All models should inherit from BaseModel and have table=True.
- All services should inherit from BaseService.

## API Endpoints
- Users Management: CRUD operations for users
- Trainer Management: Get and update trainer profiles
- Appointment Scheduling: CRUD operations for appointments
- Feedback System: Create and retrieve feedback
- Availability Management: Get and update trainer availability

## Authentication
- Password hashing is implemented using passlib with bcrypt scheme.
- User authentication is not implemented in this version but can be added using OAuth2 with JWT tokens.

## Data Validation
- Request and response models are defined using Pydantic schemas.
- Validation rules are applied to ensure data integrity.

## Error Handling
- HTTP exceptions are used to return appropriate error responses.
- Common error scenarios are handled with proper status codes and error messages.

## Reminders
- Update app/database/__init__.py after creating new models.
- Register API routes in app/server.py.
- Use dependency injection for services and database sessions.
- Add examples to request bodies for better OpenAPI documentation.

## Running the Application
- Apply database migrations: `alembic upgrade head`
- Start the FastAPI server: `uvicorn app.server:app --reload`
- Access the API documentation: `http://localhost:8000/docs`
