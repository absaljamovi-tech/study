# Project Management Approach: Scrum vs Kanban

## Executive Summary
This document outlines the project management methodology for our AI-Native development initiative, comparing Scrum and Kanban frameworks to determine the optimal approach for autonomous AI agent orchestration.

---

## 1. Scrum Approach

### Overview
Scrum is a **time-boxed, iterative framework** with fixed sprint cycles, predefined roles, and structured ceremonies.

### Key Characteristics
- **Sprint Duration**: 1-4 weeks (we'll use 2 weeks)
- **Fixed Cadence**: Sprint Planning → Execution → Daily Standups → Sprint Review → Sprint Retrospective
- **Predictability**: Fixed scope per sprint, measurable velocity
- **Team Roles**: Product Owner, Scrum Master, Development Team

### Artifacts
- **Product Backlog**: Prioritized feature list
- **Sprint Backlog**: Items committed for current sprint
- **Increment**: Potentially shippable product at end of sprint

### Advantages for AI-Native Development
✅ Clear sprint boundaries for AI agent training cycles  
✅ Structured feedback loops through sprint reviews  
✅ Velocity tracking helps predict AI model refinement timelines  
✅ Sprint retrospectives improve agent prompting & constraints  

### Disadvantages
❌ Less flexible for rapid AI model improvements  
❌ Overhead of ceremonies may slow down fast-moving dev cycles  
❌ Fixed scope may not suit experimental AI features  

---

## 2. Kanban Approach

### Overview
Kanban is a **continuous flow framework** emphasizing WIP (Work In Progress) limits, flow efficiency, and just-in-time delivery.

### Key Characteristics
- **Continuous Delivery**: Work flows through stages without fixed iterations
- **WIP Limits**: Restricts work in progress at each stage
- **Visualization**: Transparent workflow (To Do → In Progress → Review → Done)
- **Pull System**: Work is pulled when capacity exists, not pushed

### Workflow States
1. **To Do**: Backlog items waiting to start
2. **In Progress**: Active development
3. **Review**: Code/design review stage
4. **Testing**: QA and validation
5. **Done**: Completed and deployed

### Advantages for AI-Native Development
✅ Flexible for experimental AI features  
✅ Continuous delivery aligns with AI agent iterations  
✅ WIP limits prevent agent context-switching overload  
✅ Faster feedback cycles for prompt optimization  
✅ Better for variable workload types  

### Disadvantages
❌ Less predictable delivery timelines  
❌ Requires discipline to maintain WIP limits  
❌ Harder to estimate project completion dates  

---

## 3. Recommended Hybrid Approach: Scrumban

For our **AI-Native Engineering Harness**, we adopt **Scrumban**:

### Structure
- **Macro-cycles**: 2-week sprints for milestones (Scrum)
- **Micro-flows**: Continuous Kanban board for daily tasks
- **WIP Limits**: Max 3 items per stage
- **Daily Standups**: 15 minutes (async-friendly)
- **Sprint Reviews**: Every 2 weeks with stakeholders

### Workflow

```
Product Backlog (Prioritized)
    ↓
Sprint Planning (Day 1 of Sprint)
    ↓
Kanban Board: To Do → In Progress → Review → Testing → Done
    ↓
Daily Monitoring (WIP limits enforced)
    ↓
Sprint Review + Retrospective (Day 10)
    ↓
Next Sprint Planning
```

### Why Scrumban for AI-Native?
1. **Structured Planning**: Sprints provide cadence for AI model updates
2. **Flexible Execution**: Kanban allows rapid AI prompt iterations
3. **Flow Efficiency**: WIP limits prevent agent hallucinations from compounding
4. **Continuous Feedback**: Daily Kanban + Sprint Reviews = rapid learning
5. **Scalability**: Agents work in defined boundaries within continuous flow

---

## 4. AI Agent Integration

### Agent Responsibilities (Within Engineering Harness)
- **Code Generation**: Execute tasks defined in AGENTS.md specification
- **Constraint Adherence**: Respect architecture boundaries and design patterns
- **Self-Testing**: Auto-run tests before pulling to Review stage
- **Documentation**: Update AGENTS.md as capability expands

### Human Responsibilities
- **Harness Design**: Define constraints, architecture, contracts (DESIGN.md, AGENTS.md)
- **Review Gate**: Approve AI-generated code before merge
- **Model Refinement**: Adjust prompts and constraints based on agent performance
- **Strategic Decisions**: Backlog prioritization, sprint goals

---

## 5. Metrics for Success

### Scrum Metrics
- **Velocity**: Story points completed per sprint (target: consistent ±10%)
- **Sprint Burndown**: Visual progress toward sprint goal
- **Cycle Time**: Days from task start to completion

### Kanban Metrics
- **Lead Time**: Days from backlog to Done
- **Throughput**: Items completed per day/week
- **WIP Compliance**: % of time WIP limits are respected

### AI-Specific Metrics
- **Agent Success Rate**: % of auto-generated code passing review
- **Hallucination Index**: Critical bugs traced to AI context confusion
- **Constraint Violations**: % of code violating AGENTS.md rules
- **Prompt Effectiveness**: Improvements in agent output quality per iteration

---

## 6. Implementation Timeline

| Phase | Duration | Activities |
|-------|----------|------------|
| **Phase 1: Setup** | Week 1 | Define AGENTS.md, DESIGN.md, create Kanban board |
| **Phase 2: Sprint 1** | Weeks 2-3 | Build core backend with AI assistance |
| **Phase 3: Sprint 2** | Weeks 4-5 | Implement architectural patterns (Assignment 4) |
| **Phase 4: Sprint 3** | Weeks 6-7 | UI/Frontend orchestration (Assignment 5) |
| **Phase 5: Refinement** | Weeks 8-9 | Polish, testing, agent prompt optimization |
| **Phase 6: Review** | Week 10 | Final sprint review, course submission |

---

## 7. Decision: Scrumban Selected ✅

**Rationale**: For a 10-week Software Engineering course with AI-assisted development, Scrumban provides:
- Structured milestones (sprints) aligned with course deliverables
- Flexible daily workflow for AI iteration and experimentation
- Clear metrics and visibility for both instructors and automated agents
- Scalability from individual developer to multi-agent teams

---

## References
- Scrum Guide: https://scrumguides.org/
- Kanban Method: https://kanbanize.com/kanban-resources/getting-started/what-is-kanban
- SAFe Agile Framework: https://www.scaledagileframework.com/
- AI-Native Development: "Agents.md Specification" (Course Materials)
