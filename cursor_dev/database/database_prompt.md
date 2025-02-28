
# **Database Development Implementation Guide**  

## **Objective**  
Implement and manage the database system as required in `requirements/details.md`, ensuring alignment with the structured database rules in `.cursor/rules/database.mdc`. Additionally, follow the foundational project guidelines provided in `requirements/prd.md` and `requirements/task.md` to maintain consistency with the POC project objectives.  

---

## **Step-by-Step Instructions**  

### **1. Understand Database Requirements**  
Before proceeding with database setup and modifications, review the following files to fully grasp the project’s data structure and requirements:  

- **Read `requirements/details.md`** – Understand the database schema, tables, relationships, and any required queries.  
- **Follow `.cursor/rules/database.mdc`** – Adhere to database best practices, naming conventions, and structuring guidelines.  
- **Refer to `requirements/prd.md`** – Ensure the database design aligns with the core project goals.  
- **Check `requirements/task.md`** – Verify that all database-related tasks are implemented correctly.  

---

### **2. Database Setup & Configuration**  

#### **a. Ensure the PostgreSQL Database is Running**  
- The PostgreSQL container is already running.  
- Check `docker-compose.local.yml` for the **database name, username, and password**.  
- If the database already exists:  
  - Create a **new database**.  
  - Update all source code files where database connection details are used.  
  - Modify the database name in `docker-compose.local.yml` accordingly.  

#### **b. Apply Database Migrations**  
- The project uses **Alembic** for database migrations.  
- Apply all necessary migrations using Alembic:  
  ```bash
  alembic upgrade head
  ```  
- If database schema modifications are required, generate a new migration script:  
  ```bash
  alembic revision --autogenerate -m "Describe the changes"
  alembic upgrade head
  ```  
- Ensure all migrations are applied without errors.  

---

### **3. Handle Errors & Data Consistency**  
- **Resolve any database-related errors** that arise during migration or runtime.  
- If data inconsistencies occur:  
  - Refer to API structure in `requirements/details.md`.  
  - Cross-check project requirements in `requirements/prd.md`.  
  - Validate data handling according to `requirements/task.md`.  
- Modify database schemas, constraints, or queries if necessary to align with the project’s needs.  

---

### **4. Update Scratchpad & Notes Files**  

#### **Scratchpad (`cursor_dev/database/database_scratchpad.md`)**  
- Log database setup progress, schema changes, and troubleshooting steps.  
- Keep track of any migration issues, inconsistencies, or pending modifications.  

#### **Notes File (`cursor_dev/database/database_notes.md`)**  
- Document schema design decisions, indexing strategies, and query optimizations.  
- Keep a record of applied migrations and any manual database modifications.  
- Ensure both files remain structured and updated for future reference.  

---

### **5. Validate & Finalize the Database Implementation**  
- Verify the database structure against:  
  - `requirements/project_structure.md` for correct integration with the backend.  
  - `requirements/details.md` for table definitions and relationships.  
  - `.cursor/rules/database.mdc` for compliance with database rules.  
  - `requirements/prd.md` to ensure alignment with core project requirements.  
  - `requirements/task.md` to confirm all database-related tasks are completed.  
- Perform integrity checks and optimize queries for efficiency.  
- Run tests to validate that the database operates correctly within the project’s backend.  
- Resolve any outstanding errors or inconsistencies before finalizing the implementation.  

