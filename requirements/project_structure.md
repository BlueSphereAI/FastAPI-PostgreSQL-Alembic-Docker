# Project Structure Documentation

## Overview
This project implements a modern web application using FastAPI, PostgreSQL, SQLAlchemy, Alembic, and Docker. The architecture follows best practices for scalability, maintainability, and clean code organization.

## Directory Structure
```
FastAPI-PostgreSQL-Alembic-Docker/
├── backend/                     # Main backend application code
│   ├── alembic/                # Database migration files
│   ├── app/                    # Application source code
│   │   ├── api/               # API endpoints
│   │   │   └── v1/           # API version 1
│   │   ├── database/         # Database models and services
│   │   │   ├── base/        # Base models and services
│   │   │   └── [models]/    # Individual model directories
│   │   └── config.py        # Application configuration
│   ├── .env.local           # Local environment variables
│   ├── Dockerfile           # Docker configuration
│   ├── alembic.ini         # Alembic configuration
│   ├── Makefile            # Development commands
│   └── pyproject.toml      # Poetry dependencies
└── docker-compose.yml       # Docker services configuration
```

## Key Components

### 1. Database Layer
- **Location**: `backend/app/database/`
- **Components**:
  - `base/model.py`: Base model with common fields (uuid, timestamps)
  - `base/service.py`: Base service for database operations
  - Individual model directories with:
    - `model.py`: SQLModel-based data model
    - `service.py`: Business logic and database operations
    - `__init__.py`: Exports

### 2. API Layer
- **Location**: `backend/app/api/v1/`
- **Purpose**: REST API endpoints organized by resource
- **Structure**:
  - Separate router files for each resource
  - Request/Response models using Pydantic
  - Dependency injection for services

### 3. Configuration
- **Location**: `backend/app/config.py`
- **Purpose**: Application settings and environment variables
- **Features**:
  - Pydantic-based settings management
  - Environment variable validation
  - Cached configuration loading

### 4. Database Migrations
- **Location**: `backend/alembic/`
- **Purpose**: Database schema version control
- **Commands**:
  - `make initialMigration`: Create new migration
  - `make applyMigration`: Apply pending migrations

## Development Guidelines

### 1. Database Models
- Create new models in separate directories under `app/database/`
- Inherit from `BaseModel` for common fields
- Always set `table=True` for SQLModel classes
- Include type annotations for all fields

### 2. API Endpoints
- Use absolute imports
- Organize routes by resource
- Implement proper error handling
- Use dependency injection for services

### 3. Environment Setup
- Use Poetry for dependency management
- Local development uses `.env.local`
- Docker development uses environment variables in compose file

### 4. Docker Configuration
- Development environment: `docker-compose.dev.yml`
- Local environment: `docker-compose.local.yml`
- Production environment: Configure separately

## Best Practices

### 1. Code Organization
- Follow single responsibility principle
- Use type hints consistently
- Document public interfaces
- Keep functions and methods focused

### 2. Database Operations
- Use async operations with SQLAlchemy
- Implement proper error handling
- Use transactions appropriately
- Follow migration best practices

### 3. API Design
- Use proper HTTP methods
- Implement consistent error responses
- Version APIs appropriately
- Document endpoints using OpenAPI

### 4. Testing
- Write unit tests for services
- Write integration tests for APIs
- Use pytest for testing
- Implement proper test coverage

## Common Commands

### Development
```bash
# Start development environment
make runDevDocker

# Start local environment
make runLocalDocker

# Create new migration
make initialMigration

# Apply migrations
make applyMigration
```

### Database Models
When creating a new database model:
1. Create new directory in `app/database/`
2. Implement `model.py` and `service.py`
3. Update `app/database/__init__.py`
4. Generate and apply migrations

## Error Handling
- Use custom exception classes
- Implement proper error responses
- Log errors appropriately
- Handle database errors gracefully

## Security Considerations
- Implement proper authentication
- Use environment variables for secrets
- Validate input data
- Implement proper CORS settings

This structure provides a solid foundation for building scalable FastAPI applications with proper separation of concerns and maintainable code organization. 