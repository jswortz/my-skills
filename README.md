# My Custom Skills

Custom skills, workflows, and rules for Claude Code and Gemini CLI (Antigravity).

## Skills

### Google ADK / Agent Engine / A2A

| Skill | Description |
|-------|-------------|
| [a2a](a2a/) | Build multi-agent systems using Google ADK with A2A protocol, deployed on Agent Engine |
| [adk](adk/) | Build AI agents using Google's Agent Development Kit (ADK) |
| [agent-engine](agent-engine/) | Deploy and manage AI agents on Vertex AI Agent Engine |
| [agent-development](agent-development/) | Create agents, write subagents, generate agent frontmatter |
| [gemini-enterprise](gemini-enterprise/) | Work with Google's Gemini Enterprise (Discovery Engine API) for enterprise search, conversational AI, Model Armor, and external agent registration |

### Diagrams & Visualization

| Skill | Description |
|-------|-------------|
| [gcp-diagram](gcp-diagram/) | Generate GCP-branded architecture diagrams using Gemini image generation |
| [generate-diagram](generate-diagram/) | Generate publication-quality methodology diagrams from text |
| [generate-plot](generate-plot/) | Generate publication-quality statistical plots from JSON data |
| [evaluate-diagram](evaluate-diagram/) | Evaluate generated diagrams against human references |
| [claude-d3js-skill](claude-d3js-skill/) | Create interactive data visualizations using d3.js |

### Browser Automation & Testing

| Skill | Description |
|-------|-------------|
| [browser-use](browser-use/) | AI-powered browser automation using the browser-use Python library |
| [playwright-skill](playwright-skill/) | Complete browser automation with Playwright |

### Security Analysis

| Skill | Description |
|-------|-------------|
| [building-secure-contracts](building-secure-contracts/) | Build secure code contracts |
| [burpsuite-project-parser](burpsuite-project-parser/) | Parse BurpSuite project files |
| [constant-time-analysis](constant-time-analysis/) | Analyze constant-time properties |
| [defense-in-depth](defense-in-depth/) | Validate at every layer data passes through |
| [differential-review](differential-review/) | Differential code review |
| [entry-point-analyzer](entry-point-analyzer/) | Analyze code entry points |
| [firebase-apk-scanner](firebase-apk-scanner/) | Scan Firebase APK files |
| [semgrep-rule-creator](semgrep-rule-creator/) | Create Semgrep rules |
| [semgrep-rule-variant-creator](semgrep-rule-variant-creator/) | Create Semgrep rule variants |
| [sharp-edges](sharp-edges/) | Identify sharp edges in code |
| [spec-to-code-compliance](spec-to-code-compliance/) | Verify spec-to-code compliance |
| [static-analysis](static-analysis/) | Static code analysis |
| [variant-analysis](variant-analysis/) | Variant analysis for vulnerability patterns |
| [audit-context-building](audit-context-building/) | Build audit context |

### Development Workflow

| Skill | Description |
|-------|-------------|
| [brainstorming](brainstorming/) | Explore user intent, requirements and design before implementation |
| [dispatching-parallel-agents](dispatching-parallel-agents/) | Dispatch 2+ independent tasks without shared state |
| [doc-coauthoring](doc-coauthoring/) | Structured workflow for co-authoring documentation |
| [executing-plans](executing-plans/) | Execute implementation plans with review checkpoints |
| [finishing-a-development-branch](finishing-a-development-branch/) | Guide completion of development work (merge, PR, cleanup) |
| [fix-review](fix-review/) | Fix review workflow |
| [ralph-wiggum](ralph-wiggum/) | Iterative development loop (fix until passing) |
| [receiving-code-review](receiving-code-review/) | Handle code review feedback with technical rigor |
| [requesting-code-review](requesting-code-review/) | Verify work meets requirements before merging |
| [subagent-driven-development](subagent-driven-development/) | Execute plans with independent tasks via subagents |
| [systematic-debugging](systematic-debugging/) | Debug bugs and test failures systematically |
| [test-driven-development](test-driven-development/) | TDD before writing implementation code |
| [using-git-worktrees](using-git-worktrees/) | Create isolated git worktrees for feature work |
| [verification-before-completion](verification-before-completion/) | Verify before claiming work is complete |
| [writing-plans](writing-plans/) | Plan multi-step tasks before touching code |
| [writing-skills](writing-skills/) | Create, edit, and verify skills |
| [writing-rules](writing-rules/) | Create hookify rules and hook configurations |

### Testing

| Skill | Description |
|-------|-------------|
| [condition-based-waiting](condition-based-waiting/) | Replace arbitrary timeouts with condition polling |
| [property-based-testing](property-based-testing/) | Property-based testing patterns |
| [testing-anti-patterns](testing-anti-patterns/) | Avoid testing anti-patterns (never test mock behavior, etc.) |
| [testing-handbook-skills](testing-handbook-skills/) | Testing handbook reference |
| [testing-skills-with-subagents](testing-skills-with-subagents/) | RED-GREEN-REFACTOR for process documentation |

### Thinking & Problem Solving

| Skill | Description |
|-------|-------------|
| [collision-zone-thinking](collision-zone-thinking/) | Force unrelated concepts together to discover emergent properties |
| [inversion-exercise](inversion-exercise/) | Flip core assumptions to reveal hidden constraints |
| [meta-pattern-recognition](meta-pattern-recognition/) | Spot patterns appearing in 3+ domains |
| [preserving-productive-tensions](preserving-productive-tensions/) | Preserve multiple valid approaches instead of forcing premature resolution |
| [root-cause-tracing](root-cause-tracing/) | Trace bugs backward through call stack to find original trigger |
| [scale-game](scale-game/) | Test at extremes to expose fundamental truths |
| [simplification-cascades](simplification-cascades/) | Find insights that eliminate multiple components |
| [tracing-knowledge-lineages](tracing-knowledge-lineages/) | Understand how ideas evolved over time |
| [when-stuck](when-stuck/) | Dispatch to the right problem-solving technique |

### Meta / Tooling

| Skill | Description |
|-------|-------------|
| [ask-questions-if-underspecified](ask-questions-if-underspecified/) | Ask clarifying questions for underspecified tasks |
| [claude-in-chrome-troubleshooting](claude-in-chrome-troubleshooting/) | Troubleshoot Claude in Chrome |
| [claude-md-improver](claude-md-improver/) | Audit and improve CLAUDE.md files |
| [culture-index](culture-index/) | Culture index interpretation |
| [dwarf-expert](dwarf-expert/) | DWARF debug format expertise |
| [folder-sync](folder-sync/) | Keep two directories synchronized |
| [gardening-skills-wiki](gardening-skills-wiki/) | Maintain skills wiki health |
| [modern-python](modern-python/) | Modern Python development patterns |
| [pulling-updates-from-skills-repository](pulling-updates-from-skills-repository/) | Sync local skills with upstream |
| [remembering-conversations](remembering-conversations/) | Search previous conversations for context |
| [sharing-skills](sharing-skills/) | Contribute skills back upstream via PR |
| [superpowers](superpowers/) | Superpowers meta-skill |
| [superpowers-skills](superpowers-skills/) | Superpowers skills collection |
| [using-superpowers](using-superpowers/) | Find and use skills at conversation start |

## Workflows

Gemini CLI (Antigravity) workflow definitions in [`workflows/`](workflows/).

| Workflow | File |
|----------|------|
| Art | [art.md](workflows/art.md) |
| Brainstorm | [brainstorm.md](workflows/brainstorm.md) |
| Conform | [conform.md](workflows/conform.md) |
| Create Skill | [create-skill.md](workflows/create-skill.md) |
| D3 Visualization | [d3.md](workflows/d3.md) |
| Debug | [debug.md](workflows/debug.md) |
| Execute Plan | [execute-plan.md](workflows/execute-plan.md) |
| Frontend | [frontend.md](workflows/frontend.md) |
| Playwright | [playwright.md](workflows/playwright.md) |
| Property Test | [property-test.md](workflows/property-test.md) |
| Read ADK Docs | [read-adk-docs.md](workflows/read-adk-docs.md) |
| Refresh Docs | [refresh-docs.md](workflows/refresh-docs.md) |
| Review | [review.md](workflows/review.md) |
| Secure Code | [secure-code.md](workflows/secure-code.md) |
| Sharp Edges | [sharp-edges.md](workflows/sharp-edges.md) |
| Skills Search | [skills-search.md](workflows/skills-search.md) |
| Subagent | [subagent.md](workflows/subagent.md) |
| Sync Skills | [sync-skills.md](workflows/sync-skills.md) |
| TDD | [tdd.md](workflows/tdd.md) |
| Worktree | [worktree.md](workflows/worktree.md) |
| Write Plan | [write-plan.md](workflows/write-plan.md) |

## Rules

Gemini CLI rules in [`rules/GEMINI.md`](rules/GEMINI.md).

## Installation

### Claude Code Skills

Copy individual skill directories into `~/.claude/skills/`:

```bash
cp -r <skill-name> ~/.claude/skills/
```

### Gemini CLI Workflows

Copy workflow files into `~/.gemini/jetski/global_workflows/`:

```bash
cp workflows/*.md ~/.gemini/jetski/global_workflows/
```

### Gemini CLI Rules

Append or merge `rules/GEMINI.md` into `~/.gemini/GEMINI.md`.
