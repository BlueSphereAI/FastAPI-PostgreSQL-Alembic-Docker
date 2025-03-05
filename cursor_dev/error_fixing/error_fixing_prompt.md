

# Important Guidelines

1. **Always Check the Scratchpad:**  
   Before starting a new error-fixing task, review the scratchpad for incomplete tasks and prioritize them. Complete tasks sequentially and update the scratchpad accordingly.

2. **Task Implementation:**  
   - Implement fixes one by one.
   - Update the scratchpad upon completing a subtask or milestone.
   - Verify if any tasks are pending before considering a task as complete.

3. **Avoid Missing Tasks:**  
   Ensure all identified errors are accounted for and resolved—never skip an error.

4. **Running the Server:**
  - Activate the Python virtual environment using the command 'source .venv/bin/activate' in the **backend** directory.
  - Run the backend server using the command `make runLocal`. The **Makefile** is located in the **backend** directory.
  - Observe the terminal for errors, warnings, or unexpected behavior.
  - Identify, analyze, and fix all errors found during runtime.

# Best Practices

- **Error Identification:**  
  - Pay attention to error messages, stack traces, and logs.
  - Utilize tools like `pdb`, `print()`, or logging for debugging if needed.

- **Systematic Fixing:**  
  - Tackle errors systematically, starting with critical errors that block the application from running.
  - Ensure that each fix is tested thoroughly before moving on to the next issue.

- **Validation:**  
  - After fixing an error, rerun the server and validate the fix.
  - Check the application behavior to ensure no new issues are introduced.

- **Documentation:**  
  - Document the error, the fix implemented, and any relevant insights for future reference.

