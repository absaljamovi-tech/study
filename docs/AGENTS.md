# AGENTS.md - Engineering Harness for AI-Native Development

**Version**: 1.0  
**Last Updated**: 2026-05-15  
**Status**: Active  

## 1. Purpose

This AGENTS.md file defines the machine-readable constraints, architectural guardrails, and operational boundaries for AI agents and autonomous development processes in this repository. It replaces traditional requirement documents by providing executable guidance for AI-driven decision-making.

## 2. Core Principles

### Principle 1: Architectural Integrity
- All changes must maintain the defined architecture (see Section 4)
- No sideways refactoring without explicit AGENTS.md amendment
- Architecture reviews required for changes spanning 3+ components

### Principle 2: Measurable Quality
- All code contributions must include automated tests
- Test coverage must not decrease with any PR
- Performance regressions require explicit trade-off documentation

### Principle 3: Auditability
- Every decision made by an AI agent must be traceable to an AGENTS.md rule
- Changes that violate constraints are automatically rejected
- Technical debt is explicitly tracked (see Section 7)

### Principle 4: Sustainable Pace
- Tasks should be decomposable into <8 hour increments
- No unlimited scope work; complexity requires task decomposition
- Agent autonomy bounded by clear acceptance criteria

## 3. Repository Metadata

```yaml
Repository: absoljamovi-tech/study
Owner: absaljamovi-tech
Languages: ["JavaScript", "Python", "Markdown"]
Team Size: Solo developer + AI agents
Project Type: Educational AI-Native Development
Deployment Target: GitHub Pages / Cloud (TBD)
SLA: N/A (Educational)
```

## 4. Architectural Constraints

### 4.1 Directory Structure (Non-Negotiable)

```
project-root/
├── docs/                    # Documentation & specifications
│   ├── AGENTS.md           # This file
│   ├── pm_approach.md      # Project management methodology
│   ├── DESIGN.md           # Architecture & design decisions
│   ├── domain_model.md     # Data models & domain concepts
│   └── api_spec.md         # API contracts (if applicable)
├── src/                     # Source code
│   ├── components/         # Reusable modules
│   ├── services/           # Business logic
│   ├── utils/              # Utilities & helpers
│   └── index.ts/js         # Main entry point
├── tests/                   # Test suite
│   ├── unit/              # Unit tests
│   ├── integration/        # Integration tests
│   └── fixtures/          # Test data
├── .github/
│   ├── workflows/         # CI/CD pipelines
│   └── ISSUE_TEMPLATE/    # Issue templates
├── .gitignore
├── README.md
└── package.json / requirements.txt
```

### 4.2 Language & Technology Stack

| Layer | Technology | Rationale |
|-------|-----------|----------|
| **Documentation** | Markdown | Universal, version-control friendly |
| **Backend Logic** | JavaScript/TypeScript or Python | Educational flexibility |
| **Testing** | Jest (JS) / Pytest (Python) | Industry standard, easy CI integration |
| **CI/CD** | GitHub Actions | Native GitHub integration |
| **Version Control** | Git + GitHub | Distributed, industry standard |

**Constraint**: No framework lock-in without explicit approval. Use vanilla language features when possible.

### 4.3 Code Quality Standards

1. **Linting**: ESLint (JS) or pylint (Python)
   - Zero tolerance for critical issues
   - Warnings must be documented
   
2. **Testing**:
   - Minimum 70% code coverage
   - All public APIs must have tests
   - Test file co-location: `src/module.ts` → `tests/unit/module.test.ts`
   
3. **Documentation**:
   - Every module requires a docstring
   - Complex logic needs inline comments
   - Public APIs documented with examples

4. **Type Safety** (if using TypeScript):
   - No `any` types without TSIgnore comment
   - Strict mode enabled
   - Interface-based contracts

## 5. Operational Boundaries

### 5.1 Task Decomposition Rules

AI agents must decompose work according to these criteria:

| Complexity | Max Time | Example | Decompose If |
|-----------|----------|---------|---------------|
| Simple | 2 hours | Add a utility function | Estimated > 2h |
| Medium | 4 hours | Implement a component | Estimated > 4h |
| Complex | 8 hours | Refactor a service | Estimated > 8h |
| Epic | Multi-sprint | New feature with design | Always break down |

**Rule**: If task cannot be completed in 8 hours, create 2-3 dependent issues instead of one large PR.

### 5.2 Git Workflow

```
Main Branch Flow:

main (production-ready)
 ↑
 ├← develop (staging)
    ↑
    ├← feature/task-123 (AI agent working branch)
         ├ Commit atomic changes
         ├ Include issue reference (#123)
         ├ Squash before PR if > 5 commits
         └ Create PR with checklist
```

**PR Requirements**:
- [ ] Linked to GitHub Issue
- [ ] Tests pass (100% automated)
- [ ] No test coverage decrease
- [ ] Documentation updated
- [ ] Self-reviewed against AGENTS.md checklist

### 5.3 Issue Linking Protocol

Every PR MUST be linked to a GitHub Issue using:
- PR description includes: `Closes #123` or `Resolves #123`
- Issue title matches feature/fix scope
- Issue includes acceptance criteria
- Labels applied: `type:bug`, `type:feature`, `priority:high`, etc.

**Automation**: GitHub will automatically close issues when PR is merged.

## 6. AI Agent Permissions & Constraints

### 6.1 What Agents CAN Do (Autonomous)
- Create branches and commits per this AGENTS.md
- Create GitHub Issues with proper templates
- Create PRs with self-review checklists
- Write unit tests and documentation
- Update non-critical AGENTS.md sections (v1.x patch updates)

### 6.2 What Agents MUST Escalate (Human Decision)
- Changes to repository structure (Section 4.1)
- Technology stack changes (Section 4.2)
- AGENTS.md major version updates (v2.0+)
- Breaking API changes
- Security-related modifications
- Decisions conflicting with multiple AGENTS.md rules

### 6.3 Blocked Operations
- Merging own PRs (requires human review)
- Deleting branches on main/develop
- Modifying GitHub Actions workflows
- Changing repository settings
- Force-pushing to protected branches

## 7. Technical Debt Management

### 7.1 Debt Tracking

Technical debt is tracked via GitHub Issues with label `tech-debt`:

```markdown
## Technical Debt Register

Current Debt: [List issues with tech-debt label]
Debt/Revenue Ratio Target: <10%
Monitored Metrics:
- Code complexity (cyclomatic complexity < 5)
- Dependency count (minimize transitive deps)
- Test coverage (maintain ≥70%)
```

### 7.2 Debt Repayment Policy

- **Minor debt**: Address within 1 sprint
- **Major debt**: Create epic, schedule across 2-3 sprints
- **Critical debt**: Blocks new features until resolved

## 8. Continuous Integration & Deployment

### 8.1 Mandatory CI Checks

All PRs must pass:
1. ✅ Linting (ESLint / pylint)
2. ✅ Unit tests (>70% coverage)
3. ✅ Type checking (if TypeScript)
4. ✅ Security scan (dependency vulnerabilities)
5. ✅ AGENTS.md compliance check

### 8.2 GitHub Actions Workflows

**Workflows Location**: `.github/workflows/`

Required workflows:
- `test.yml` - Run tests on every PR
- `lint.yml` - Code quality checks
- `security.yml` - Dependency scanning
- `coverage.yml` - Coverage trend reporting

## 9. Documentation Standards

All documentation must follow this structure:

```markdown
# Document Title

**Version**: X.Y  
**Last Updated**: YYYY-MM-DD  
**Status**: Draft | Review | Active | Deprecated  

## Purpose
[Why this doc exists]

## Scope
[What's in/out of scope]

## Content
[Main body]

## Decision Log
| Date | Decision | Rationale |

## References
- [Link to related docs]
```

## 10. Review & Amendment Process

### 10.1 AGENTS.md Amendments

- **v1.x patches**: AI agents can update directly (bug fixes, clarifications)
- **v2.0+ major changes**: Require PR + human review + decision log entry
- **Quarterly review**: Full AGENTS.md review and update

### 10.2 Change Log

```yaml
Version History:
  1.0:
    date: 2026-05-15
    author: absaljamovi-tech
    changes:
      - Initial AGENTS.md creation
      - Defined architectural constraints
      - Established operational boundaries
```

## 11. Success Metrics

The following metrics indicate healthy adherence to this harness:

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Avg PR review time | <24h | TBD | TBD |
| Test coverage | ≥70% | TBD | TBD |
| Failed CI checks/month | <5% | TBD | TBD |
| AGENTS.md compliance rate | 100% | TBD | TBD |
| Time to deploy from merge | <4h | TBD | TBD |
| Technical debt (days to repay) | <30 | TBD | TBD |

## 12. Quick Reference Checklist

**For every PR:**
- [ ] Linked to GitHub Issue with `Closes #XXX`
- [ ] Branch follows naming convention: `feature/` or `fix/`
- [ ] Commit messages reference issue (#123)
- [ ] Tests added/updated (70%+ coverage)
- [ ] Documentation updated
- [ ] No AGENTS.md violations
- [ ] Linting passes
- [ ] Type checking passes (if applicable)
- [ ] Self-reviewed against this checklist

---

**Questions?** Create a GitHub Issue with label `question` and tag @absaljamovi-tech.

**To update this AGENTS.md**: Create PR with detailed rationale in description. Changes require explicit acknowledgment of impact.
