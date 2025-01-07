# Backend Detailed Requirements

The backend of the MediGlobal Connect platform will be implemented using FastAPI, designed to handle medical procedure comparisons, facility credential views, and travel expense estimations efficiently and securely. This documentation outlines the necessary APIs, models, schemas, and additional backend components to be developed.

## API Endpoints

### User Management API

**Path:** `/api/v1/users/register`  
**Method:** `POST`  
**Description:** Registers a new user.

- **Request Body:**
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```

- **Response Body:**
  ```json
  {
    "msg": "User created successfully",
    "user_id": "integer"
  }
  ```

- **Exceptions:**
  - `422 Unprocessable Entity`: Validation error or user already exists.

### Procedures API

**Path:** `/api/v1/procedures`  
**Method:** `GET`  
**Description:** Retrieves a list of medical procedures with optional filtering.

- **Query Parameters:**
  - `category` (optional): Filter by medical category.
  - `name` (optional): Search by partial procedure name.

- **Response Body:**
  ```json
  [
    {
      "procedure_id": "integer",
      "name": "string",
      "description": "string",
      "category": "string",
      "us_price": "decimal"
    }
  ]
  ```

### Facilities API

**Path:** `/api/v1/facilities/{facility_id}`  
**Method:** `GET`  
**Description:** Gets detailed information about a specific facility, including credentials and patient reviews.

- **Path Parameters:**
  - `facility_id`: The ID of the facility to retrieve.

- **Response Body:**
  ```json
  {
    "facility_id": "integer",
    "name": "string",
    "location": "string",
    "credentials": "json",
    "reviews": [
      {
        "rating": "integer",
        "comment": "string"
      }
    ]
  }
  ```

### Travel Estimation API

**Path:** `/api/v1/travel-estimates`  
**Method:** `POST`  
**Description:** Provide a cost estimation for travel related to a procedure.

- **Request Body:**
  ```json
  {
    "procedure_id": "integer",
    "facility_id": "integer"
  }
  ```

- **Response Body:**
  ```json
  {
    "total_estimate": "decimal",
    "breakdown": {
        "flight_cost": "decimal",
        "accommodation_cost": "decimal",
        "local_transportation_cost": "decimal"
    }
  }
  ```

### Booking Simulation API

**Path:** `/api/v1/bookings/simulate`  
**Method:** `POST`  
**Description:** Simulates a booking request for a given procedure at a facility.

- **Request Body:**
  ```json
  {
    "user_id": "integer",
    "procedure_id": "integer",
    "facility_id": "integer"
  }
  ```

- **Response Body:**
  ```json
  {
    "booking_id": "integer",
    "status": "SIMULATED"
  }
  ```

- **Exceptions:**
  - `404 Not Found`: If the procedure or facility is not valid.

### Chat Support Simulation API

**Path:** `/api/v1/chat/initiate`  
**Method:** `POST`  
**Description:** Starts a simulated chat session with a travel advisor.

- **Request Body:**
  ```json
  {
    "user_id": "integer"
  }
  ```

- **Response Body:**
  ```json
  {
    "chat_id": "integer",
    "messages": []
  }
  ```

- **Exceptions:**
  - `500 Internal Server Error`: Issues initializing chat session.

## Models and Schemas

### Models

- **User Model:**
  - `user_id`: Primary Key
  - `username`, `email`, `password_hash`, `created_at`, `updated_at`

- **Procedure Model:**
  - `procedure_id`: Primary Key
  - `name`, `description`, `category`, `us_price`, `created_at`

- **Facility Model:**
  - `facility_id`: Primary Key
  - `name`, `location`, `credentials`, `contact_email`, `created_at`, `updated_at`

- **TravelEstimates Model:**
  - `estimate_id`: Primary Key
  - `procedure_id`, `facility_id`, `flight_cost`, `accommodation_cost`, `local_transportation_cost`, `total_estimate`, `created_at`

- **Booking Model:**
  - `booking_id`: Primary Key
  - `user_id`, `procedure_id`, `facility_id`, `status`, `created_at`, `updated_at`

- **ChatLogs Model:**
  - `chat_id`: Primary Key
  - `user_id`, `messages`, `created_at`

### Schemas

- **User Schema:**
  - Request and response validation for user data

- **Procedure Schema:**
  - Validate procedure data for restful response

- **Facility Schema:**
  - Manage and display information about facilities

- **Booking Schema:**
  - Booking request and information handling

## Services

### Booking Service

- Handles the logic for simulating bookings, updating booking statuses, and fetching booking data.

### Cost Estimation Service

- Manages calculations for travel and accommodation expense estimations based on various parameters.

### User Management Service

- A central service to handle user registration, authentication, and profile management.

## Utilities

### Dependencies Utility

- Houses dependency injections and reusable functions for FastAPI configuration.

### Communication Utility

- Handles internal logic for chat messages and integration with third-party services like Twilio for future expansion.

This detailed backend documentation should provide a comprehensive understanding of how to implement each component of the MediGlobal Connect platform using FastAPI, PostgreSQL, and corresponding service layers. The structure supports scalability and ease of maintenance for developers working on the project.