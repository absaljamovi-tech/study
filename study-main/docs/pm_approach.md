# Project Management Approach

We use a hybrid Scrumban approach: short 2-week planning cycles (Scrum-like cadence) combined with continuous task flow and WIP limits (Kanban). This gives predictable checkpoints for scope and demo while keeping flexibility for fast iteration, which is important in an AI-assisted project where requirements and implementation details can evolve during discovery.

Responsibility split is explicit. I own product direction, architecture decisions, task prioritization, and final code review/approval. The AI assistant supports execution by drafting boilerplate, generating unit tests, preparing refactoring proposals, and producing documentation drafts. Every AI-generated change must pass human review, follow AGENTS.md and docs constraints, and be validated with linting/tests before merge.
