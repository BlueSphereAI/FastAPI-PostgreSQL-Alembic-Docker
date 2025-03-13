# Database Implementation Notes

## Database Configuration
- PostgreSQL database is used for this project
- Database is running in a Docker container with the following credentials:
  - Database name: postgres
  - Username: fastapi
  - Password: fastapi
  - Connection URL: postgresql+asyncpg://fastapi:fastapi@localhost:5432/postgres

## Model Design Decisions
- All models inherit from BaseModel which provides common functionality like save, update, and delete methods
- TimeStampMixin is used to automatically track created_at and updated_at timestamps
- UUID is used as the primary key for all models instead of integer IDs for better security and distribution
- Foreign keys are properly defined with ON DELETE CASCADE where appropriate
- Appropriate constraints are defined for fields (e.g., rating is constrained between 1 and 5)

## SQLAlchemy and SQLModel Usage
- The project uses SQLModel which combines SQLAlchemy and Pydantic
- This provides both ORM capabilities and data validation
- Async session management is used for better performance

## Alembic Migration Strategy
- Alembic is used for database migrations
- Migrations are generated automatically based on model changes
- The migration workflow is:
  1. Make changes to models
  2. Generate migration with `alembic revision --autogenerate -m "message"`
  3. Apply migration with `alembic upgrade head`
  4. If needed, rollback with `alembic downgrade -1`

## Implementation Notes

### Model Structure
1. **User Model**:
   - Primary fields: username, email, password_hash, first_name, last_name, user_type
   - Unique constraints on username and email
   - Password hashing using bcrypt via passlib

2. **Trainer Model**:
   - Extends user functionality with trainer-specific fields
   - One-to-one relationship with User model via user_id foreign key
   - Optional fields for biography, certifications, hourly_rate, specialties, location

3. **Appointment Model**:
   - Connects trainers and clients via foreign keys
   - Includes appointment_time and status fields
   - Status can be "Scheduled", "Completed", or "Cancelled"

4. **Feedback Model**:
   - Connected to appointments via appointment_id foreign key
   - Includes rating (1-5) and optional comments
   - Allows clients to rate their experience with trainers

5. **Availability Model**:
   - Tracks trainer availability with start_time and end_time
   - Connected to trainers via trainer_id foreign key
   - Boolean is_available flag to indicate if the slot is available

### Environment Variables
- The database connection URL is stored in the PG_DATABASE_URL environment variable
- This variable must be set before running Alembic commands or starting the application
- For local development, the value is set in the .env.local file

### Issues and Solutions
1. **Pydantic Type Annotations**:
   - SQLModel requires all fields to have type annotations
   - Enum-like classes need to use ClassVar for class variables
   - Example: `TRAINER: ClassVar[str] = "trainer"`

2. **Database Connection**:
   - The application uses asyncpg for async database connections
   - Connection string format: postgresql+asyncpg://username:password@host:port/database
