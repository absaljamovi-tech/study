# AGENTS.md

## Project Core Concept
- Build an AI-assisted software product for the Software Engineering course.
- Follow layered architecture: presentation -> application -> domain -> infrastructure.
- Use design patterns (Strategy, Factory, Observer) where they fit naturally.
- Deliver an MVP first, then iterate with measurable quality improvements.

## Rules For AI Agents
- Primary language: Python 3.10+.
- Coding style: PEP 8, type hints for public APIs, concise docstrings for public functions/classes.
- Keep functions focused and small; avoid layer boundary violations.
- Do not add new dependencies unless explicitly approved.
- Do not modify architecture decisions without explicit approval.
- Add or update tests for all non-trivial code changes.
- Prefer clear, deterministic code over "smart" shortcuts.

## Required Context Loading
- Always read the /docs folder before proposing or generating code.
- Treat /docs as the source of truth for requirements, roadmap, and architecture.
- At minimum, check these files first:
  - /docs/DESIGN.md
  - /docs/domain_model.md
  - /docs/pm_approach.md
  - /docs/plans/roadmap.md
