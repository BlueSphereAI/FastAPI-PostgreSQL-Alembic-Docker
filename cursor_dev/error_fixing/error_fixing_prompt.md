# **Test Script Writing Guidelines**

### **1. Always Check the Scratchpad:**
- Before starting a new testing task, review the scratchpad for incomplete tasks and prioritize them.
- Complete tasks sequentially and update the scratchpad accordingly.

### **2. Task Implementation:**
- Implement test scripts one by one, focusing on verifying backend logic, particularly for APIs.
- Update the scratchpad upon completing a subtask or milestone.
- Verify if any testing tasks are pending before considering a task as complete.

### **3. API Testing Focus:**
- Write test scripts to cover all available API endpoints, ensuring proper request and response behavior.
- Validate status codes, response data, and error handling scenarios.

---

# **Backend Server Setup**

### **Check Server Status:**
- The backend server should be running at **http://localhost:8000**.
- If the server is not running, follow these steps:
  - Activate the Python virtual environment:
    ```bash
    source .venv/bin/activate
    ```
  - Run the server using the Makefile:
    ```bash
    make runLocal
    ```
  - Observe the terminal for any errors, warnings, or unexpected behavior.

---

# **Test Script Management**

### **Folder Structure:**
- Store all test scripts under a dedicated **test** directory within the **backend** directory to maintain organization:
  ```plaintext
  backend/
    └── test/
        ├── test_api_endpoints.py
        └── test_database_logic.py
  ```

### **Dependency Management:**
- If new testing dependencies are required, update the **pyproject.toml** file accordingly.
- Run:
```bash
poetry add <package_name>
```

---

# **cURL Command Logging:**
- Whenever a cURL command is executed successfully, log the command along with a clear description in the file `cursor_dev/api_testing/curl.md` to maintain a record of tested API endpoints.

---

# **Best Practices for Testing**

### **Validation:**
- Run all test scripts and validate outputs against expected results.
- Perform both positive and negative test cases to ensure robustness.

### **Documentation:**
- Document each test, expected behavior, and actual results for future reference.
- Include notes on edge cases and potential improvements identified during testing.

