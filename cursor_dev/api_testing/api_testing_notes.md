# API Testing Notes

## API Structure
The backend API is structured as follows:
- Base URL: http://localhost:8000
- API Version: v1 (Note: The actual endpoints use `/api/` without the version number)
- Authentication: JWT Bearer token

## Endpoints Overview

### Authentication Endpoints
- POST `/api/auth/signup` - Create a new user account
  - Request: Username and password
  - Response: JWT token
  - Status: ✅ Working correctly
- POST `/api/auth/login` - Login with existing credentials
  - Request: Username and password (using OAuth2PasswordRequestForm)
  - Response: JWT token
  - Status: ✅ Working correctly

### Compounds Endpoints
- POST `/api/compounds/upload` - Upload a new compound
  - Authentication: Required
  - Request: Chemical structure data
  - Response: Compound ID and message
  - Status: ✅ Working correctly
- GET `/api/compounds/{compound_id}` - Get compound details
  - Authentication: Required
  - Response: Compound details including binding affinity and repurposing suggestions
  - Status: ❌ Returns Internal Server Error

### Simulations Endpoints
- POST `/api/simulations/start` - Start a new simulation for a compound
  - Authentication: Required
  - Request: Compound ID
  - Response: Simulation ID and status
  - Status: ✅ Working correctly

### Reports Endpoints
- GET `/api/reports/download/{compound_id}` - Download a PDF report for a compound
  - Authentication: Required
  - Response: PDF report
  - Status: ❌ Returns Internal Server Error

## Authentication Flow
1. Register a new user via `/api/auth/signup`
2. Login with credentials via `/api/auth/login`
3. Use the returned JWT token in the Authorization header for subsequent requests:
   ```
   Authorization: Bearer {token}
   ```

## Common Headers
- Content-Type: application/json
- Authorization: Bearer {token} (for authenticated endpoints)

## Issues Discovered
1. The compound details endpoint (`/api/compounds/{compound_id}`) returns an Internal Server Error
2. The report download endpoint (`/api/reports/download/{compound_id}`) returns an Internal Server Error

## Recommendations
1. Investigate the backend code for the compound details and report download endpoints to identify and fix the issues
2. Add better error handling to provide more informative error messages
3. Implement proper logging to help diagnose issues in production
