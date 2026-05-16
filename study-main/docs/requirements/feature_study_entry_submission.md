# Feature: Study Entry Submission

## User Story
As a student, I want to submit a study entry, so that my progress is saved and available for later review.

## Acceptance Criteria (BDD)

### AC1: Successful submission with valid input
Given a student provides a non-empty title and non-empty content
When the student submits a new study entry
Then the system returns a successful result with status "accepted" and a normalized entry payload

### AC2: Rejection on missing required fields
Given a student provides an empty title or empty content
When the student submits a new study entry
Then the system returns a validation error with status "rejected" and a clear reason for each invalid field

### AC3: Rejection on duplicate title for the same day
Given a student already has a submitted entry with the same normalized title on the same date
When the student submits another entry with that title on that date
Then the system returns a conflict error with status "rejected" and reason "duplicate_entry"
