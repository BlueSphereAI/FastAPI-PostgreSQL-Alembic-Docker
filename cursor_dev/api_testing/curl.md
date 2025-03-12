# cURL Commands Log

## Authentication Endpoints

### User Signup
```bash
# Create a new user account and receive a JWT token
curl -X POST "http://localhost:8000/api/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpassword123"}'
```
Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkMjYwMWViOS0wZjI3LTRkMDktYWUyNS1jODRkMDIwY2M1NGYiLCJleHAiOjE3NDE3MTM2Mjd9.FuR_MufkdmmhVfwhBgoRwg0-lU0215eHQtmddEe_Vsg",
  "token_type": "bearer"
}
```

### User Login
```bash
# Login with existing credentials and receive a JWT token
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=testpassword123"
```
Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkMjYwMWViOS0wZjI3LTRkMDktYWUyNS1jODRkMDIwY2M1NGYiLCJleHAiOjE3NDE3MTM2NjF9.FNDI_aePi2uFwsa73-wYjrIIGwjR-3Qu-dssgLoWB_0",
  "token_type": "bearer"
}
```

## Compounds Endpoints

### Upload Compound
```bash
# Upload a new compound with authentication
curl -X POST "http://localhost:8000/api/compounds/upload" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkMjYwMWViOS0wZjI3LTRkMDktYWUyNS1jODRkMDIwY2M1NGYiLCJleHAiOjE3NDE3MTM2NjF9.FNDI_aePi2uFwsa73-wYjrIIGwjR-3Qu-dssgLoWB_0" \
  -d '{"chemical_structure": "CC(=O)OC1=CC=CC=C1C(=O)O"}'
```
Response:
```json
{
  "message": "Compound uploaded successfully",
  "compound_id": "068a2e92-938c-4175-9f41-b225198f2206"
}
```

### Get Compound Details
```bash
# Get compound details with authentication
curl -X GET "http://localhost:8000/api/compounds/068a2e92-938c-4175-9f41-b225198f2206" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkMjYwMWViOS0wZjI3LTRkMDktYWUyNS1jODRkMDIwY2M1NGYiLCJleHAiOjE3NDE3MTM2NjF9.FNDI_aePi2uFwsa73-wYjrIIGwjR-3Qu-dssgLoWB_0"
```
Response:
```
Internal Server Error
```

### Authentication Verification
```bash
# Attempt to get compound details without authentication
curl -X GET "http://localhost:8000/api/compounds/068a2e92-938c-4175-9f41-b225198f2206"
```
Response:
```json
{
  "detail": "Not authenticated"
}
```

## Simulations Endpoints

### Start Simulation
```bash
# Start a simulation for a compound with authentication
curl -X POST "http://localhost:8000/api/simulations/start" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkMjYwMWViOS0wZjI3LTRkMDktYWUyNS1jODRkMDIwY2M1NGYiLCJleHAiOjE3NDE3MTM2NjF9.FNDI_aePi2uFwsa73-wYjrIIGwjR-3Qu-dssgLoWB_0" \
  -d '{"compound_id": "068a2e92-938c-4175-9f41-b225198f2206"}'
```
Response:
```json
{
  "simulation_id": "30b18592-fa74-4d1b-ab19-0ce045d12c54",
  "status": "completed"
}
```

## Reports Endpoints

### Download Report
```bash
# Download a report for a compound with authentication
curl -X GET "http://localhost:8000/api/reports/download/068a2e92-938c-4175-9f41-b225198f2206" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkMjYwMWViOS0wZjI3LTRkMDktYWUyNS1jODRkMDIwY2M1NGYiLCJleHAiOjE3NDE3MTM2NjF9.FNDI_aePi2uFwsa73-wYjrIIGwjR-3Qu-dssgLoWB_0"
```
Response:
```
Internal Server Error
```
