# AGENTS.md - Engineering Harness Specification

**Version**: 1.0  
**Last Updated**: 2026-05-15  
**Course**: Software Engineering (Part 1) - B-750-01  
**Repository**: absaljamovi-tech/study

---

## 1. Purpose

This document defines the **Engineering Harness**—a machine-readable specification that constrains AI agents to maintain architectural integrity, prevent technical debt, and ensure deliverables align with course objectives.

Instead of writing massive requirement specifications for humans, we create **strict contracts** that guide autonomous AI agents.

---

## 2. Project Scope

### Objective
Build a **feature-complete, AI-assisted software project** demonstrating software engineering principles: requirements analysis, architectural design, design patterns, component-based development, and quality assurance.

### Core Deliverables (Aligned with Course Assignments)
1. **Assignment 2**: Project Planning & Metrics (SWE Project Planning)
2. **Assignment 3**: Requirements & UML (AI-Ready Requirements and UML-as-Code)
3. **Assignment 4**: Architectural Patterns (Structural Integrity)
4. **Assignment 5**: UI/Frontend Orchestration (Spec-Driven Development)

### Technology Stack
- **Language**: Python 3.10+ (or TypeScript/Java, to be determined)
- **Frontend Framework**: Streamlit / Gradio / React
- **Design Patterns**: GoF (Gang of Four) patterns
- **Architecture**: Microservices-ready component model
- **SCM**: Git + GitHub (branching strategy: Git Flow)
- **CI/CD**: GitHub Actions

---

## 3. AI Agent Role & Constraints

### What AI Agents Can Do ✅
- Generate boilerplate code following strict templates
- Implement design patterns (Factory, Strategy, Observer, etc.)
- Create test cases and unit tests
- Generate documentation (README, API docs, architecture diagrams)
- Suggest code optimizations and refactoring
- Auto-generate UI components from DESIGN.md specifications

### What AI Agents CANNOT Do ❌
- Deviate from architecture defined in DESIGN.md
- Introduce new dependencies without approval
- Write "magical" or hallucinated code outside defined contracts
- Skip test coverage requirements
- Modify architectural boundaries or layer violations
- Create code that violates SOLID principles

### Quality Gates (Enforcement)
```
AI-Generated Code → Linting (ESLint/Pylint) → Unit Tests → Human Review → Merge
```

**All AI-generated code must**:
1. Pass linting checks (0 errors, <5 warnings)
2. Pass unit tests (≥80% code coverage)
3. Pass architecture validation (layer boundaries respected)
4. Receive human code review before merge
5. Include documentation strings

---

## 4. Architecture Blueprint

### Layered Architecture (Clean Code)

```
┌─────────────────────────────────────────┐
│   Presentation Layer (UI)               │
│   (Streamlit/Gradio/React)              │
│   - User Interface Components           │
│   - Form Validation                     │
│   - State Management                    │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│   Application Layer                     │
│   - Use Cases / Business Logic          │
│   - Orchestration                       │
│   - Request/Response Handling           │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│   Domain Layer                          │
│   - Entities                            │
│   - Value Objects                       │
│   - Domain Rules                        │
│   - Design Patterns Implementation      │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│   Infrastructure Layer                  │
│   - Databases / APIs                    │
│   - External Services                   │
│   - File I/O                            │
└─────────────────────────────────────────┘
```

### Directory Structure

```
study/
├── docs/
│   ├── pm_approach.md              # Project management strategy
│   ├── DESIGN.md                   # UI/Architecture design contracts
│   └── architecture/
│       ├── domain_model.md         # Entity relationships
│       └── design_patterns.md      # Applied GoF patterns
├── src/
│   ├── domain/                     # Domain layer (Pure functions)
│   │   ├── entities/
│   │   ├── value_objects/
│   │   └── rules/
│   ├── application/                # Application layer (Use cases)
│   │   └── services/
│   ├── infrastructure/             # Infrastructure layer
│   │   ├── repositories/
│   │   └── external_services/
│   └── presentation/               # UI layer
│       └── components/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── .github/
│   └── workflows/
│       ├── lint.yml
│       ├── test.yml
│       └── deploy.yml
└── README.md
```

---

## 5. Design Patterns (GoF) - Mandatory Implementation

### Pattern Selection Rules
**Rule 1**: Use **Strategy Pattern** for interchangeable algorithms  
**Rule 2**: Use **Factory Pattern** for object creation logic  
**Rule 3**: Use **Observer Pattern** for event handling  
**Rule 4**: Use **Singleton Pattern** only for stateless utilities  
**Rule 5**: Document why each pattern was chosen in code comments  

### Example Constraint
```python
# ✅ GOOD: Factory Pattern for creating different report types
class ReportFactory:
    @staticmethod
    def create_report(report_type: str) -> Report:
        if report_type == "pdf":
            return PDFReport()
        elif report_type == "excel":
            return ExcelReport()
        else:
            raise ValueError(f"Unknown report type: {report_type}")

# ❌ BAD: Direct instantiation (violates DRY + Factory pattern)
if report_type == "pdf":
    report = PDFReport()
elif report_type == "excel":
    report = ExcelReport()
```

---

## 6. Code Quality Standards

### Linting & Formatting
- **Python**: Black (line length: 88), Pylint (8.0+ score)
- **TypeScript**: ESLint + Prettier
- **Java**: Google Style Guide

### Testing Requirements
- **Unit Tests**: ≥80% code coverage
- **Test Framework**: pytest (Python) / Jest (TypeScript) / JUnit (Java)
- **Test Pattern**: Arrange-Act-Assert (AAA)

### Documentation
- **Docstrings**: Google/NumPy style for all public functions
- **Comments**: Explain WHY, not WHAT (code explains what)
- **README**: Mandatory for each module
- **API Docs**: Auto-generated from docstrings

### SOLID Principles (Enforced)
| Principle | Rule | Example |
|-----------|------|---------|
| **S**ingle Responsibility | One reason to change | `UserService` handles users only, not emails |
| **O**pen/Closed | Open for extension, closed for modification | Use inheritance/interfaces, not if-else chains |
| **L**iskov Substitution | Derived classes must substitute base classes | `PDFReport` can replace `Report` interface |
| **I**nterface Segregation | Many specific interfaces vs. one generic | `Payable` interface instead of `Worker` |
| **D**ependency Inversion | Depend on abstractions, not concretions | Inject services via constructor |

---

## 7. AI Prompt Templates (For Developers Using AI)

### Template 1: Generate Domain Entity
```
Create a Python class for [ENTITY_NAME] with:
- Pure attributes (no business logic)
- Type hints for all parameters
- Docstring in Google style
- Follow the domain model in docs/architecture/domain_model.md
- No external dependencies
```

### Template 2: Implement Design Pattern
```
Implement the [PATTERN_NAME] pattern for [USE_CASE].
Requirements:
- Follow GoF definition strictly
- Include unit tests (≥80% coverage)
- Document the pattern choice in code comments
- Respect layer boundaries defined in AGENTS.md
- Use dependency injection for testability
```

### Template 3: Generate UI Component
```
Create a Streamlit component for [FEATURE]:
- Use DESIGN.md specification located at docs/DESIGN.md
- Follow accessibility guidelines (WCAG 2.1 AA)
- Include input validation and error handling
- Add unit tests for business logic
- Connect to backend via [API_ENDPOINT]
```

---

## 8. Git Workflow & Branching Strategy

### Branching Model: Git Flow

```
main (production)
  └─ release branches (v1.0.0-rc)
       └─ develop (integration)
            ├─ feature/assignment-2-project-planning
            ├─ feature/assignment-3-uml-design
            ├─ feature/assignment-4-design-patterns
            ├─ feature/assignment-5-ui-orchestration
            ├─ bugfix/issue-XXX
            └─ docs/architecture-updates
```

### Commit Message Convention

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`  
**Scope**: Feature area (e.g., `domain`, `ui`, `patterns`)  
**Subject**: Imperative mood, < 50 chars  

**Example**:
```
feat(patterns): Implement Factory pattern for report generation

- Add ReportFactory class in domain/factories/
- Support PDF, Excel, and JSON report types
- Add 5 unit tests covering all branches

Closes #15
```

### Pull Request Checklist (AI-Generated PRs must verify)
- [ ] Branch follows naming convention
- [ ] Commit messages follow convention
- [ ] All tests pass locally
- [ ] Code coverage ≥80%
- [ ] No linting errors
- [ ] Docstrings added
- [ ] Links to related issues
- [ ] Ready for human review

---

## 9. Definition of Done (DoD)

A task is "Done" when:

- ✅ Code written & reviewed by human
- ✅ Unit tests: ≥80% coverage, all passing
- ✅ Linting: 0 errors, <5 warnings
- ✅ Documentation: README + docstrings complete
- ✅ Design patterns: Applied & documented (if applicable)
- ✅ Architecture: No layer violations
- ✅ PR merged to develop branch
- ✅ Issue linked & closed

---

## 10. Escalation & Hallucination Detection

### Red Flags for AI Hallucinations
🚨 Code that doesn't follow defined patterns  
🚨 New dependencies introduced without approval  
🚨 Layer violations (e.g., UI calling database directly)  
🚨 Missing error handling  
🚨 Code that can't be explained by the pattern template  
🚨 Functions with >100 lines (violation of SRP)  

### Response: If Hallucination Detected
1. **Request Changes** on PR with specific violations
2. **Clarify Constraints** by re-running with updated AGENTS.md
3. **Add Test Case** to prevent regression
4. **Document** the issue for future prompt refinement

---

## 11. Review Checklist (For Human Reviewers)

```markdown
## Code Review Checklist

- [ ] Code follows architecture layers (no cross-layer calls)
- [ ] Design pattern applied correctly (if required)
- [ ] SOLID principles respected
- [ ] Functions <100 lines (SRP)
- [ ] Docstrings complete
- [ ] Tests ≥80% coverage
- [ ] No external dependencies added
- [ ] Linting passes
- [ ] Error handling implemented
- [ ] Database queries optimized (if applicable)
```

---

## 12. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Code Coverage** | ≥80% | pytest coverage report |
| **Linting Score** | 8.0+ (Pylint) | CI/CD pipeline |
| **Pattern Adherence** | 100% | Code review checklist |
| **Hallucination Rate** | <5% | Review feedback frequency |
| **PR Merge Time** | <24 hours | GitHub metrics |
| **Test Pass Rate** | 100% | CI/CD pipeline |
| **Documentation** | 100% of functions | Docstring coverage |

---

## 13. Course Alignment

### Assignment Mapping

| Assignment | AGENTS.md Component | Deliverable |
|------------|-------------------|------------|
| **#2** | Project Planning | SWE metrics + Kanban board |
| **#3** | Domain Layer + DESIGN.md | UML diagrams + requirements |
| **#4** | Design Patterns | GoF implementation + tests |
| **#5** | Presentation Layer | UI components + DESIGN.md |

---

## 14. How to Use This Document

### For Developers
1. Read sections 2-4 (scope, architecture, constraints)
2. Use templates in section 7 when asking AI for code
3. Check section 8-9 before committing
4. Review section 11 checklist before pushing PR

### For AI Agents
1. Parse this file at every code generation request
2. Validate against constraints in sections 3, 5-6
3. Ensure all code follows architecture in section 4
4. Include tests per section 6 requirements
5. Document decisions per section 7 templates

### For Instructors
- Use section 12 (metrics) to evaluate project quality
- Review section 10 (hallucination detection) for AI assessment
- Cross-reference section 13 with course rubrics

---

## 15. Updates & Versioning

**Current Version**: 1.0  
**Next Review**: After Assignment 3 (UML-as-Code)  
**Modification Process**:
1. Propose changes in GitHub Issue (label: `harness-update`)
2. Discuss with team
3. Update AGENTS.md on feature branch
4. Merge via Pull Request with detailed changelog

---

## 16. References

- **OpenAI Harness Engineering**: AI prompt engineering best practices
- **Clean Code** by Robert C. Martin: Architecture & SOLID principles
- **Design Patterns** by Gang of Four: Reusable design solutions
- **Agents.md Specification**: Course material on machine-readable agent constraints
- **Course Material**: Software Engineering (Part 1) - B-750-01

---

**Last Modified**: 2026-05-15 by absaljamovi-tech  
**Status**: Active ✅  
**Next Version**: AGENTS.md v1.1 (Post-Assignment 3)
