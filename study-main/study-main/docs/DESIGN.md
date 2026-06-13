# Design Document

**Version**: 1.1  
**Last Updated**: 2026-06-13  
**Status**: Active  

## Purpose

This design document defines the UI contract and visual system for Study Entry Submission. It is intended to keep the interface predictable, accessible, and directly connected to the backend business logic without ad hoc styling or vague design decisions.

## Design System

### Visual Tokens

- **Primary color**: `#1F2937` (strong dark text and interface anchor)
- **Secondary color**: `#3B82F6` (action and focus state)
- **Success color**: `#16A34A`
- **Warning color**: `#F59E0B`
- **Error color**: `#DC2626`
- **Background**: `#F8FAFC`
- **Surface**: `#FFFFFF`
- **Border**: `#E2E8F0`

### Typography

- **Heading**: `Inter, 24px, 700` for page titles
- **Body**: `Inter, 16px, 400` for form labels and copy
- **Monospace**: `Menlo` / `Courier New` for JSON payload display

### Layout & Spacing

- **Spacing scale**: `4px, 8px, 16px, 24px, 32px`
- **Content width**: constrained to promote focus and readability
- **Form spacing**: 16px vertical rhythm between input components
- **Button padding**: 12px 20px

### States

- **Idle**: clear form prompt and field helper text
- **Loading**: spinner or disabled submit state
- **Success**: green success banner with normalized entry details
- **Validation error**: explicit field warnings and error banner
- **Duplicate entry**: warning callout with actionable advice

## Component Contract

### Study Entry Form

Input fields:
- `title`: single-line text input, required, normalized before duplicate check
- `content`: multi-line textarea, required
- `date`: date input, defaults to current date
- `submit`: primary call-to-action button

Output states:
- `accepted`: show normalized entry and append title to existing search keys
- `rejected.validation_failed`: show per-field validation errors
- `rejected.duplicate_entry`: show duplicate warning and preserve user input

### Feedback Panels

- `success`: visible when backend returns `status == "accepted"`
- `error`: visible when backend returns `reason == "validation_failed"`
- `warning`: visible when backend returns `reason == "duplicate_entry"`
- `payload`: debug-friendly JSON view of backend response

## Data Contract

The UI must call the backend pure function with this payload shape:

```python
{
    "title": str,
    "content": str,
}
```

Additional context:
- `existing_titles`: `List[str]` passed from the UI state to detect duplicates
- `date`: `str` in ISO format, e.g. `"2026-06-13"`

The backend response contract is:

```python
{
    "status": "accepted" | "rejected",
    "reason": None | "validation_failed" | "duplicate_entry",
    "normalized_entry": Optional[Dict[str, str]],
    "errors": Optional[Dict[str, str]],
}
```

## Accessibility Contract

- Every input must include an explicit label.
- Field helper text must describe expected input.
- Color states must not rely on color alone.
- The interface must support keyboard navigation and screen readers.

## Interaction Flows

1. **Valid entry**: user fills title + content → submit → backend returns accepted → UI shows success and normalized entry.
2. **Missing fields**: user submits incomplete form → backend returns validation errors → UI shows field-level warnings.
3. **Duplicate title**: user submits title already in `existing_titles` → backend returns duplicate warning → UI shows warning and preserves input.

## Implementation Plan

- Use Streamlit as the frontend runtime for rapid, accessible UI composition.
- Keep backend and UI separated: `evaluate_entry_submission` remains pure and contained in `src/study_entry_submission/strategy.py`.
- Use session state to store existing titles and render feedback state.

## AI-Native Rationale

This design is spec-driven rather than ad hoc. The UI is defined by a strict contract, visual tokens, and data-driven interaction flows, which eliminates vague "vibe code" and avoids generic div-based layouts.
