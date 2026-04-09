---
name: agile
description: "Sprint-based agile development with parallel agent execution. Use when the user wants to run an agile sprint, plan sprint work, conduct standups, run retrospectives, manage a backlog, estimate story points, track velocity, or coordinate parallel development across multiple agents acting as Scrum team roles (Scrum Master, Product Owner, Tech Lead, Frontend Dev, Backend Dev, QA Engineer). Also use when the user mentions sprints, user stories, acceptance criteria, definition of done, kanban, or SAFe. Triggers on: 'run a sprint', 'sprint planning', 'standup', 'retrospective', 'backlog grooming', 'agile workflow', 'scrum team'."
---

# Agile Sprint Orchestration

Coordinate parallel development using Gemini CLI agents as a Scrum team.

## Quick Reference

| Ceremony | Agent | Command |
|----------|-------|---------|
| Sprint Planning | scrum-master | Plan sprint scope, create tasks |
| Daily Standup | scrum-master | Collect status from all agents |
| Development | frontend-dev, backend-dev | Parallel feature implementation |
| Code Review | tech-lead | Architecture review, standards |
| Testing | qa-engineer | Acceptance tests, regression |
| Sprint Review | product-owner | Validate acceptance criteria |
| Retrospective | scrum-master | What went well/improve/actions |


## Advanced Details & Examples
For advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).
