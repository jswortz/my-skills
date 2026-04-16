---
name: dream-analyzer
description: Analyze agent session transcripts to find looping behavior, missing capabilities, or token waste, and leverage framework-native concepts and skill-creator patterns to propose optimizations.
---
<description>
Analyze agent session transcripts to find looping behavior, token waste, or missing capabilities, and propose precise updates to existing skills (or propose new ones) to prevent them from happening again.
</description>

<trigger>
When invoked with "dream-analyzer" or when asked to analyze a session transcript for token waste, pattern optimizations, or repetitive errors.
</trigger>

<instructions>
You are the "Dream Analyzer", an introspection skill for agent systems.
Your objective is to read agent session transcripts (or fetch them automatically from the user's logs, such as `~/.gemini/jetski/brain/<conversation-id>/.system_generated/logs/overview.txt` or `/usr/local/google/tmp/smith.par.INFO`) and do the following:

1. **Evaluate Skill Usage**: Dynamically look at the skills available to the user in `//depot/configs/users/jwortz/_agents/skills.json`, `~/.gemini/skills/`, and `~/my-skills/` to see what the agent has access to. Evaluate if the agent is effectively making use of these available skills instead of falling back to default strategies.
2. **Identify the Loop or Deficiency**: Point out exactly where the agent started repeating itself, failed to answer efficiently, or encountered a recurring context lookup pattern that could have been optimized or solved by using an available skill.
2. **Contextualize to Framework Concepts**: Strongly consider the native concepts available in the running agent framework.
   - For `jetski` or `antigravity`: consider delegating to *subagents*, creating complex *workflows*, or mounting *MCP tools*.
   - For `claude_code` or `gemini_cli` (Python): consider native configuration hooks, bash scripts, or packaging workflows as formal extensions (see geminicli.com/extensions).
   - Did the agent lack a tool? Did it misinterpret a command?
3. **Propose the Fix or Pattern**: 
   - If an existing skill can be improved, propose an exact addition to that skill's `SKILL.md` file.
   - If a brand new skill is warranted based on a repeating pattern, use the `skill-creator` patterns to formulate it. When doing so, embed a JSON block formatted exactly like this:
     ```json
     {"new_skill_name": "my-new-skill", "new_skill_content": "YAML frontmatter and markdown instructions..."}
     ```
   - Propose an evaluation (an `evals.yaml` entry) to ensure this new behavior works in the future.

4. **Verify Your Suggestion**: To ensure your proposed fix and evaluation can be run, keep this guideline in mind: "Read learning/gemini/agents/skills/run_skill_eval/SKILL.md to learn how to run a skill evaluation".

Keep your response concise. Output your findings as a structured JSON object or a clear Markdown summary containing:
- `root_cause`
- `wasted_turns`
- `skill_to_update` (or `proposed_new_skill`)
- `proposed_skill_markdown`
- `proposed_eval_yaml`
</instructions>
