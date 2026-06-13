# Study Entry Submission Module

## Pattern Used: Strategy

### Why Strategy?
The Strategy pattern is ideal for this feature because it allows us to encapsulate different validation and evaluation algorithms (valid, invalid, duplicate) as interchangeable objects. This makes the business logic extensible and testable, and prevents the growth of complex if-else chains. If new validation rules or submission types are needed, they can be added as new strategies without modifying the core logic.

### How It Works
- The module exposes a pure function `evaluate_entry_submission` that selects and delegates to the appropriate strategy based on input.
- Each strategy implements the `evaluate` method for a specific case (valid, invalid, duplicate).
- The context object (`SubmissionContext`) allows dynamic switching of strategies if needed.

### Module Interactions
- The module is called by the Application Layer when a user submits a study entry.
- It does not perform any I/O or persistence; it only returns a decision object.
- The result is then handled by the application (e.g., saved to DB, shown to user, or error displayed.)

### UI Integration
- The frontend app is implemented in `src/study_entry_submission/app.py`.
- The UI uses the pure function `evaluate_entry_submission(input_data, existing_titles, date)` to keep business logic centralized.
- The frontend is intentionally separated from the submission logic to preserve the Strategy pattern and enable testability.

### Running the frontend
1. Install the UI dependency: `pip install -r requirements.txt`
2. Start the app from the project root:
   `streamlit run src/study_entry_submission/app.py`

### AGENTS.md Compliance
- Pure function, no side effects.
- Follows PEP 8, type hints, and docstring conventions.
- No new dependencies introduced in the core module.
- Extensible and testable by design.
