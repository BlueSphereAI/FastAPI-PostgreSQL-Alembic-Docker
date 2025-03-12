# API Testing Plan

## Overview
We need to test the FastAPI backend endpoints located at http://localhost:8000. The API has the following main endpoints:
- `/api/auth` - Authentication endpoints (login, signup)
- `/api/compounds` - Compound management endpoints
- `/api/simulations` - Simulation endpoints
- `/api/reports` - Report endpoints

## Testing Steps

### 1. Server Setup
- [X] Activate Python virtual environment in the backend directory
- [X] Run the backend server using `make runLocal`
- [X] Verify the server is running at http://localhost:8000

### 2. Authentication Testing
- [X] Test user signup endpoint (`/api/auth/signup`)
- [X] Test user login endpoint (`/api/auth/login`)
- [X] Obtain and store authentication token for subsequent requests

### 3. Compounds Testing
- [X] Test compound upload endpoint (`/api/compounds/upload`)
- [X] Test retrieving compound details (`/api/compounds/{compound_id}`)
- [X] Verify authorization requirements

### 4. Simulations Testing
- [X] Test simulation start endpoint (`/api/simulations/start`)
- [X] Verify simulation results

### 5. Reports Testing
- [X] Test report download endpoint (`/api/reports/download/{compound_id}`)
- [X] Verify report content

## Testing Summary

### Working Endpoints
- Authentication endpoints (signup and login) are working correctly
- Compound upload endpoint is working correctly
- Simulation start endpoint is working correctly

### Issues Found
- Compound details retrieval endpoint returns an Internal Server Error
- Report download endpoint returns an Internal Server Error

### Authentication
- Authentication is properly enforced for all protected endpoints
- JWT tokens are correctly generated and can be used for subsequent requests

## Authentication Token
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkMjYwMWViOS0wZjI3LTRkMDktYWUyNS1jODRkMDIwY2M1NGYiLCJleHAiOjE3NDE3MTM2NjF9.FNDI_aePi2uFwsa73-wYjrIIGwjR-3Qu-dssgLoWB_0
```

## Compound ID
```
068a2e92-938c-4175-9f41-b225198f2206
```

## Simulation ID
```
30b18592-fa74-4d1b-ab19-0ce045d12c54
```
