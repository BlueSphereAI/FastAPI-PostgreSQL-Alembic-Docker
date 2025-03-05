# Important Guidelines

1. **Always Check the Scratchpad:**  
   Before starting a new testing task, review the scratchpad for incomplete tasks and prioritize them. Complete tasks sequentially and update the scratchpad accordingly.

2. **Task Implementation:**  
   - Implement tasks one by one.
   - Update the scratchpad upon completing a subtask or milestone.
   - Verify if any tasks are pending before considering a task as complete.

3. **Avoid Missing Tasks:**  
   Ensure all tasks are accounted for and implemented—never skip a task.

4. **API Location & Server Details:**

    - The Python code for the APIs is located at backend/app/api. Check all the APIs and perform testing.

    - If any issues are found, resolve them accordingly.

    - The backend server is hosted at http://localhost:8000. If the server is not found, inspect the backend directory to determine the correct server hosting details.



# cURL Command Rules

- **Consistency:**  
  - Use clear and descriptive comments before each cURL command.
  - Always include all necessary headers, authentication tokens, and parameters.

- **Formatting:**  
  - Use multi-line formatting for better readability:
    ```bash
    curl -X POST "https://example.com/api" \
      -H "Authorization: Bearer <token>" \
      -H "Content-Type: application/json" \
      -d '{"key": "value"}'
    ```

- **Error Handling:**  
  - Always include `-v` (verbose) or `-i` (include headers) flags when troubleshooting.
  - Capture output to a file if needed:
    ```bash
    curl -X GET "https://example.com/api" -o response.json
    ```

# Best Practices

- **Authentication:**  
  - Use environment variables for sensitive information:
    ```bash
    curl -H "Authorization: Bearer $API_TOKEN" https://example.com/api
    ```

- **Testing & Validation:**  
  - Compare responses with expected results and document discrepancies.
  - For complex testing scenarios, include example responses and analysis in the notes.

- **Documentation:**  
  - Document each tested endpoint, including request structure, parameters, headers, and example responses.

