---
name: Remembering Conversations
description: Search previous Gemini CLI conversations for facts, patterns, decisions, and context using semantic or text search. Use when partner mentions past discussions, debugging familiar issues, or seeking historical context about decisions and patterns.
---

# Remembering Conversations

Search archived conversations using semantic similarity or exact text matching.

**Core principle:** Search before reinventing.

**Announce:** "I'm searching previous conversations for [topic]."

**Setup:** See INDEXING.md

## When to Use

**Search when:**
- Your human partner mentions "we discussed this before"
- Debugging similar issues
- Looking for architectural decisions or patterns
- Before implementing something familiar

**Don't search when:**
- Info in current conversation
- Question about current codebase (use Grep/Read)

## In-Session Use

**Always use subagents** (50-100x context savings). See skills/using-skills for workflow.

## Direct Search (Manual/CLI)

For humans outside Gemini CLI sessions, use the direct search tool. Details are in [references/direct-search.md](references/direct-search.md).