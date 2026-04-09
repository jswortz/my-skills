---
name: novastorm-tracker
description: Guide and recipes for managing Buganizer issues for the NovaStorm project
  (Component ID 2059327).
---
# NovaStorm Tracker Skill

Use this skill when managing Buganizer issues for the NovaStorm project. It provides recipes and default configurations to interact with the Buganizer MCP using the correct Component ID (`2059327`).

## Configuration
The default component ID for NovaStorm is `2059327`.

### Required Attributes
Issues should have the following attributes:
-   **Status**: `NEW` (if possible, otherwise `ASSIGNED`).
-   **Assignee**: The user (e.g. `jwortz@google.com`).
-   **Planned For**: `NovaStorm: Dynamic Swarm Intelligence (DSSIB) on Google Cloud`.

### Automatic Setting via Comments
To set attributes automatically (if not supported by tool parameters), use comment commands in the initial description or a follow-up comment.

**Using Comment Commands:**
-   `/status NEW`
-   `/assign jwortz@google.com`
-   `/planned-for "NovaStorm: Dynamic Swarm Intelligence (DSSIB) on Google Cloud"`

*Note: Status might automatically become ASSIGNED if an assignee is present. Planned For may require manual setting if tools do not support it.*

## Common Recipes

### 1. List Open Issues
Use this recipe to list open bugs in the NovaStorm component.
```bash
# Using Buganizer MCP (conceptual example, use actual tool)
# query: "componentid:2059327 status:open"
```
*Note: Since the Buganizer MCP tools require explicit parameters, use the following patterns.*

**Using `mcp_buganizer_get_bugs` Tool:**
- `query`: `componentid:2059327 status:open`
- `maxResults`: `10` (default)

### 2. Create a New Bug
Use this recipe to file a new bug in the NovaStorm component.

**Using `mcp_buganizer_create_buganizer_issue` Tool:**
- `componentId`: `"2059327"`
- `title`: `"[Category] Brief description"`
- `commentMarkdown`: `"Detailed description..."`
- `priority`: `"P2"` (default)
- `severity`: `"S2"` (default)

### 3. Search Issues
Search for specific text within the NovaStorm component.

**Using `mcp_buganizer_get_bugs` Tool:**
- `query`: `componentid:2059327 "search term"`

### 4. Check Phase 3 Status
List issues related to Phase 3 implementation.

**Using `mcp_buganizer_get_bugs` Tool:**
- `query`: `componentid:2059327 "Phase 3"`

## Best Practices
1. **Always** use `componentId: "2059327"` when creating or listing issues for NovaStorm unless specifically directed otherwise.
2. Structure titles with categories where applicable, e.g. `[GEPA]`, `[Critic Agent]`, `[Cloud Run]`, `[Dataplex]`, `[Multi-Agent]`, `[Memory Bank]`, etc.
3. Use Markdown in comments for better readability.

## Evaluation
For evaluation criteria, see [references/evaluate.md](references/evaluate.md).
