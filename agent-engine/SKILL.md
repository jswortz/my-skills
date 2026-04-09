---
name: agent-engine
description: Deploy and manage AI agents on Vertex AI Agent Engine. Use when deploying ADK agents to production, configuring Agent Engine runtime, managing deployed agents, setting up sessions and memory, or integrating with A2A protocol. Covers deployment from agent objects and source files, environment configuration, scaling, sessions, memory bank, and agent management operations.
---

# Vertex AI Agent Engine

Deploy, manage, and scale AI agents in production on Google Cloud.

## Quick Reference

| Task | Pattern |
|------|---------|
| Install SDK | `pip install google-cloud-aiplatform[agent_engines,adk]` |
| Initialize client | `vertexai.Client(project, location)` |
| Deploy agent | `client.agent_engines.create(agent=app, config={...})` |
| Query agent | `remote_agent.stream_query(user_id, message)` |
| Delete agent | `remote_agent.delete(force=True)` |


## Advanced Details & Examples
For advanced configurations, detailed examples, and more information, see [references/details.md](references/details.md).
