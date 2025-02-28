# Backend Detailed Requirements

## Overview
This document outlines the backend requirements for the AI-Driven Drug Repurposing Platform, detailing all necessary APIs, models, schemas, CRUD operations, services, and utilities to support the platform's core functionalities as described in the project overview and frontend detailed requirements.

## API Endpoints

### 1. Authentication API
**Path:** `/api/auth/login`  
**Method:** `POST`  
**Description:** Authenticates a user and returns a JWT token upon successful login.  

#### Request Body Parameters:
- `username`: `string` (required) - The user's username.
- `password`: `string` (required) - The user's password.

#### Response Body:
- `access_token`: `string` - JWT token for the authenticated user.
- `token_type`: `string` - The type of token provided (e.g., "bearer").

#### Exceptions:
- `401 Unauthorized` if the credentials are invalid.

---

### 2. Compound Management API
**Path:** `/api/compounds/upload`  
**Method:** `POST`  
**Description:** Allows the user to upload compound data.  

#### Request Body Parameters:
- `chemical_structure`: `string` (required) - Chemical structure or SMILES notation.

#### Response Body:
- `message`: `string` - Confirmation message regarding successful upload.
- `compound_id`: `UUID` - The unique identifier for the uploaded compound.

#### Exceptions:
- `400 Bad Request` if the compound data is improperly structured.

**Path:** `/api/compounds/{compound_id}`  
**Method:** `GET`  
**Description:** Retrieves compound details including binding affinity and repurposing suggestions.  

#### Path Parameters:
- `compound_id`: `UUID` - The unique identifier of the compound.

#### Response Body:
- `compound`: `object` - Detailed information about the compound including simulations and suggestions.

#### Exceptions:
- `404 Not Found` if the compound does not exist.

---

### 3. Simulation API
**Path:** `/api/simulations/start`  
**Method:** `POST`  
**Description:** Initiates a mock AI analysis for a given compound.  

#### Request Body Parameters:
- `compound_id`: `UUID` (required) - The unique ID of the compound for simulation.

#### Response Body:
- `simulation_id`: `UUID` - Identifier for the initiated simulation.
- `status`: `string` - Current simulation status.

#### Exceptions:
- `404 Not Found` if the compound ID is not valid.

---

### 4. Report API
**Path:** `/api/reports/download/{compound_id}`  
**Method:** `GET`  
**Description:** Downloads a PDF summary report for a specific compound.  

#### Path Parameters:
- `compound_id`: `UUID` - The unique identifier of the compound.

#### Response Body:
- **Binary PDF file** - The generated report file.

#### Exceptions:
- `404 Not Found` if the report for the compound does not exist.

---

## Models

### 1. User Model
**Attributes:**
- `user_id`: `UUID` - Primary Key.
- `username`: `string` - Unique.
- `password_hash`: `string`.
- `created_at`: `TIMESTAMP`.
- `last_login`: `TIMESTAMP`, nullable.

### 2. Compound Model
**Attributes:**
- `compound_id`: `UUID` - Primary Key.
- `user_id`: `UUID` - Foreign Key.
- `chemical_structure`: `string`.
- `upload_timestamp`: `TIMESTAMP`.

### 3. Simulation Model
**Attributes:**
- `simulation_id`: `UUID` - Primary Key.
- `compound_id`: `UUID` - Foreign Key.
- `simulation_result`: `JSON`.
- `status`: `string`.
- `created_at`: `TIMESTAMP`.

### 4. Binding Affinity Model
**Attributes:**
- `binding_id`: `UUID` - Primary Key.
- `simulation_id`: `UUID` - Foreign Key.
- `before_affinity`: `float`.
- `after_affinity`: `float`.
- `created_at`: `TIMESTAMP`.

### 5. Repurposing Suggestion Model
**Attributes:**
- `suggestion_id`: `UUID` - Primary Key.
- `compound_id`: `UUID` - Foreign Key.
- `therapeutic_area`: `string`.
- `suggestion_details`: `string`.
- `created_at`: `TIMESTAMP`.

### 6. Report Model
**Attributes:**
- `report_id`: `UUID` - Primary Key.
- `compound_id`: `UUID` - Foreign Key.
- `content`: `BYTEA`.
- `created_at`: `TIMESTAMP`.

---

## Schemas

### 1. User Schema
**Properties:**
- `username`: `string`.
- `password`: `string` (only in request schema).

### 2. Compound Schema
**Properties:**
- `chemical_structure`: `string`.

---

## CRUD Operations

### 1. User CRUD
**Operations:**
- Create user
- Retrieve user by ID
- Retrieve user by username

### 2. Compound CRUD
**Operations:**
- Create compound
- Retrieve compound by ID
- List compounds by user

---

## Services

### 1. AuthService
**Responsibilities:**
- Handle user authentication processes.
- Generate JWT tokens.
- Manage password hashing.

### 2. CompoundService
**Responsibilities:**
- Logic for processing compound uploads.
- Managing simulations.
- Generating reports.

---

## Utilities

### 1. JWT Utility
**Functions:**
- Generate and verify JWT tokens.

### 2. PDF Generator Utility
**Functions:**
- Convert simulation and compound data into downloadable PDF reports.

---

## Conclusion
This document provides a comprehensive blueprint for building the backend of the AI-Driven Drug Repurposing Platform. Each component and functionality is designed to ensure a robust, scalable, and maintainable system that aligns with both frontend requirements and overall project goals.

