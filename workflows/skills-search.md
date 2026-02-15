---
description: Search for available global skills by keyword
---

1. Ask the user for the keyword if not provided.
2. Use `grep_search` to look for the keyword in `~/.gemini/antigravity/global_skills`.
   - Focus on `SKILL.md` files.
   - Example: `grep_search(Query="keyword", SearchPath="~/.gemini/antigravity/global_skills", Includes=["**/SKILL.md"])`
3. Present the relevant skills found to the user.
