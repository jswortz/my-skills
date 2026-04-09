# Gemini CLI Skills Repository (my-skills)

This repository is the central source of truth for specialized Gemini skills and agents. It contains modular capabilities that extend the Gemini CLI through structured documentation, scripts, and assets.

## Strategic Workflow
- **Skill Maintenance:** Use `skill_architect` to audit and update skills.
- **Visual Documentation:** Use `diagram_wizard` for all architecture diagrams.
- **Iterative Improvement:** Use `ralph_optimizer` for prompt tuning and bug fixing.
- **Data Analysis:** Use `bigquery_expert` for all BigQuery-related tasks.

## Skill Standards
1. **Concise metadata:** Descriptions must be trigger-focused.
2. **Progressive disclosure:** Keep `SKILL.md` body lean; move details to `references/`.
3. **Deterministic scripts:** Use Python/Bash for repetitive logic.
4. **Validation:** Always run `package_skill.py` before finalizing changes.

## Delegation Strategy
Always consider if a task should be handled by a sub-agent.
- Adding a new skill? Delegate to `skill_architect`.
- Refactoring multiple skills? Delegate to `generalist`.
- Analyzing repository patterns? Delegate to `codebase_investigator`.
