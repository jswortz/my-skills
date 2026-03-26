# Jira MCP Integration

## Setup

Install the MCP server:
```bash
pip install mcp-atlassian
```

Add to `~/.claude/.mcp.json`:
```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": ["mcp-atlassian"],
      "env": {
        "JIRA_URL": "https://your-company.atlassian.net",
        "JIRA_USERNAME": "your.email@company.com",
        "JIRA_API_TOKEN": "your_api_token"
      }
    }
  }
}
```

Generate an API token at: https://id.atlassian.com/manage-profile/security/api-tokens

## Available Jira Tools

Once configured, agents can use these MCP tools:

| Tool | Description |
|------|-------------|
| `jira_get_issue` | Get issue details by key (e.g., PROJ-123) |
| `jira_search` | Search issues via JQL |
| `jira_create_issue` | Create new issue |
| `jira_update_issue` | Update issue fields |
| `jira_add_comment` | Add comment to issue |
| `jira_list_sprints` | List sprints for a board |
| `jira_get_sprint_issues` | Get issues in a sprint |
| `jira_transition_issue` | Move issue to new status |

## Sprint Planning with Jira

The scrum-master agent can pull stories from Jira:
```
"Pull all stories from sprint 42 in project GROCERY, break them into implementation tasks, and create a TaskList with dependencies."
```

## Syncing Status

After completing work, agents can update Jira:
```
"Transition GROCERY-456 to 'Done' and add a comment with the implementation summary."
```

## Confluence Integration

Add Confluence credentials to the same MCP config to also access:
- `confluence_get_page` — Read wiki pages
- `confluence_search` — Search Confluence
- `confluence_create_page` — Create new pages
- `confluence_update_page` — Update existing pages

Useful for storing sprint retrospective notes and architecture decisions.
