# **Backend Testing Implementation Guide**

## **Objective**  
Ensure proper testing of the backend implementation as specified in `requirements/details.md`, following the structured guidelines from `.cursor/rules/test.mdc`. Testing should cover unit tests, integration tests, and API tests to verify the correctness, reliability, and performance of the backend system.

---  

## **Step-by-Step Instructions**  

### **1. Understand the Testing Requirements**  
Before writing tests, review the relevant files to gain a clear understanding of what needs to be tested and how:

- **Read `requirements/details.md`** – Understand the full scope of backend functionalities to be tested.
- **Follow the testing guidelines in `.cursor/rules/tes.mdc`** – Ensure best practices and structural consistency in testing.
- **Refer to `requirements/prd.md`** – Consider the fundamental project requirements and goals for validation.
- **Check `requirements/task.md`** – Ensure test coverage aligns with the defined backend tasks.

---  

### **2. Organizing the Test Suite**  

#### **a. Define the test structure**  
Ensure that test files are placed correctly in the `tests/` directory with appropriate subdirectories for unit, integration, and API tests:

```
backend/
├── tests/                 # Main testing directory
│   ├── unit/             # Unit tests
│   ├── integration/      # Integration tests
│   ├── api/             # API tests
│   ├── conftest.py      # Test configuration & fixtures
│   └── __init__.py      # Test module initialization
```

#### **b. Use Pytest for Testing**  
- Ensure `pytest` is installed as a dependency in `pyproject.toml`.
- Run tests using `pytest` commands.
- Utilize `conftest.py` for reusable fixtures.

#### **c. Implement Feature-Specific Tests**  
- **Unit Tests**: Test individual functions and methods in isolation.
- **Integration Tests**: Validate database interactions and service layers.
- **API Tests**: Ensure all endpoints behave as expected.

---  

### **3. Writing Unit Tests**  

#### **a. Structure of Unit Tests**  
- Test core business logic in isolation.
- Use mock dependencies where necessary.
- Cover edge cases, valid cases, and failure scenarios.

#### **b. Example Unit Test**  
```python
import pytest
from app.database.models.user import User

def test_create_user():
    user = User(name="John Doe", email="john@example.com")
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
```

---  

### **4. Writing Integration Tests**  

#### **a. Structure of Integration Tests**  
- Test interactions with the database.
- Validate business logic across services.
- Use `pytest-asyncio` for async database queries.

#### **b. Example Integration Test**  
```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_database_connection():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == 200
```

---  

### **5. Writing API Tests**  

#### **a. Structure of API Tests**  
- Test all API endpoints for expected behavior.
- Validate request/response formats.
- Ensure authentication and authorization rules are enforced.
- Test edge cases and error handling.

#### **b. Example API Test**  
```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/users/", json={"name": "Jane", "email": "jane@example.com"})
        assert response.status_code == 201
        assert response.json()["name"] == "Jane"
```

---  

### **6. Update Scratchpad & Notes Files**  

#### **Scratchpad (`cursor_dev/test/test_scratchpad.md`)**  
- Log work-in-progress testing efforts.
- Track ongoing debugging and temporary notes.
- Record any known test failures and pending fixes.

#### **Notes File (`cursor_dev/test/test_notes.md`)**  
- Document key testing strategies and observations.
- Maintain a record of bugs discovered and resolutions applied.
- Ensure that both files remain structured and up-to-date.

---  

### **7. Running Tests & Ensuring Coverage**  

#### **a. Running Tests**  
- Execute tests using `pytest`:
  ```bash
  pytest tests/
  ```
- Run only API tests:
  ```bash
  pytest tests/api/
  ```
- Run integration tests with database:
  ```bash
  pytest tests/integration/
  ```

#### **b. Measuring Test Coverage**  
- Use `pytest-cov` to generate test coverage reports:
  ```bash
  pytest --cov=app tests/
  ```
- Ensure high coverage for critical functionalities.

---  

### **8. Validate & Finalize the Testing Implementation**  

- Cross-check the completed test suite against:
  - `requirements/project_structure.md` for correct placement of test files.
  - `requirements/details.md` to verify that all features are tested.
  - `.cursor/rules/test.mdc` to ensure compliance with best practices.
  - `requirements/prd.md` to confirm alignment with project requirements.
  - `requirements/task.md` to ensure full test coverage of implemented tasks.
- Review and resolve any failing tests before finalizing the testing phase.

---  

