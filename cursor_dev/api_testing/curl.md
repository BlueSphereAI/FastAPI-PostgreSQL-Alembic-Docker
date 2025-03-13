# cURL Command Log

This file contains a record of all successful API requests made during testing.

## Format
Each entry should include:
1. A clear description of the API endpoint and purpose
2. The complete cURL command used
3. A brief note about the response (optional)

## Log Entries

### 1. Create a new user (POST /api/users)
```bash
curl -X POST http://localhost:8000/api/users -H "Content-Type: application/json" -d '{"username": "testuser", "email": "testuser@example.com", "password": "securepassword", "first_name": "Test", "last_name": "User", "user_type": "client"}'
```
Response: Successfully created a new user with UUID a6d84357-5917-4ded-b5d0-256d81c3a318

### 2. Get user details (GET /api/users/{user_id})
```bash
curl -X GET http://localhost:8000/api/users/a6d84357-5917-4ded-b5d0-256d81c3a318 -H "Content-Type: application/json"
```
Response: Successfully retrieved user details for the user with UUID a6d84357-5917-4ded-b5d0-256d81c3a318

### 3. Update user details (PUT /api/users/{user_id})
```bash
curl -X PUT http://localhost:8000/api/users/a6d84357-5917-4ded-b5d0-256d81c3a318 -H "Content-Type: application/json" -d '{"email": "updated.email@example.com", "first_name": "Updated", "last_name": "User"}'
```
Response: Successfully updated the user with UUID a6d84357-5917-4ded-b5d0-256d81c3a318

### 4. Delete user (DELETE /api/users/{user_id})
```bash
curl -X DELETE http://localhost:8000/api/users/a6d84357-5917-4ded-b5d0-256d81c3a318 -H "Content-Type: application/json"
```
Response: Successfully deleted the user with UUID a6d84357-5917-4ded-b5d0-256d81c3a318 (HTTP 204 No Content)

### 5. Create a trainer user (POST /api/users)
```bash
curl -X POST http://localhost:8000/api/users -H "Content-Type: application/json" -d '{"username": "trainer1", "email": "trainer1@example.com", "password": "securepassword", "first_name": "Trainer", "last_name": "One", "user_type": "trainer"}'
```
Response: Successfully created a new trainer user with UUID 4ac0ec6a-839b-4aa8-afef-b9f576b63237

### 6. Create/Update trainer profile (PUT /api/trainers/{user_id})
```bash
curl -X PUT http://localhost:8000/api/trainers/4ac0ec6a-839b-4aa8-afef-b9f576b63237 -H "Content-Type: application/json" -d '{"biography": "Certified personal trainer with 5 years of experience.", "certifications": "NASM CPT, ACE Group Fitness", "hourly_rate": 50.0, "specialties": "Weight Loss, Strength Training", "location": "New York, NY"}'
```
Response: Successfully created a trainer profile with UUID 2bb96248-ffe9-4b6d-bbe1-4457164ebc77

### 7. Get trainer details (GET /api/trainers/{user_id})
```bash
curl -X GET http://localhost:8000/api/trainers/4ac0ec6a-839b-4aa8-afef-b9f576b63237 -H "Content-Type: application/json"
```
Response: Successfully retrieved trainer details for the trainer with UUID 2bb96248-ffe9-4b6d-bbe1-4457164ebc77

### 8. Create a client user (POST /api/users)
```bash
curl -X POST http://localhost:8000/api/users -H "Content-Type: application/json" -d '{"username": "client1", "email": "client1@example.com", "password": "securepassword", "first_name": "Client", "last_name": "One", "user_type": "client"}'
```
Response: Successfully created a new client user with UUID aaa0f3d3-ef2e-4c5b-b539-a64f300e7426

### 9. List all appointments (GET /api/appointments)
```bash
curl -X GET http://localhost:8000/api/appointments -H "Content-Type: application/json"
```
Response: Successfully retrieved a list of all appointments
