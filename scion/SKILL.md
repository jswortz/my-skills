---
name: scion
description: A specialized skill for building and managing **Supervised Agent Teams** using Google's Agent Development Kit (ADK). SCION emphasizes safety, role spe...
---

# SCION (Safe Cloud Intelligent Orchestration Network)

A specialized skill for building and managing **Supervised Agent Teams** using Google's Agent Development Kit (ADK). SCION emphasizes safety, role specialization, and explicit hand-offs.

## Core Mandates

1.  **Supervisor-Worker Architecture**: Always use a lead **Supervisor** agent to orchestrate specialized **Worker** agents.
2.  **Specialization**: Each Worker should have a narrow, expert-level instruction set and a minimal set of tools.
3.  **Explicit Hand-offs**: Use the `transfer_to_agent` tool (or ADK sub-agent routing) with clear announcements of role changes.
4.  **Shared State Management**: Leverage `tool_context.state` to share data (e.g., file URIs, user preferences) across the team.

## Architecture Pattern

```
      User Request
          ↓
    [Supervisor Agent]
    (Orchestration & Routing)
          ↓
    ┌─────┴─────┬──────────┐
    ↓           ↓          ↓
 [Worker A] [Worker B] [Worker C]
 (Expert A) (Expert B) (Expert C)
```

## Implementation Recipes

### 1. Supervisor Configuration

The Supervisor classifies user intent and delegates to workers.

```python
from google.adk.agents import Agent
from google.adk.planners import BuiltInPlanner

supervisor = Agent(
    name="supervisor",
    model="gemini-2.0-flash",
    instruction="""
    You are the Supervisor. Your role is to understand the user's goal 
    and delegate to the right specialist:
    - Specialist A: Handles X.
    - Specialist B: Handles Y.
    
    Use transfer_to_agent to delegate.
    """,
    sub_agents=[specialist_a, specialist_b]
)
```

### 2. Worker Configuration

Workers focus on execution and hand back to the Supervisor when finished.

```python
worker = Agent(
    name="specialist_a",
    model="gemini-2.0-flash",
    instruction="""
    You are Specialist A. You excel at X.
    1. Perform X using tool_x.
    2. Confirm with the user.
    3. Once satisfied, inform them you are handing back to the Supervisor.
    """
)
```

### 3. State Sharing

Use common keys in `tool_context.state` to maintain continuity.

```python
# In Tool A
tool_context.state["working_file"] = "gs://bucket/image.png"

# In Tool B (used by a different agent)
image_uri = tool_context.state.get("working_file")
```

## When to Use SCION

- **Complex Workflows**: Multi-stage processes (e.g., Try-On -> Edit -> Animate).
- **High-Reliability Tasks**: Where specific models or instruction sets improve output quality.
- **Audit-Sensitive Routing**: Where you need to track exactly which specialist handled a request.
- **Large Toolsets**: Breaking tools across specialized agents prevents "tool fatigue" and reduces hallucinations.

## Best Practices

- **Minimal Tools for Workers**: Only give a worker the tools it absolutely needs.
- **Clear Descriptions**: Set the `description` field on sub-agents accurately so the Supervisor knows when to call them.
- **Shared Instructions**: Use a `GLOBAL_INSTRUCTION` for context common to the entire team.
- **Supervisor-only Greeting**: Only the Supervisor should handle the initial greeting and high-level project management.
