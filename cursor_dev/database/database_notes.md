# Database Implementation Notes

## Database Configuration
- PostgreSQL database is used for this project
- Database credentials:
  - Username: fastapi
  - Password: fastapi
  - Database name: postgres
  - Port: 5432
- Connection URL: `postgresql+asyncpg://fastapi:fastapi@localhost:5432/postgres`

## Model Structure
- All models inherit from `BaseModel` defined in `app/database/base/model.py`
- Models use SQLModel with `table=True` parameter
- Primary keys use UUID type with auto-generation
- Timestamps are handled through mixins:
  - `TimeStampMixin` for created_at and updated_at
  - `CreatedAtOnlyTimeStampMixin` for created_at only

## Database Schema
The following models have been implemented:

1. User Model
   - uuid: UUID (Primary Key)
   - username: string (Unique)
   - password_hash: string
   - created_at: TIMESTAMP
   - updated_at: TIMESTAMP
   - last_login: TIMESTAMP (nullable)

2. Compound Model
   - uuid: UUID (Primary Key)
   - user_id: UUID (Foreign Key to User)
   - chemical_structure: string
   - created_at: TIMESTAMP
   - updated_at: TIMESTAMP

3. Simulation Model
   - uuid: UUID (Primary Key)
   - compound_id: UUID (Foreign Key to Compound)
   - simulation_result: JSON
   - status: string
   - created_at: TIMESTAMP
   - updated_at: TIMESTAMP

4. Binding Affinity Model
   - uuid: UUID (Primary Key)
   - simulation_id: UUID (Foreign Key to Simulation)
   - before_affinity: float
   - after_affinity: float
   - created_at: TIMESTAMP
   - updated_at: TIMESTAMP

5. Repurposing Suggestion Model
   - uuid: UUID (Primary Key)
   - compound_id: UUID (Foreign Key to Compound)
   - therapeutic_area: string
   - suggestion_details: string
   - created_at: TIMESTAMP
   - updated_at: TIMESTAMP

6. Report Model
   - uuid: UUID (Primary Key)
   - compound_id: UUID (Foreign Key to Compound)
   - content: BYTEA
   - created_at: TIMESTAMP
   - updated_at: TIMESTAMP

## Relationships
- User -> Compound: One-to-Many
- Compound -> Simulation: One-to-Many
- Simulation -> BindingAffinity: One-to-Many
- Compound -> RepurposingSuggestion: One-to-Many
- Compound -> Report: One-to-Many

## Migrations
- Initial migration created and applied successfully
- Migration file: `backend/alembic/versions/e000a7fc4821_initial_migration.py`
- All tables created with proper indexes and foreign key constraints

## Database Access
- The database can be accessed using SQLModel ORM
- Each model has corresponding Create and Read schemas for API requests and responses
- The BaseModel provides methods for save, update, and delete operations
