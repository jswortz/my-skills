---
name: a2a
description: Build multi-agent systems using Google ADK with A2A protocol, deployed on Agent Engine. Use when creating agents that communicate via A2A, building multi-tier agent hierarchies, connecting ADK agents with RemoteA2aAgent, exposing agents with to_a2a(), or deploying agent stacks to Vertex AI Agent Engine. Covers leaf agents with tools, functional agents that delegate, orchestrators that route, local testing with uvicorn, and phased cloud deployment.
---

# A2A Multi-Agent Development

Build multi-tier ADK agent systems using the A2A protocol, deployed to Agent Engine.

## Architecture Pattern

```
Level 1: Orchestrator (routes requests)
├── Level 2: Functional Agent A (delegates to leaf)
│   └── Level 3: Leaf Agent A (has tools, does work)
└── Level 2: Functional Agent B (delegates to leaf)
    └── Level 3: Leaf Agent B (has tools, does work)
```

**Key principle:** Leaf agents have tools. Functional agents delegate. Orchestrators route.


## Advanced Details & Examples
For advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).
