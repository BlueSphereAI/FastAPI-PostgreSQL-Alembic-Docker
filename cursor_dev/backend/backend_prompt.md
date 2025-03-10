
# **Backend Development Implementation Guide**  

## **Objective**  
Develop and implement the backend tasks as specified in `requirements/details.md`, following the structured guidelines from `.cursor/rules/backend.mdc`. Additionally, ensure that all implementations align with the foundational knowledge provided in `requirements/prd.md` and `requirements/task.md`, which contain essential project requirements and task details for the POC project.  

---  

## **Step-by-Step Instructions**  

### **1. Understand the Development Requirements**  
Before beginning the implementation, review the relevant files to gain a clear understanding of the scope, requirements, and technology choices:  

- **Read `requirements/details.md`** – Understand the full scope of backend tasks and feature requirements.  
- **Follow the implementation guidelines in `.cursor/rules/backend.mdc`** – Ensure best practices and structural consistency.  
- **Refer to `requirements/prd.md`** – Consider the fundamental project requirements and goals.  
- **Check `requirements/task.md`** – Ensure that the backend implementation aligns with the tasks defined for the POC project.  

---  

### **2. Backend Implementation**  

#### **a. Organize the project structure**  
Ensure the project structure follows the specifications outlined in `requirements/project_structure.md`.  

#### **b. Implement Features & Components**  
- Develop the backend based on the feature specifications in `requirements/details.md`.  
- Ensure modular, scalable, and maintainable code.  
- Implement code in alignment with the project requirements outlined in `requirements/prd.md`.  
- Follow the specific task implementations as described in `requirements/task.md`.  
- Ensure that all required libraries, frameworks, and configurations are correctly set up.  
- All code must be written inside the backend directory.
-  For configurations such as database and Python environment packages, refer to the configuration files inside the backend directory, including alembic.ini and pyproject.toml.
- Use the virtual environment located in the backend directory by running source backend/.venv/bin/activate

---  

### **3 API Implementation Rule**  
- Referencing `requirements/details.md`, `requirements/project_structure.md`, `requirements/prd.md`, and `requirements/task.md`, implement each API group mentioned in `requirements/details.md` with complete endpoint code, including actual database interaction logic, and configure router settings with the server **without user authentication**.  
- Always add api_router in `backend/app/server.py` to ensure that all API routes are properly registered with the FastAPI application.
# Start of Selection
- Always add an example in the request body of FastAPI API endpoints to enhance the openapi.json documentation. 

  Example:
  ```python
  from fastapi import FastAPI, Body

  app = FastAPI()

  @app.post("/create-user")
  async def create_user(user: User = Body(..., example={
      "name": "Jane Doe",
      "age": 25
  })):
      return user
  ```
# End of Selection

- Always ensure that a "User Sign-In" API is implemented whenever a "User Login" API exists.
- Ensure `pyproject.toml` in the `backend` directory includes all necessary Python dependencies, such as FastAPI, SQLAlchemy, asyncpg, Alembic, Uvicorn, Pydantic, and any other packages required by the project. Add the dependency in the file if needed.

---  

### **4. Update Scratchpad & Notes Files**  

#### **Scratchpad (`cursor_dev/backend/backend_scratchpad.md`)**  
- Log work-in-progress changes, ongoing debugging efforts, and temporary notes.  
- Keep track of any bugs, blockers, or pending tasks.  

#### **Notes File (`cursor_dev/backend/backend_notes.md`)**  
- Document key design choices, implementation decisions, challenges faced, and resolutions.  
- Maintain a record of dependencies installed, performance optimizations, and areas for future improvement.  
- Ensure that both files remain structured, up-to-date, and accessible for future reference.  

---  

### **5. Validate & Finalize the Backend Implementation**  
- Cross-check the completed implementation against:  
  - `requirements/project_structure.md` to ensure the correct project structure.  
  - `requirements/details.md` to verify feature completion.  
  - `.cursor/rules/backend.mdc` to ensure compliance with coding and development guidelines.  
  - `requirements/prd.md` to verify alignment with the core project requirements.  
  - `requirements/task.md` to ensure all specified tasks have been properly implemented.  
- Conduct final testing to verify that the implemented features function as expected.  
- Resolve any inconsistencies, errors, or missing components before finalizing the backend codebase.  

---  
