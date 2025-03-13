# Backend Requirements Documentation  

## API Endpoints  

### **Users Management Endpoints**  

#### **Get User Details**  
- **Endpoint:** `GET /api/users/{id}`  
- **Parameters:**  
  - `id` (path): Identifier of the user.  
- **Description:** Fetch detailed information about a specific user.  
- **Response:**  
  - `200 OK`: Returns user details.  
  - `404 Not Found`: User does not exist.  

#### **Create a New User**  
- **Endpoint:** `POST /api/users`  
- **Request Body:**  
  - `username` (string): Unique username.  
  - `password` (string): User's password.  
  - `email` (string): User's email address.  
  - `first_name` (string): User’s first name.  
  - `last_name` (string): User’s last name.  
  - `user_type` (string): Role of the user, either 'trainer' or 'client'.  
- **Description:** Creates a new user with the role 'trainer' or 'client.'  
- **Response:**  
  - `201 Created`: User successfully created.  
  - `400 Bad Request`: Invalid input data.  
  - `409 Conflict`: Username or email already taken.  

#### **Update User Information**  
- **Endpoint:** `PUT /api/users/{id}`  
- **Parameters:**  
  - `id` (path): Identifier of the user.  
- **Request Body:**  
  - `email` (string, optional): User's email address.  
  - `first_name` (string, optional): User's first name.  
  - `last_name` (string, optional): User's last name.  
- **Description:** Updates details for a specific user.  
- **Response:**  
  - `200 OK`: User details updated successfully.  
  - `400 Bad Request`: Invalid input data.  
  - `404 Not Found`: User does not exist.  

#### **Delete a User**  
- **Endpoint:** `DELETE /api/users/{id}`  
- **Parameters:**  
  - `id` (path): Identifier of the user.  
- **Description:** Deletes a specific user from the system.  
- **Response:**  
  - `204 No Content`: Successfully deleted user.  
  - `404 Not Found`: User does not exist.  

---

### **Trainer Management Endpoints**  

#### **Get Trainer Profile**  
- **Endpoint:** `GET /api/trainers/{user_id}`  
- **Parameters:**  
  - `user_id` (path): Identifier of the user who is a trainer.  
- **Description:** Fetch detailed information about a trainer.  
- **Response:**  
  - `200 OK`: Returns trainer's profile.  
  - `404 Not Found`: Trainer does not exist.  

#### **Update Trainer Profile**  
- **Endpoint:** `PUT /api/trainers/{user_id}`  
- **Parameters:**  
  - `user_id` (path): Identifier of the user who is a trainer.  
- **Request Body:**  
  - `biography` (string, optional): Trainer’s biography.  
  - `certifications` (string, optional): Trainer’s certifications.  
  - `hourly_rate` (number, optional): Hourly rate for the trainer.  
  - `specialties` (array, optional): List of specialties.  
  - `location` (string, optional): Trainer’s geographical location.  
- **Description:** Updates a trainer's profile information.  
- **Response:**  
  - `200 OK`: Trainer's profile updated successfully.  
  - `400 Bad Request`: Invalid input data.  
  - `404 Not Found`: Trainer does not exist.  

---

### **Appointment Scheduling Endpoints**  

#### **List Appointments**  
- **Endpoint:** `GET /api/appointments`  
- **Parameters:**  
  - `status` (query, optional): Filter the appointments by status (`Scheduled`, `Completed`, `Cancelled`).  
- **Description:** Fetch a list of all appointments with optional filtering by status.  
- **Response:**  
  - `200 OK`: Returns a list of appointments.  

#### **Create an Appointment**  
- **Endpoint:** `POST /api/appointments`  
- **Request Body:**  
  - `trainer_id` (integer): ID of the trainer.  
  - `client_id` (integer): ID of the client booking the appointment.  
  - `appointment_time` (datetime): Scheduled date and time for the appointment.  
- **Description:** Create a new appointment between a user and a trainer.  
- **Response:**  
  - `201 Created`: Appointment successfully created.  
  - `400 Bad Request`: Invalid input data.  

#### **Update Appointment Status**  
- **Endpoint:** `PUT /api/appointments/{id}`  
- **Parameters:**  
  - `id` (path): Identifier of the appointment.  
- **Request Body:**  
  - `status` (string): New status of the appointment.  
- **Description:** Update the status of an existing appointment.  
- **Response:**  
  - `200 OK`: Appointment status updated.  
  - `400 Bad Request`: Invalid status.  
  - `404 Not Found`: Appointment does not exist.  

#### **Delete an Appointment**  
- **Endpoint:** `DELETE /api/appointments/{id}`  
- **Parameters:**  
  - `id` (path): Identifier of the appointment.  
- **Description:** Delete an appointment from the schedule.  
- **Response:**  
  - `204 No Content`: Appointment successfully deleted.  
  - `404 Not Found`: Appointment does not exist.  

---

### **Feedback System Endpoints**  

#### **List Feedback for a Trainer**  
- **Endpoint:** `GET /api/feedback/{trainer_id}`  
- **Parameters:**  
  - `trainer_id` (path): Identifier of the trainer.  
- **Description:** Fetch all feedback entries for a specific trainer.  
- **Response:**  
  - `200 OK`: Returns the list of feedback for the trainer.  
  - `404 Not Found`: Trainer does not exist.  

#### **Create Feedback for an Appointment**  
- **Endpoint:** `POST /api/feedback`  
- **Request Body:**  
  - `appointment_id` (integer): ID of the completed appointment.  
  - `rating` (integer): Rating score given by the client.  
  - `comments` (string, optional): Written feedback provided by the client.  
- **Description:** Submit feedback for a completed appointment.  
- **Response:**  
  - `201 Created`: Feedback successfully recorded.  
  - `400 Bad Request`: Invalid input data.  
  - `404 Not Found`: Appointment does not exist.  

---

### **Availability Management Endpoints**  

#### **Get Trainer Availability**  
- **Endpoint:** `GET /api/availability/{trainer_id}`  
- **Parameters:**  
  - `trainer_id` (path): Identifier of the trainer.  
- **Description:** Fetch availability slots for a specific trainer.  
- **Response:**  
  - `200 OK`: Returns availability slots.  
  - `404 Not Found`: Trainer does not exist.  

#### **Update Trainer Availability**  
- **Endpoint:** `PUT /api/availability/{trainer_id}`  
- **Parameters:**  
  - `trainer_id` (path): Identifier of the trainer.  
- **Request Body:**  
  - `availability_slots` (array of objects): Array of availability slots where each object contains `start_time`, `end_time`, `is_available`.  
- **Description:** Updates availability slots for a specific trainer.  
- **Response:**  
  - `200 OK`: Availability updated successfully.  
  - `400 Bad Request`: Invalid input data.  
  - `404 Not Found`: Trainer does not exist.  

---

## **Models, Schemas, and Services**  

### **Models**  
- `User Model`: Represents users with attributes like `username`, `password_hash`, `email`, etc.  
- `Trainer Model`: Extends `User` model for trainers with additional attributes.  
- `Appointment Model`: Represents appointments.  
- `Feedback Model`: Stores feedback.  
- `Availability Model`: Captures real-time availability.  

---

This documentation provides a structured view for implementing, testing, and maintaining the backend efficiently.  
