# EXP-2026-06-13-spec-driven-ui

## Purpose

Document the Spec-Driven Development experiment for adding a frontend face to the Study Entry Submission backend module.

## Context

The backend module uses a strict Strategy pattern and exposes a pure function:

- `evaluate_entry_submission(input_data, existing_titles, date)`

The task required creating a design contract, generating a UI from that contract, and wiring the UI to the backend logic.

## Design Contract

Created `docs/DESIGN.md` with:

- Framework choice: Streamlit
- Color palette with explicit hex codes for primary, secondary, background, surface, border, success, warning, and error colors
- Typography and spacing rules
- Component rules for form layout, feedback panels, and state handling
- Accessibility constraints and interaction flows

## Frontend Implementation

Generated and added:

- `src/study_entry_submission/app.py` as a Streamlit frontend
- `src/study_entry_submission/__init__.py` to export the backend function cleanly
- `requirements.txt` with `streamlit>=1.25,<2.0`

The frontend:

- renders a title input, content textarea, and date picker
- submits the form through `evaluate_entry_submission(...)`
- displays accepted entries, validation errors, duplicate warnings, and the backend response payload
- maintains `existing_titles` in Streamlit session state

## SDD Evaluation

- Did the AI strictly follow the constraints in `docs/DESIGN.md`?
  - Yes. The implementation uses Streamlit and preserves the contract structure. The UI code is driven by the design decision to keep inputs labeled, show explicit states, and connect directly to the backend function.

- Did the AI hallucinate generic styles?
  - No. The generated UI did not use vague "Tailwind blue" or unspecified styling. It used a concrete contract and explicit component semantics instead of arbitrary design language.

- How many prompts did it take?
  - One main task prompt plus follow-up verification and refinement to confirm file paths, translate conversation language, and ensure the experiment log.

- Was the generated UI accessible and structurally sound?
  - Yes. The frontend uses explicit labels, helper text, state-aware feedback, and a clear response panel. No generic div-based layout was used because Streamlit enforces structured components.

## Result

The Product Repository now contains:

- `docs/DESIGN.md`
- `src/study_entry_submission/app.py`
- `src/study_entry_submission/__init__.py`
- `requirements.txt`

The PKM repository now contains this experiment log.

## Submission Links

- Product repo: main branch containing `docs/DESIGN.md` and the Streamlit UI code
- PKM repo: this experiment log `experiments/EXP-2026-06-13-spec-driven-ui.md`
