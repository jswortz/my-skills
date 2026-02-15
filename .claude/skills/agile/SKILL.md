---
name: agile
description: "Sprint-based agile development with parallel agent execution. Use when the user wants to run an agile sprint, plan sprint work, conduct standups, run retrospectives, manage a backlog, estimate story points, track velocity, or coordinate parallel development across multiple agents acting as Scrum team roles (Scrum Master, Product Owner, Tech Lead, Frontend Dev, Backend Dev, QA Engineer). Also use when the user mentions sprints, user stories, acceptance criteria, definition of done, kanban, or SAFe. Triggers on: 'run a sprint', 'sprint planning', 'standup', 'retrospective', 'backlog grooming', 'agile workflow', 'scrum team'."
---

# Agile Sprint Orchestration

Coordinate parallel development using Claude Code agents as a Scrum team.

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

## Sprint Workflow

### 1. Sprint Planning

Launch the scrum-master agent to initialize the sprint:

```
Task(subagent_type="scrum-master", prompt="Plan sprint N: [goal]. Break down these user stories into tasks, estimate story points, and create the sprint backlog using TaskCreate.")
```

The scrum-master will:
- Break user stories into implementable tasks via TaskCreate
- Set dependencies between tasks (blocked/blocking)
- Assign tasks to appropriate agent roles
- Define acceptance criteria for each story

### 2. Parallel Execution

Launch development agents in parallel for independent stories:

```
Task(subagent_type="frontend-dev", prompt="Implement [story]: [details]")
Task(subagent_type="backend-dev", prompt="Implement [story]: [details]")
Task(subagent_type="qa-engineer", prompt="Write acceptance tests for [story]")
```

### 3. Review & Integration

```
Task(subagent_type="tech-lead", prompt="Review implementation of [story] for architecture, code quality, and standards compliance")
Task(subagent_type="product-owner", prompt="Validate [story] against acceptance criteria: [criteria]")
```

### 4. Retrospective

```
Task(subagent_type="scrum-master", prompt="Run sprint N retrospective. Review completed tasks, velocity, blockers encountered, and generate action items for next sprint.")
```

## Agent Roles

| Agent | Role | Focus |
|-------|------|-------|
| `scrum-master` | Facilitator | Ceremonies, impediments, process |
| `product-owner` | Value owner | Backlog, acceptance criteria, priorities |
| `tech-lead` | Architecture | Design decisions, code review, standards |
| `frontend-dev` | UI developer | Frontend implementation |
| `backend-dev` | API developer | Backend implementation, data layer |
| `qa-engineer` | Quality | Testing, validation, bug tracking |

## Velocity Tracking

Use the knowledge graph to persist sprint metrics:

```
mcp__memory__create_entities([{
  name: "Sprint N",
  entityType: "sprint",
  observations: [
    "Planned points: 40",
    "Completed points: 35",
    "Velocity: 35",
    "Goal: [sprint goal]",
    "Status: completed"
  ]
}])
```

Query historical velocity:
```
mcp__memory__search_nodes("sprint velocity")
```

## Kanban Mode

For continuous flow instead of sprints:
- Use `product-owner` to maintain a prioritized backlog
- Set WIP limits: max 2 in-progress tasks per agent
- Use `scrum-master` as flow master to monitor cycle time

## Scaling (SAFe)

For multi-team coordination, see [references/safe.md](references/safe.md).

## Jira Integration

If the `mcp-atlassian` MCP server is configured, agents can:
- Read/update Jira issues and sprints
- Sync task status with Jira boards
- Pull acceptance criteria from Jira stories
- Create sub-tasks in Jira from sprint planning

See [references/jira-integration.md](references/jira-integration.md) for setup.
