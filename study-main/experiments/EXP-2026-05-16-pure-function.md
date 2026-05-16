# EXP-2026-05-16 Pure Function Experiment

## Feature
Study Entry Submission

## Prompt Provided To AI
Using the following BDD requirements and Mermaid sequence diagram, write the logic for this feature as a pure function. It must have no side effects (stateless) and must return a predictable output.

### BDD Requirements
- As a student, I want to submit a study entry, so that my progress is saved and available for later review.
- Given a student provides a non-empty title and non-empty content
  When the student submits a new study entry
  Then the system returns a successful result with status "accepted" and a normalized entry payload
- Given a student provides an empty title or empty content
  When the student submits a new study entry
  Then the system returns a validation error with status "rejected" and a clear reason for each invalid field
- Given a student already has a submitted entry with the same normalized title on the same date
  When the student submits another entry with that title on that date
  Then the system returns a conflict error with status "rejected" and reason "duplicate_entry"

### Mermaid Diagram
```mermaid
sequenceDiagram
    autonumber
    actor Student
    participant UI as Presentation Layer (UI)
    participant App as Application Service
    participant PF as Pure Function: evaluate_entry_submission(input, existing_titles, date)
    participant Repo as Repository

    Student->>UI: Enter title and content, click Submit
    UI->>App: submitStudyEntry(rawInput)
    App->>PF: evaluate_entry_submission(input, existing_titles, date)

    alt input is valid and not duplicate
        PF-->>App: {status: "accepted", normalized_entry, reason: null}
        App->>Repo: save(normalized_entry)
        Repo-->>App: saved_entry_id
        App-->>UI: success response
        UI-->>Student: Show "Entry saved"
    else input invalid
        PF-->>App: {status: "rejected", errors, reason: "validation_failed"}
        App-->>UI: validation error response
        UI-->>Student: Show field-level validation errors
    else duplicate title on same date
        PF-->>App: {status: "rejected", reason: "duplicate_entry"}
        App-->>UI: conflict response
        UI-->>Student: Show duplicate warning
    end
```

## Experiment Result
The AI produced correct validation structure on the first try, but initially included persistence logic (repository save) inside the function.

## Did AI Succeed On First Try?
Partially. Logic was close, but not fully pure because side effects were mixed into the function.

## Did I Need To Adjust BDD Or Diagram?
Yes. I clarified the constraint that the function must only compute and return a decision object, with no database, API, file, or UI calls.

## Final Conclusion
With explicit pure-function constraints and clear BDD + Mermaid context, the AI generated a deterministic stateless solution.
