# Troubleshooting

| Issue | Solution |
|-------|----------|
| `PERMISSION_DENIED` on streamAssist | Ensure `X-Goog-User-Project` header is set |
| Token overflow (>1M input tokens) | Use `data_store_specs` to filter stores; remove workspace connectors |
| Document import stuck | Check GCS permissions; verify JSONL metadata format |
| Agent returns empty response | Verify documents are indexed (check import LRO status) |
| Model Armor blocks all queries | Check confidence levels; use `FAIL_OPEN` during testing |
| VertexAiSearchTool + sub-agents fails | Switch to `DiscoveryEngineSearchTool` |
| 403 on workspace data store | Workspace connectors require user OAuth, not service account |
| Engine creation fails | Ensure data stores exist first — engine references them |
| Regional vs global mismatch | Engine and data stores must be in the same location |
| Model Armor location error | Use `us` multi-region (not `us-central1`) for global engines |

## Browser Automation (GE UI)

GE's web UI uses deep shadow DOM. Standard `document.body.innerText` returns empty for chat content.

**Only reliable text extraction:** CDP `Accessibility.getFullAXTree` — penetrates all shadow roots, returns visible text only.

**Critical patterns:**
- `@AgentName` dropdown: type `@Trend`, click `page.locator("text=Trends2Insights")`, or ArrowDown+Enter
- **Clear agent bar after first message**: `button[aria-label*="clear"]` — otherwise "continue" routes to the agent, not the root orchestrator
- **False positives**: User prompt contains pipeline keywords ("focus group", "commercial"). Track text growth from baseline.
- **Thinking is transient**: Only visible mid-response, disappears when response completes.

Full guide: **[references/browser_automation.md](references/browser_automation.md)**

## References

- **[references/api_reference.md](references/api_reference.md)** — Complete REST API endpoint reference with payloads and response formats
- **[references/provisioning.md](references/provisioning.md)** — Step-by-step provisioning guide for engines, data stores, Model Armor
- **[references/browser_automation.md](references/browser_automation.md)** — GE browser automation with Playwright + CDP (shadow DOM parsing)
- **[scripts/stream_assist_client.py](scripts/stream_assist_client.py)** — Portable StreamAssist REST client with retry logic
